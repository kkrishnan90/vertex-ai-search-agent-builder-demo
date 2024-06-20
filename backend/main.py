from fastapi import FastAPI, File, UploadFile, HTTPException
import os
from env import load_dotenv
import json
from pydantic import BaseModel
from search import search_discovery_engine
from upload import upload_to_gcs
from datastore import import_documents_sample
from fastapi.middleware.cors import CORSMiddleware
import uuid
from fastapi.staticfiles import StaticFiles

load_dotenv('.env')

LOCATION = os.getenv("LOCATION")

# Define Pydantic models for request data


class QueryModel(BaseModel):
    query: str
    summary_result_count: int = 3
    page_size: int = 10
    max_snippet_count: int = 5
    include_citations: bool = True
    use_semantic_chunks: bool = True
    max_extractive_answer_count: int = 3
    max_extractive_segment_count: int = 3


class DatastoreImportModel(BaseModel):
    pdf_gcs_filename: str
    category: str
    tenant: str
    description: str
    year: str


# Create FastAPI app
app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    # Allow all origins (for development, be more specific in production)
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


# Define API endpoints


@app.get("/ping")
async def ping():
    """
    Simple endpoint to check if the API is running.

    Returns:
        dict: A dictionary with a "status" key set to "pong".
    """
    return {"status": "pong"}


@app.post("/search")
async def search(query_model: QueryModel):
    """
    Searches the Discovery Engine for documents matching the provided query.

    Args:
        query_model (QueryModel): A Pydantic model containing the search query and other parameters.

    Returns:
        dict: A dictionary containing the search results.
    """
    results = search_discovery_engine(
        location=LOCATION, search_query=query_model.query, summary_result_count=query_model.summary_result_count,
        page_size=query_model.page_size, max_snippet_count=query_model.max_snippet_count,
        include_citations=query_model.include_citations, use_semantic_chunks=query_model.use_semantic_chunks,
        max_extractive_answer_count=query_model.max_extractive_answer_count,
        max_extractive_segment_count=query_model.max_extractive_segment_count)
    return results


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a PDF file to Google Cloud Storage.

    Args:
        file (UploadFile): The PDF file to upload.

    Returns:
        dict: A dictionary containing the uploaded file name and public URL.

    Raises:
        HTTPException: If the file type is not a PDF or if the upload fails.
    """
    try:
        # Validate file type
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400, detail="Only PDF files are allowed")

        file_obj = file.file
        file_name = f"docs/{file.filename}"
        public_url = upload_to_gcs(
            file_obj, file_name, content_type="application/pdf")
        return {"file_name": file_name, "url": public_url}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"File upload failed: {str(e)}")


@app.post("/datastore/import")
async def import_data(data: DatastoreImportModel):
    """
    Imports a PDF document into Cloud Datastore.

    Args:
        data (DatastoreImportModel): A Pydantic model containing the PDF file's GCS filename, category, tenant, description, and year.

    Returns:
        dict: A dictionary containing the status, data, URL, and Datastore response.

    Raises:
        HTTPException: If the Datastore import fails.
    """
    try:
        bucket_name = os.getenv("BUCKET_NAME")
        full_gcs_path = f"gs://{bucket_name}/{data.pdf_gcs_filename}"

        # Build document data for NDJSON file
        doc_data = {
            "id": f"doc-{uuid.uuid4()}",
            "structData": {
                "title": data.pdf_gcs_filename,
                "description": data.description,
                "year": data.year,
                "category": data.category,
                "tenant": data.tenant,
            },
            "content": {
                "mimeType": "application/pdf",
                "uri": full_gcs_path,
            },
        }

        # Extract filename components
        actual_filename = data.pdf_gcs_filename.split("/")[1]
        filename_without_extension = actual_filename.split(".")[0]
        ndjson_filename = f"{filename_without_extension}.json"

        # Create and upload NDJSON file
        with open(ndjson_filename, "w") as ndjson_file:
            json.dump(doc_data, ndjson_file)

        with open(ndjson_filename, "r") as ndjson_file:
            ndjson_public_url = upload_to_gcs(
                ndjson_file, ndjson_filename, content_type="application/json")

        uploaded_ndjson_path = f"gs://{bucket_name}/{ndjson_filename}"
        response = import_documents_sample(uploaded_ndjson_path)

        return {
            "status": "success",
            "data": ndjson_filename,
            "url": ndjson_public_url,
            "datastore": response
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Datastore import failed: {str(e)}")

# Serve the static files (uncomment only if running locally)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

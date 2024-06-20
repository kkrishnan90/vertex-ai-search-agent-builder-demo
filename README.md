# Google Quality Search Engine with Your Own Data

This repository demonstrates how to build a Google-quality search engine with your own data using
Google Cloud Vertex AI Agent Builder and search agent.

## Prerequisites

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```

## Local Development

### Backend Setup

1. **Create a virtual environment**:

   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare environment variables**:

   - Change the `.env` file in the location `backend/.env` and update all values. Fill in the values as required and as per your project.

4. **Avoid serving static files locally**:

   - Comment the last line in `backend/main.py` to avoid serving static files when running locally.

5. **Run the backend**:
   ```sh
   uvicorn main:app --reload
   ```

### Frontend Setup

1. **Navigate to the frontend directory**:

   ```sh
   cd frontend
   ```

2. **Install dependencies**:

   ```sh
   npm install
   ```

3. **Run the frontend**:
   ```sh
   npm run start
   ```

## Cloud Deployment

To deploy this application on Cloud Run:

1. **Connect your GitHub repository to Cloud Build**:

   - Follow [this guide](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github) to connect your GitHub repository to Cloud Build.

2. **Run the build**:

   - Once linked, trigger the build manually or set up a push trigger.

3. **Cloud Build and Deployment**:
   - The `cloudbuild.yaml` file in the root directory will handle the creation of the container using the Dockerfile and deploy it to Cloud Run.
   - The application will be accessible through an unauthenticated public endpoint on Cloud Run.

### Note for Cloud Deployment

- If running on Cloud Run, ensure to uncomment the last line of `backend/main.py` to serve static files.

## Architecture

This app employs the following architecture using Google Cloud services:

1. **Google Cloud Storage (GCS)**:

   - Upload a bunch of PDF files to a GCS bucket (recommended to use `alphabet-metadata.json` provided in the root folder).

2. **Vertex AI Agent Builder**:

   - **Create a Datastore**:
     - Follow [this guide](https://cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#cloud-storage) to create a datastore on Vertex AI Agent Builder, selecting Cloud Storage as the source and the GCS bucket where files are uploaded.
   - **Create an App**:
     - Create an app and select 'search' as the agent. Refer to [this guide](https://cloud.google.com/generative-ai-app-builder/docs/create-engine-es) for detailed instructions.

3. **Preview Search**:
   - Once the files are indexed, you can preview your search on the Google Cloud console.

## Google Cloud Services Used

1. **Cloud Build API**
2. **Cloud Run API**
3. **Vertex AI Search API**

For ease of use, a metadata JSON file of publicly available Alphabet reports (`alphabet-metadata.json`) is provided in the root folder of this project.

## Conclusion

This application provides a comprehensive understanding of leveraging Google Cloud services to build a powerful search engine with your own data. By following the steps outlined above, you can set up the application locally, deploy it on Cloud Run, and explore the capabilities of Google Cloud Vertex AI Agent Builder.
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine
import os
import json

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
DATASTORE_ID = os.getenv("DATASTORE_ID")


def import_documents_sample(
    gcs_uri: Optional[str] = None,
    bigquery_dataset: Optional[str] = None,
    bigquery_table: Optional[str] = None,
) -> str:
    """Imports documents into a Vertex AI Search Datastore.

    This function imports documents into a Vertex AI Search Datastore from either a Google Cloud Storage (GCS) URI or a BigQuery table.

    Args:
        gcs_uri (Optional[str]): The GCS URI of the jsonl file containing the documents to import.
        bigquery_dataset (Optional[str]): The BigQuery dataset containing the documents to import.
        bigquery_table (Optional[str]): The BigQuery table containing the documents to import.

    Returns:
        str: The name of the operation that was created.

    Raises:
        ValueError: If both `gcs_uri` and `bigquery_dataset` are provided.
    """
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(
            api_endpoint=f"{LOCATION}-discoveryengine.googleapis.com")
        if LOCATION != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DocumentServiceClient(
        client_options=client_options)

    # The full resource name of the search engine branch.
    # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
    parent = client.branch_path(
        project=PROJECT_ID,
        location=LOCATION,
        data_store=DATASTORE_ID,
        branch="default_branch",
    )

    if gcs_uri:
        request = discoveryengine.ImportDocumentsRequest(
            parent=parent,
            gcs_source=discoveryengine.GcsSource(
                input_uris=[gcs_uri]
            ),
            # Options: `FULL`, `INCREMENTAL`
            reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
        )
    else:
        request = discoveryengine.ImportDocumentsRequest(
            parent=parent,
            bigquery_source=discoveryengine.BigQuerySource(
                project_id=PROJECT_ID,
                dataset_id=bigquery_dataset,
                table_id=bigquery_table,
                data_schema="custom",
            ),
            # Options: `FULL`, `INCREMENTAL`
            reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
        )

    # Make the request
    operation = client.import_documents(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # Once the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

    return operation.operation.name

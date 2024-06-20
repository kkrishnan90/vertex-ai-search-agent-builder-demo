from google.cloud import storage
import os
import logging
from wrapper import log_data


storage_client = storage.Client()


@log_data
def upload_to_gcs(file_obj, file_name, content_type):
    """
    Uploads a file to Google Cloud Storage.

    Args:
        file_obj: The file object to upload.
        file_name: The name of the file to upload.
        content_type: The content type of the file.

    Returns:
        str: The public URL of the uploaded file.

    Raises:
        Exception: If the upload fails.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(os.getenv("BUCKET_NAME"))
        blob = bucket.blob(file_name)
        blob.upload_from_file(file_obj, content_type=content_type)
        return blob.public_url
    except Exception as e:
        logging.getLogger().error(e)
        return f"Failed to upload file {file_name} to bucket {os.getenv('BUCKET_NAME')} due to {e}"

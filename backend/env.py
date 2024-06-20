import os
from dotenv import load_dotenv
from wrapper import log_data


load_dotenv('.env')

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
BUCKET_NAME = os.getenv("BUCKET_NAME")
DATASTORE_ID = os.getenv("DATASTORE_ID")
AGENT_APPLICATION_ID = os.getenv("AGENT_APPLICATION_ID")


# Check if environment variables are empty and load from Cloud Run if necessary
if not PROJECT_ID:
    PROJECT_ID = os.getenv("PROJECT_ID", None)
if not LOCATION:
    LOCATION = os.getenv("LOCATION", None)
if not BUCKET_NAME:
    BUCKET_NAME = os.getenv("BUCKET_NAME", None)
if not DATASTORE_ID:
    DATASTORE_ID = os.getenv("DATASTORE_ID", None)
if not AGENT_APPLICATION_ID:
    AGENT_APPLICATION_ID = os.getenv("AGENT_APPLICATION_ID", None)


@log_data
def show_all_env():
    """
   Retrieves and displays all environment variables.

   This function reads environment variables from a .env file using the `dotenv` library.
   It then returns a formatted string containing the values of the following variables:

   - PROJECT_ID
   - LOCATION
   - BUCKET_NAME
   - DATASTORE_ID
   - AGENT_APPLICATION_ID

   Returns:
       str: A string containing the values of all environment variables.
   """
    response = f"""PROJECT_ID: {PROJECT_ID}\nLOCATION: {LOCATION}\nBUCKET_NAME: {BUCKET_NAME}\nDATASTORE_ID: {DATASTORE_ID}\nAGENT_APPLICATION_ID: {AGENT_APPLICATION_ID}"""
    return response


show_all_env()

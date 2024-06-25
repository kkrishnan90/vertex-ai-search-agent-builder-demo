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
4. **Service Account Roles for Google Quality Search Engine**

This document outlines the specific roles required for the service account used by the Google Quality Search Engine application to function correctly on Google Cloud.

**Required Roles**

The service account needs the following roles to access and interact with the necessary Google Cloud services:

1. **Vertex AI Agent Builder:**

   - **Vertex AI Search Agent:** This role grants the service account the ability to create, manage, and interact with the search agent within Vertex AI Agent Builder. It allows the service account to index data, perform searches, and manage the search agent's configuration.

   - **Storage Object Viewer:** This role enables the service account to read data from the Cloud Storage bucket where the PDF files are stored. This is essential for the search agent to access the content of the files and index them for search.

2. **Cloud Run:**

   - **Cloud Run Invoker:** This role allows the service account to invoke Cloud Run services. This is crucial for deploying and running the backend application on Cloud Run. It enables the service account to trigger the backend service to handle search requests.

3. **Cloud Storage:**

   - **Storage Object Admin:** This role provides the service account with full control over objects in the Cloud Storage bucket. This includes uploading, deleting, and modifying files. It allows the service account to manage the PDF files used for indexing and search.

**Importance of Role Assignment**

- **Security:** Assigning specific roles to the service account ensures that it only has the necessary permissions to perform its tasks. This minimizes the risk of unauthorized access or actions.

- **Efficiency:** By granting only the required permissions, the service account operates with the least privilege, improving performance and reducing potential conflicts.

- **Compliance:** Adhering to the principle of least privilege is essential for compliance with security standards and regulations.

**Best Practices**

- **Review and Update:** Regularly review the roles assigned to the service account to ensure they remain appropriate and up-to-date.

- **Least Privilege:** Always strive to grant the minimum permissions necessary for the service account to function correctly.

- **Monitoring:** Monitor the service account's activity to detect any suspicious behavior or potential security breaches.

By following these guidelines and assigning the appropriate roles to the service account, you can ensure the secure and efficient operation of the Google Quality Search Engine application on Google Cloud.
For more information on service account and how to create or add roles to existing service account please refer to the link [https://cloud.google.com/iam/docs/service-accounts-create]

**Note for Cloud Deployment**

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

# Use a base image with Node.js and Python installed
FROM nikolaik/python-nodejs:python3.12-nodejs22

# Set working directories
WORKDIR /app

# Copy backend requirements file and install dependencies
COPY backend/requirements.txt /app/backend/
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy backend source code
COPY backend /app/backend

# Copy frontend package files and install dependencies
COPY frontend/package.json frontend/package-lock.json /app/frontend/
RUN cd /app/frontend && npm install

# Build the React app
COPY frontend /app/frontend
RUN cd /app/frontend && npm run build

# Copy the built React app to a directory served by FastAPI
RUN mkdir -p /app/backend/app/static
RUN cp -r /app/frontend/build/* /app/backend/app/static/

# Set the working directory to the backend
WORKDIR /app/backend

# Expose the port for the FastAPI app
EXPOSE 8000

# Run FastAPI and serve the React app
CMD ["fastapi","run","main.py", "--host", "0.0.0.0", "--port", "8000"]

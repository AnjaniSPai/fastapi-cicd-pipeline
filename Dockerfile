# STEP 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# STEP 1.5: Install system packages needed for build and testing
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

    # STEP 2: Set the working directory in the container
WORKDIR /usr/src/app

# STEP 3: Copy the requirements file and install dependencies
# This is a critical step for efficiency (caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# STEP 4: Copy the entire application code to the container
COPY . .

# STEP 5: Make the port 8000 available to the world outside this container
EXPOSE 8000

# STEP 6: Run the uvicorn server when the container starts
# The host 0.0.0.0 is needed for the server to be accessible outside the container
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# STEP 6: Run the uvicorn server when the container starts
CMD ["/usr/local/bin/python", "main.py"]
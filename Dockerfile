# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required by Librosa and audio libraries
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies without caching to keep image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project source code into the container
COPY . .

# Define the default command to run when the container starts
CMD ["python", "main.py"]
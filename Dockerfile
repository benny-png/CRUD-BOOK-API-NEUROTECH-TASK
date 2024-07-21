# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt /app/

# Install the dependencies specified in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the working directory
COPY . /app/

# Run the application
CMD ["uvicorn", "src.main.app:app", "--host", "0.0.0.0", "--port", "8000"]

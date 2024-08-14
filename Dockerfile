# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Expose the port that the app runs on
EXPOSE 8000

# Copy the requirements.txt file from the root directory to /code
COPY requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code from the app directory to /code/app
COPY app /code/app

# Copy the static files from the root directory to /code/static
COPY static /code/static

# Create a directory for the SQLite database
RUN mkdir -p /code/sqlitedb

# Define the command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
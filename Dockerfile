# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port and run the Django app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ARG TEST1=value1

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Expose the Flask app port
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Run the application
CMD ["flask", "run"]

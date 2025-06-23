# Dockerfile
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask prometheus-flask-exporter

# Expose Flask port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]


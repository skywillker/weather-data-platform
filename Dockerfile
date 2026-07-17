# Use the official slim image to reduce image size without affecting our application.
FROM python:3.13-slim

# Defines the work directory inside the container
WORKDIR /app

# Copy only the requirements archive first
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application only after installing dependencies to maximize Docker layer cache reuse.
COPY . .

# Command when the container starts
CMD ["python", "-m", "src.ingestion.weather_api"]
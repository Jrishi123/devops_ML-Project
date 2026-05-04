# Use official Python image
FROM python:3.11-slim
 
# Set working directory
WORKDIR /app
 
# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy application code
COPY app/ ./app/
COPY model/ ./model/
 
# Expose port
EXPOSE 8000
 
# Start the API server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
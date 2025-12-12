FROM python:3.13-slim

WORKDIR /app

# Set PYTHONPATH to ensure imports work correctly
ENV PYTHONPATH=/app

# Copy requirements and install dependencies
COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./backend/. /app

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


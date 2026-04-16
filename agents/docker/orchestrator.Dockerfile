FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY agents/scripts/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy orchestrator
COPY agents/scripts /app/scripts
COPY agents/config /app/config

# Create workspace directories
RUN mkdir -p /app/workspace/{threads,files,state,logs}

# Default command - run orchestrator
CMD ["python", "scripts/orchestrator.py"]

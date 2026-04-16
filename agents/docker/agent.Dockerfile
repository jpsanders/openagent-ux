FROM python:3.11-slim

WORKDIR /app

# Install Node.js and opencode
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g opencode \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY agents/scripts/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy agent config
COPY agents/config /app/config
COPY agents/roles /app/roles

# Default command
CMD ["python", "-m", "opencode", "--role", "$ROLE"]

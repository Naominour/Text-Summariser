FROM python:3.11-slim-buster

# Install dependencies
RUN apt-get update -y && apt-get install -y curl apt-transport-https lsb-release gnupg \
    && curl -sL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ buster main" > /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update -y \
    && apt-get install -y azure-cli

# Set working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install Python dependencies with increased timeout
RUN pip install --default-timeout=1000 -r requirements.txt

# Copy the rest of the source code
COPY . /app

# Set default command
CMD ["python", "app.py"]

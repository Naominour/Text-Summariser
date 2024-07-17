FROM python:3.11-slim-buster

# Install Azure CLI
RUN apt-get update -y && apt-get install -y curl apt-transport-https lsb-release gnupg \
    && curl -sL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl -sL https://packages.microsoft.com/repos/azure-cli/$(lsb_release -cs)/prod.list > /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update -y \
    && apt-get install -y azure-cli

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
FROM python:3.11-slim-buster

# Install Azure CLI
RUN apt-get update -y && apt-get install -y curl apt-transport-https lsb-release gnupg \
    && curl -sL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl -sL https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update -y \
    && apt-get install -y azure-cli

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
docker build -t naeimehacr.azurecr.io/myapp:latest .

echo "This is a test change" >> README.md
^X


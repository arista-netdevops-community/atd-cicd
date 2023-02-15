FROM python:3.9.7-slim

# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN ansible-galaxy collection install arista.avd
WORKDIR /app

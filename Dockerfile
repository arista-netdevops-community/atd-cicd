FROM python:3.9.16-slim

# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN ansible-galaxy collection install arista.avd arista.cvp community.general --force
RUN apt-get update && apt-get install build-essential -y
WORKDIR /app

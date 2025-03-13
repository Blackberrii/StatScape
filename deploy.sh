#!/bin/bash

# Exit on any error
set -e

# Check if running on ARM
if [ "$(uname -m)" != "aarch64" ]; then
    echo "Error: This script expects ARM64 architecture"
    exit 1
fi

echo "Updating system packages..."
sudo dnf update -y

echo "Installing Docker if not present..."
if ! command -v docker &> /dev/null; then
    sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install -y docker-ce docker-ce-cli containerd.io
    sudo systemctl start docker
    sudo systemctl enable docker
fi

# Create data directory if it doesn't exist
sudo mkdir -p /opt/statscape/data
sudo chown -R opc:opc /opt/statscape

echo "Building Docker image..."
docker build -t statscape-bot .

echo "Stopping existing container if running..."
docker stop statscape-bot 2>/dev/null || true
docker rm statscape-bot 2>/dev/null || true

echo "Starting new container..."
docker run -d \
  --name statscape-bot \
  --restart unless-stopped \
  --env-file .env \
  -v /opt/statscape/data:/app/data \
  statscape-bot

echo "Bot deployment complete!"
echo "You can check logs with: docker logs statscape-bot"

#!/bin/bash

# Exit on any error
set -e

# Ensure user has Docker permissions
if ! groups | grep -q docker; then
    echo "Adding user to docker group..."
    sudo usermod -aG docker $USER
    echo "Please log out and back in for group changes to take effect"
    echo "Then run this script again"
    exit 0
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
    statscape-bot

echo "Container started successfully!"

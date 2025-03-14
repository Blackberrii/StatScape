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

# Ensure .env exists
if [ ! -f /opt/statscape/.env ]; then
    echo "Error: .env file not found!"
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
echo "Verifying .env file exists and has content:"
ls -l .env
echo "ENV file contents (token hidden):"
cat .env | sed 's/=.*/=HIDDEN/'

docker build -t statscape-bot .

echo "Stopping existing container if running..."
docker stop statscape-bot 2>/dev/null || true
docker rm statscape-bot 2>/dev/null || true

echo "Starting new container..."
TOKEN=$(cat .env | grep DISCORD_BOT_TOKEN | cut -d'=' -f2)
echo "Token found (first 10 chars): ${TOKEN:0:10}..."

docker run -d \
    --name statscape-bot \
    --restart always \
    -e "DISCORD_BOT_TOKEN=${TOKEN}" \
    --memory="512m" \
    --memory-swap="1g" \
    statscape-bot

# Verify environment variable in container
echo "Verifying environment in container:"
docker exec statscape-bot env | grep DISCORD

echo "Container started successfully!"

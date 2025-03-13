#!/bin/bash

# Exit on any error
set -e

echo "Installing Docker..."
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf -y install docker-ce docker-ce-cli containerd.io

echo "Setting up Docker permissions..."
sudo usermod -aG docker opc
sudo systemctl start docker
sudo systemctl enable docker
sudo chmod 666 /var/run/docker.sock

# Ensure group membership is active
exec sudo su -l opc

echo "Creating installation directory..."
sudo mkdir -p /opt/statscape
sudo chown -R opc:opc /opt/statscape

echo "Copying files to installation directory..."
cp -r . /opt/statscape/

echo "Setting up systemd service..."
sudo cp /opt/statscape/statscape.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable statscape.service

echo "Starting the service..."
sudo systemctl start statscape.service

echo "Installation complete!"
echo "To check status: sudo systemctl status statscape"
echo "To view logs: docker logs statscape-bot"

chmod +x oracle-setup.sh deploy.sh

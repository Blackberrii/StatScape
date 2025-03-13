#!/bin/bash

# Exit on any error
set -e

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

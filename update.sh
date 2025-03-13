#!/bin/bash

# Save current directory and env file
cd /opt/statscape
cp .env ../env_backup

# Force reset and pull latest changes
git reset --hard
git clean -fd
git pull --force origin main

# Restore env file
mv ../env_backup .env

# Make scripts executable
chmod +x *.sh

# Rebuild and restart container
./deploy.sh

echo "Update complete!"

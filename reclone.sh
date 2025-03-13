#!/bin/bash

# Save your .env file temporarily
cp .env ~/statscape_env_backup

# Remove existing directory if it exists
rm -rf ~/StatScape

# Clone fresh from GitHub into home directory
cd ~
git clone https://github.com/blackberrii/StatScape.git

# Move into the directory
cd StatScape

# Restore your .env file
mv ~/statscape_env_backup .env 

# Make scripts executable again
chmod +x *.sh

echo "Repository has been successfully recloned!"

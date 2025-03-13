#!/bin/bash

# Save your .env file temporarily
cp .env ../statscape_env_backup

# Remove existing directory
cd ..
rm -rf StatScape

# Clone fresh from GitHub
git clone https://github.com/blackberrii/StatScape.git

# Move back into the directory
cd StatScape

# Restore your .env file
mv ../statscape_env_backup .env 

# Make scripts executable again
chmod +x *.sh

echo "Repository has been successfully recloned!"

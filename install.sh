#!/bin/bash
set -e

PROJECT_NAME="TinyVault"
REPO_URL="https://github.com/dakofds/TinyVault"

echo "Installing TinyVault..."
if [ ! -d "$ORIJECT_NAME" ]; then
	echo "Cloning repository..."
	git clone $REPO_URL
else
	echo "Repository already exists, pulling latest changes..."
	cd $PROJECT_NAME
	git pull
	cd ..
fi

cd $PROJECT_NAME

echo "Installing dependencies..."
pip install --upgrade pip
pip install -e .

echo "Installation complete!"
echo "You can now run 'tvault help' from the terminal."

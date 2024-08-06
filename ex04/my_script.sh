#!/bin/bash

# Script to set up virtual environment and install requirements for Django

# Constants
VENV_NAME="django_venv"
REQUIREMENTS_FILE="/sgoinfre/students/belamiqu/Djangogit/Django-1-Lib/ex04/requirement.txt"

# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing..."
    pip install virtualenv
    if [ $? -ne 0 ]; then
        echo "Failed to install virtualenv. Aborting."
        exit 1
    fi
fi

# Create virtual environment using virtualenv
echo "Creating virtual environment $VENV_NAME"
virtualenv $VENV_NAME || exit 1

# Activate virtual environment
echo "Activating virtual environment $VENV_NAME"
source $VENV_NAME/bin/activate || exit 1

# Install requirements
echo "Installing requirements from $REQUIREMENTS_FILE"
pip install -r $REQUIREMENTS_FILE || exit 1

# Deactivate virtual environment
echo "Deactivating virtual environment $VENV_NAME"
deactivate

echo "Setup completed successfully."

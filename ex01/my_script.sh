#!/usr/bin/bash

# Display pip version
pip --version

# Install path.py with force-reinstall into local_lib directory
pip install --force-reinstall --target=./local_lib git+https://github.com/jaraco/path.git > install.log 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "path.py library installed successfully."
    
    # Execute the Python program
    python3 my_program.py
else
    echo "Error installing path.py library. Check install.log for details."
fi

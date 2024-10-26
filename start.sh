#!/bin/bash
bash setup.sh
# Activate the Python virtual environment
source ./myenv/bin/activate


# Check if activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

touch ~/.Xauthority

# Install Python packages
pip install pyautogui
pip install --upgrade pillow
pip install opencv-python-headless
pip install pyperclip

# Run gofile.sh
 bash gofile.py

# Check if gofile.sh executed successfully
if [ $? -ne 0 ]; then
  echo "gofile.sh failed to execute."
  exit 1
fi

# Run github.sh
bash github.sh

# Check if github.sh executed successfully
if [ $? -ne 0 ]; then
  echo "github.sh failed to execute."
  exit 1
fi

echo "Both scripts executed successfully."

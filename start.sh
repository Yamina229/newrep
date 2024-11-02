#!/bin/bash

# Run setup and environment activation
bash setup.sh

# Activate the Python virtual environment
source ./myenv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

# Prepare environment
touch ~/.Xauthority

# Install required Python packages
pip install pyautogui
pip install --upgrade pillow
pip install opencv-python-headless
pip install pyperclip
bash gofile.sh
bash github.sh
# Repeat gofile.sh and github.sh execution 10 times
for i in {1..9}; do
  echo "Execution cycle $i for gofile.sh and github.sh"

  # Run gofile.sh
  bash gofile.sh

  # Check if gofile.sh executed successfully
  if [ $? -ne 0 ]; then
    echo "gofile.sh failed to execute on cycle $i."
    exit 1
  fi

  # Run github.sh
  bash github.sh

  # Check if github.sh executed successfully
  if [ $? -ne 0 ]; then
    echo "github.sh failed to execute on cycle $i."
    exit 1
  fi
  python navigate.py
done

echo "Completed 10 cycles of gofile.sh and github.sh."

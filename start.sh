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

# Repeat gofile.sh and github.sh execution 10 times
for i in {1..10}; do
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
done

echo "Completed 10 cycles of gofile.sh and github.sh."

# Run window.sh 5000 times
for j in {1..5000}; do
  echo "Execution cycle $j for window.sh"
  
  # Run window.sh
  bash window.sh

  # Check if window.sh executed successfully
  if [ $? -ne 0 ]; then
    echo "window.sh failed to execute on cycle $j."
    exit 1
  fi
done

echo "Completed 5000 executions of window.sh successfully."

import pyautogui
import time
import subprocess

# Step 1: Initial sleep for 2 seconds
time.sleep(2)

# Step 2: Click at (964, 45)
pyautogui.click(964, 45)

# Step 3: Sleep for 2 seconds
time.sleep(2)

# Step 4: Type the URL for the Firefox add-on
pyautogui.write("https://addons.mozilla.org/nl/firefox/addon/tab-reloader/")

# Step 5: Sleep for 1 second
time.sleep(1)

# Step 6: Press Enter
pyautogui.press("enter")

# Step 7: Sleep for 6 seconds to allow the page to load
time.sleep(6)
pyautogui.click(99, 174)
time.sleep(2)
# Step 8: Press Tab 13 times, with a 1-second delay between each press
for _ in range(8):
    pyautogui.press("tab")
    time.sleep(1)

# Step 9: Press Enter
pyautogui.press("enter")

# Step 10: Sleep for 3 seconds
time.sleep(3)

# Step 11: Click at (1276, 273)
pyautogui.click(1276, 273)

# Step 12: Sleep for 2 seconds
time.sleep(2)

# Step 13: Click at (1272, 39)
pyautogui.click(1272, 39)

# Step 14: Sleep for 2 seconds
time.sleep(2)

# Step 15: Click at (1308, 205)
pyautogui.click(1308, 205)

# Step 16: Sleep for 2 seconds
time.sleep(2)

# Step 17: Click at (1153, 42)
pyautogui.click(1153, 42)

# Step 18: Sleep for 2 seconds
time.sleep(2)

# Step 19: Click at (1306, 84)
pyautogui.click(1306, 84)

# Step 20: Sleep for 1 second
time.sleep(1)

# Step 21: Click at (1297, 178)
pyautogui.click(1297, 178)

# Step 22: Sleep for 2 seconds
time.sleep(2)

# Step 23: Press the down arrow key 6 times, with a 1-second delay between each press
for _ in range(6):
    pyautogui.press("down")
    time.sleep(1)

# Step 24: Press Enter
pyautogui.press("enter")

# Step 25: Sleep for 2 seconds to finish the initial sequence
time.sleep(2)

# Additional steps: Run reload.py and perform specified actions
# Step 26: Run reload.py
subprocess.run(["python3", "reload.py"])

# Step 27: Sleep for 2 seconds
time.sleep(2)

# Step 28: Click at (596, 37)
pyautogui.click(596, 37)

# Step 29: Sleep for 2 seconds
time.sleep(2)

# Step 30: Run reload.py again
subprocess.run(["python3", "reload.py"])

# Step 31: Sleep for 2 seconds
time.sleep(2)

# Step 32: Click at (335, 43)
pyautogui.click(335, 43)

# Step 33: Run reload.py again
subprocess.run(["python3", "reload.py"])

# Step 34: Sleep for 2 seconds
time.sleep(2)

# Step 35: Click at (144, 43)
pyautogui.click(144, 43)

# Step 36: Sleep for 2 seconds
time.sleep(2)

# Step 37: Run reload.py for the last time
subprocess.run(["python3", "reload.py"])

# Step 38: Sleep for 2 seconds to finish the script
time.sleep(2)

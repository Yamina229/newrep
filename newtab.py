import pyautogui
import time
import random

def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Step 1: Sleep for 2 seconds
time.sleep(2)

# Step 2: Click at location (515, 35)
pyautogui.click(515, 35)

# Step 3: Sleep for 2 seconds
time.sleep(2)

# Step 4: Type the URL
pyautogui.write("https://github.com/codespaces/new")

# Step 5: Sleep for 1 second
time.sleep(1)

# Step 6: Press Enter
pyautogui.press("enter")

# Step 7: Sleep for 6 seconds to allow the page to load
time.sleep(6)

for _ in range(11):
    pyautogui.press("tab")
    time.sleep(1)

# Press Enter, sleep 1 second
pyautogui.press("enter")
time.sleep(1)

# Press the down arrow key once, sleep 1 second, then press Enter
pyautogui.press("down")
time.sleep(1)
pyautogui.press("enter")
time.sleep(4)

# Press the down arrow key 3 times
for _ in range(3):
    pyautogui.press("down")
    time.sleep(1)
time.sleep(2)
click_locations_13 = [(928, 536), (950, 532), (968, 535), (990, 533), 
                      (1004, 533), (1013, 530)]
click_at(*random.choice(click_locations_13))
time.sleep(20)
# Step 11: Mouse click at (253, 40)

click_at(420, 315)
time.sleep(2)

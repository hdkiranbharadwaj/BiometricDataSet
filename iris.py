from PIL import ImageGrab
import keyboard
from datetime import datetime
import os

def take_eye_screenshot(bbox, folder_path, eye_type):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{eye_type}_{timestamp}.png"
    filepath = os.path.join(folder_path, filename)

    screenshot = ImageGrab.grab(bbox=bbox)
    screenshot.save(filepath)

    print(f"{eye_type.capitalize()} eye screenshot taken and saved as '{filename}'.")

def create_folder(name):
    folder_path = os.path.join(os.getcwd(), name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def main():
    while True:
        user_name = input("Enter your name (or 'q' to quit): ")
        if user_name.lower() == 'q':
            print("Quitting the program.")
            break

        folder_path = create_folder(user_name)

        eye_bbox = (779, 344, 1354, 661)  # Adjust the coordinates for both eyes

        print(f"Press 's' to start taking screenshots for {user_name}'s left eye. Press 'q' to quit.")

        # Wait for 's' key press to start taking screenshots for the left eye
        keyboard.wait('s')
        take_eye_screenshot(eye_bbox, folder_path, "left_eye")
        print(f"Screenshots for {user_name}'s left eye completed.")

        print(f"Press 's' to start taking screenshots for {user_name}'s right eye. Press 'q' to quit.")

        # Wait for 's' key press to start taking screenshots for the right eye
        keyboard.wait('s')
        take_eye_screenshot(eye_bbox, folder_path, "right_eye")
        print(f"Screenshots for {user_name}'s right eye completed.\n")

if __name__ == "__main__":
    main()

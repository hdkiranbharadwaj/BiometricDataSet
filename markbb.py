import pyautogui
import keyboard

def get_bounding_box():
    print("Please move the mouse to the top-left corner of the region and press 's' to start selecting.")
    keyboard.wait('s')

    start_x, start_y = pyautogui.position()
    print(f"Start Position: ({start_x}, {start_y})")

    print("Move the mouse to the bottom-right corner of the region and press 'e' to end selection.")
    keyboard.wait('e')

    end_x, end_y = pyautogui.position()
    print(f"End Position: ({end_x}, {end_y})")

    return start_x, start_y, end_x, end_y

def main():
    print("Press 'q' to quit.")

    while True:
        if keyboard.is_pressed('q'):
            print("Quitting the program.")
            break

        if keyboard.is_pressed('s'):
            bbox = get_bounding_box()
            print("Bounding Box Coordinates:", bbox)

if __name__ == "__main__":
    main()

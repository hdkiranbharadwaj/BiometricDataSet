# Fingerprint Capture Script

The Fingerprint Capture Script is designed to capture fingerprint images using a fingerprint sensor and organize them into a structured folder hierarchy. The script prompts the user for information such as user name, hand (left or right), and fingers to capture.

## Prerequisites
- Ensure that the fingerprint sensor is connected and properly configured.
- Python 3.x installed on your system.

## Usage
1. **Run the Script**
    - Open a terminal or command prompt.
    - Navigate to the script directory.
    - Execute the script using the command: `python script_name.py`

2. **User Input**
    - Enter the name of the user when prompted.
    - Simply hit Enter to capture each finger or any other key to skip.

3. **Capturing Fingerprint Data**
    - The script captures fingerprint images and organizes them into folders based on user input.
    - Images are saved in the destination folder with unique filenames.

## Script Structure

- **`move_fingerprint_image` Function:**
    - Moves the fingerprint image from the source folder to the destination folder.
    - Constructs the destination path based on user information.

- **`capture_user_data` Function:**
    - Prompts the user to enter their name.
    - Returns the entered user name.

- **`capture_hand_data` Function:**
    - Prompts the user to specify fingers for a given hand (left or right).
    - Returns the hand name and a list of selected fingers.

- **Source Folder:**
    - The folder where fingerprint images are captured by the fingerprint sensor.
    - Default: `C:\Program Files\Mantra\MFS100\Driver\MFS100Test\FingerData`

- **Destination Folder:**
    - The base folder where organized fingerprint images will be saved.
    - Default: `D:\Onedrive\Desktop\New folder`

## Configuration
- Update the `source_folder` and `destination_base_folder` variables in the script to match your system's configuration.

## Example

python fingerprint_capture.py

<br>
<br>
<br>
<br>
<hr>

# Eye Screenshot Capture Program

This Python program captures screenshots of a user's left and right eyes and stores them in a folder named after the user.

## Features

- Captures screenshots of both left and right eyes.
- Creates a folder for each user and saves the screenshots inside it.
- Uses the Pillow library for screenshot capture.
- Utilizes the keyboard library to wait for user input.

## Prerequisites

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Required Libraries**: Install the required Python libraries using the following command:

    ```bash
    pip install Pillow keyboard
    ```

## Usage

1. **Run the script:**

    ```bash
    python eye_screenshot_capture.py
    ```

2. **Enter the user's name when prompted.**

3. **Press 's' to start capturing screenshots for the left eye.**

4. **Press 's' again to start capturing screenshots for the right eye.**

5. **The screenshots are saved in a folder named after the user in the current working directory.**

6. **Repeat the process for each user.**

7. **Press 'q' to quit the program.**

## Customization

- **Adjust Bounding Box Coordinates:**
  - Open the script (`eye_screenshot_capture.py`) in a text editor.
  - Locate the `eye_bbox` variable and adjust the coordinates based on your specific requirements.


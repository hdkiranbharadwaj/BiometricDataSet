import os
import shutil

def move_fingerprint_image(source_path, destination_folder, user_name, hand, finger):
    # Check if the source file exists
    if os.path.exists(source_path):
        # Create the user's destination folder if it doesn't exist
        user_destination_folder = os.path.join(destination_folder, user_name, hand)

        if not os.path.exists(user_destination_folder):
            os.makedirs(user_destination_folder)

        # Construct the destination path with the finger number
        destination_path = os.path.join(user_destination_folder, f'{user_name}_{hand}_{finger}.bmp')

        # Copy the file to the destination
        shutil.copy2(source_path, destination_path)

        print(f'Fingerprint image moved to: {destination_path}')
    else:
        print(f'Error: Source file not found at {source_path}')

def capture_user_data():
    user_name = input("Enter the name of the user: ")
    return user_name

def capture_hand_data(hand):
    fingers = ['0', '1', '2', '3', '4']
    finger_data = []

    print(f"\nEnter the fingers for the {hand} hand:")
    for finger in fingers:
        response = input(f"Do you want to capture finger {finger}? (Press Enter for yes, any other key for no): ")
        if response == '':
            source_file = os.path.join(source_folder, 'FingerImage.bmp')
            move_fingerprint_image(source_file, destination_base_folder, user_name, hand, finger)
            finger_data.append(finger)

    return hand, finger_data

# Source folder where the fingerprint images are captured
source_folder = r'C:\Program Files\Mantra\MFS100\Driver\MFS100Test\FingerData'

# Base destination folder
destination_base_folder = r'D:\Onedrive\Desktop\New folder'

# Get user data
user_name = capture_user_data()

# Capture fingerprints for the left hand
left_hand, left_hand_fingers = capture_hand_data("L")

# Capture fingerprints for the right hand
right_hand, right_hand_fingers = capture_hand_data("R")

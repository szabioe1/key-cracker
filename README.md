# Szabioe's Cracker

## Introduction
Szabioe's Cracker is a Python program that offers users the ability to generate, store, and crack random keys or manually input keys. The program provides a user-friendly command-line interface with features like a progress bar, timing, and detailed statistics.

## Features
- **Generate and Store Keys**: Users can generate random keys of specified lengths or manually input keys of their choice. The generated keys are stored in a file named 'secret.key.'
- **Crack Stored Keys**: Users can attempt to crack the stored keys using a brute-force approach, while visualizing their progress through a progress bar.
- **Timing and Statistics**: The program measures and displays the time taken to crack a key and the total number of guesses made during the process.

## Prerequisites
- Python 3.x
- Windows operating system (for the `ctypes` library used to set the console title)

## Dependencies
- `random`: Used for generating random characters.
- `time`: Used for pausing and measuring time.
- `string`: Used for defining the character set (letters and digits).
- `ctypes`: Used for setting the console title in a Windows environment.
- `tqdm`: Used to create a progress bar to visualize the cracking progress.

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the `tqdm` library using pip:
   ```bash
   pip install tqdm
## Usage

### Menu
Upon running the program, users are presented with a menu with two options:

1. **Store**: Users can store a key either by manually inputting it or generating a random key.

2. **Crack**: Users can attempt to crack a stored key using a brute-force method while monitoring their progress with a visual progress bar.

### Storing Keys
#### Manual Key Input
- Users can manually input a key, which will be stored in the 'secret.key' file.

#### Generated Key
- Users can generate a random key of a specified length, which will also be stored in 'secret.key.'

### Cracking Keys
- The program attempts to crack the stored key character by character using a brute-force approach.
- Users can monitor the progress through a visual progress bar provided by `tqdm`.
- The program measures and displays the time taken to crack the key and the total number of guesses made.

## Visual Progress Bar
- The progress bar visually represents the cracking progress. It fills as the program successfully guesses characters from the key.
- Users can see their progress and gauge how close they are to cracking the key.

## Timing and Statistics
- The program measures the time taken to crack the key using `time.time()` and displays it in seconds.
- It also displays the total number of guesses made during the key-cracking process.

## Notes
- The program may not work as expected in non-Windows environments due to the use of `ctypes` to set the console title.
- You can adjust the timing mechanism in the code (e.g., `time.sleep`) to control the speed of the brute-force cracking.

## Author
- Szabioe

## Version
- 2.0 (Enhanced with progress bar and timing features)

## License
- This code is provided under an open-source license. You are free to use, modify, and distribute it as per the terms of the license.

## Disclaimer
- This program is intended for educational purposes and should not be used for any malicious activities.

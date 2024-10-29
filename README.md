# Automated Data Entry Bot for Desktop Application

This Python script fetches posts from the JSONPlaceholder API, saves them as individual text files on the desktop, and utilizes Notepad for the file creation process. The bot automatically manages directory creation, file saving, and cleanup.

## Features

- Fetches up to 10 posts from the JSONPlaceholder API.
- Creates a dedicated directory on the desktop to store the text files.
- Launches Notepad to type and save each post's title and body.
- Closes Notepad after saving all posts.

## Requirements

To run this script, you'll need:

- Python 3.x
- The following Python packages:
  - `pyautogui` (for automating keyboard input)
  - `requests` (for making HTTP requests)

You can install the required packages using pip:

```bash
pip install pyautogui requests
```

## Usage

1. Clone or download the repository.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script:

```bash
python your_script_name.py
```

Replace `your_script_name.py` with the name of your Python file.

## Script Overview

### Main Functionality

- The script defines a main function that orchestrates the fetching of posts, directory creation, and the launching of Notepad.
- It fetches the first 10 posts from the JSONPlaceholder API using the `fetch_posts` function.
- It creates a directory named `tjm-project` on the desktop to store the text files.
- It uses the `pyautogui` library to type the fetched post data into Notepad and save it to individual text files.
- Notepad is automatically closed after all posts are saved.

### Functions

- `main()`: The main function that coordinates the workflow of the script.
- `fetch_posts(post_limit)`: Fetches posts from the JSONPlaceholder API and returns a list of post data.
- `save_posts(data, folder_path)`: Saves the fetched post data into individual text files in the specified directory.

## Notes

- Ensure Notepad is installed on your system. The script relies on Notepad for file creation.
- The script is designed to run on Windows due to the use of Notepad and specific file path structures.

## Troubleshooting

- If you encounter issues launching Notepad, please ensure it is correctly installed and accessible from the command line.
- If the script fails to fetch posts, check your internet connection or the API status.

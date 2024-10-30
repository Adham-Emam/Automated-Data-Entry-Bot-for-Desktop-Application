import os
import pyautogui
import subprocess
import time
import requests


def main():
    """The main function of the script.

    This function calls other functions in the correct order to fetch posts from the
    JSONPlaceholder API, create a new directory on the desktop, launch Notepad,
    save the posts to individual text files in the directory, and then close Notepad.

    Returns:
        None
    """
    post_limit = 10
    data = fetch_posts(post_limit)

    # Define the directory for saving the files
    folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "tjm-project")

    # Ensure tjm-project directory exists
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Directory {folder_path} created.")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # Launch Notepad
    try:
        # Launch Notepad and keep its process handle
        notepad_process = subprocess.Popen(["notepad"])

        # Wait for the Notepad window to appear
        time.sleep(2)
    except FileNotFoundError:
        print("Notepad not found. Please install it and try again.")
    except Exception as e:
        print(f"Error launching Notepad: {e}")
        return

    save_posts(data, folder_path)

    # Close Notepad if it was opened
    if notepad_process:
        try:
            notepad_process.terminate()
            print("Notepad closed successfully.")
        except Exception as e:
            print(f"Error closing Notepad: {e}")


def fetch_posts(post_limit=10):
    """Fetches the first 10 posts from the JSONPlaceholder API.

    Returns:
        list: A list of dictionaries containing the posts' data.
    """
    try:
        url = "https://jsonplaceholder.typicode.com/posts/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data[:post_limit]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []


def save_posts(data, folder_path):
    """
    Saves post data to individual text files in the specified folder path.

    Args:
        data (list): A list of dictionaries containing post data.
        folder_path (str): The path to the folder where the files will be saved.
    """
    if data:
        for post in data:
            # Construct the file name and file path
            file_name = f"{post['id']}.txt"
            file_path = os.path.join(folder_path, file_name)

            # Type the post title and body into Notepad
            pyautogui.typewrite(f"Title:\n{post['title']}\n\nBody:\n{post["body"]}")

            # Remove the file if it already exists
            if os.path.exists(file_path):
                # Remove the existing file if it already exists
                os.remove(file_path)
            time.sleep(1)

            # Save the contents in Notepad
            pyautogui.hotkey("shift", "ctrl", "s")
            # Wait for the Save As dialog box to appear
            time.sleep(1)

            # Type the file path and save the file
            pyautogui.typewrite(file_path)
            pyautogui.hotkey("enter")

            # Wait for the file to be saved
            time.sleep(1)

            # Clear Notepad for the next post
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("del")
            print(f"Post {post['id']} saved to {file_name}.")

        print("Posts saved successfully!")
    else:
        print("No posts found.")


if __name__ == "__main__":
    main()

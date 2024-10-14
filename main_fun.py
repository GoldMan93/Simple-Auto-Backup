import shutil
import os
from datetime import datetime

# A global variable to store the counter (reset when the app is restarted)
copy_counter = 0

def create_unique_folder(destination):
    """
    Create a unique folder based on the current date (year-month-day) and a counter.
    The folder will be created under the destination directory.
    """
    global copy_counter
    current_date = datetime.now().strftime("%Y-%b-%d")  # E.g., 2024-Oct-14
    copy_counter += 1  # Increment the counter for each copy
    folder_name = f"{current_date}_{copy_counter}"
    folder_path = os.path.join(destination, folder_name)

    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def copy_single_file(source, destination, file_name):
    """
    Copy a specific file from source to a date-based folder in destination.
    """
    folder_path = create_unique_folder(destination)
    src_file = os.path.join(source, file_name)
    dest_file = os.path.join(folder_path, file_name)
    
    if not os.path.exists(src_file):
        raise FileNotFoundError(f"File '{file_name}' not found in source directory.")

    shutil.copy(src_file, dest_file)
    print(f"Successfully copied {file_name} to {folder_path}")

def copy_all_files(source, destination):
    """
    Copy all files from source to date-based folders in destination.
    """
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source directory '{source}' not found.")
    
    if not os.path.exists(destination):
        os.makedirs(destination)  # Create destination folder if it doesn't exist

    for file_name in os.listdir(source):
        src_path = os.path.join(source, file_name)
        
        if os.path.isfile(src_path):
            folder_path = create_unique_folder(destination)
            dest_path = os.path.join(folder_path, file_name)
            
            shutil.copy(src_path, dest_path)
            print(f"Successfully copied {file_name} to {folder_path}")

def copy_files(source, destination, file_name=None, copy_specific_file=False):
    """
    Copy files from source to destination. Copy all files or a specific file based on parameters.
    """
    if copy_specific_file and file_name:
        copy_single_file(source, destination, file_name)
    elif not copy_specific_file:
        copy_all_files(source, destination)
    else:
        raise ValueError("Invalid input: Either 'file_name' must be specified or 'copy_specific_file' must be True.")

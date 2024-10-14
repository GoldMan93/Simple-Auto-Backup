import shutil
import os

def copy_single_file(source, destination, file_name):
    """
    Copy a specific file from source to destination.
    """
    src_file = os.path.join(source, file_name)
    dest_file = os.path.join(destination, file_name)
    
    if not os.path.exists(src_file):
        raise FileNotFoundError(f"File '{file_name}' not found in source directory.")

    shutil.copy(src_file, dest_file)
    print(f"Successfully copied {file_name} to {destination}")


def copy_all_files(source, destination):
    """
    Copy all files from source to destination.
    """
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source directory '{source}' not found.")
    
    if not os.path.exists(destination):
        os.makedirs(destination)  # Create destination folder if it doesn't exist

    for file_name in os.listdir(source):
        src_path = os.path.join(source, file_name)
        dest_path = os.path.join(destination, file_name)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Successfully copied {file_name} to {destination}")

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


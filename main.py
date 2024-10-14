import shutil
import os

def move_file(source_path, destination_folder):
    # Check if source file exists
    if not os.path.exists(source_path):
        print(f"The file {source_path} does not exist.")
        return
    
    # Make sure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Get the file name
    file_name = os.path.basename(source_path)
    
    # Construct the destination path
    destination_path = os.path.join(destination_folder, file_name)
    
    # Move the file
    shutil.copy(source_path, destination_path)
    print(f"Moved {file_name} to {destination_folder}")

# Example usage
source_file = "test/test.test"
destination = "test2/"

move_file(source_file, destination)

import shutil
import os

def copy_files(source_folder, destination_folder, file_name=None, copy_specific_file=False):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"The source folder {source_folder} does not exist.")
        return
    
    # Make sure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # If copying a specific file
    if copy_specific_file and file_name:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        
        # Check if the specific file exists
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"Copied {file_name} to {destination_folder}")
        else:
            print(f"The file {file_name} does not exist in {source_folder}.")
    
    # If copying all files
    elif not copy_specific_file:
        for file_name in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
                print(f"Copied {file_name} to {destination_folder}")

# Example usage
source_folder = "C:/path/to/source/folder"
destination_folder = "C:/path/to/destination/folder"
specific_file_name = "file.txt"  # Specify the file name if needed


# To copy a specific file, set copy_specific_file to True
copy_files(source_folder, destination_folder, file_name=specific_file_name, copy_specific_file=True)

# To copy all files, set copy_specific_file to False
# copy_files(source_folder, destination_folder, copy_specific_file=False)

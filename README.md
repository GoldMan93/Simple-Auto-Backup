Here is the `README.md` content in markdown format:

````markdown
# File Transfer Application

This Python-based application enables users to copy files from a source directory to a destination directory. The application supports both copying all files and copying specific files. Additionally, users can set an interval for copying files and track progress through a progress bar and log of transferred files. The application creates folders based on the current date, and each new copy operation increments a counter in the folder name.

## Features:

- Copy all files or specific files based on user preference.
- Create new folders with a date-based naming convention (`YYYY_Mon_DD_n`).
- Set a time interval for copying files.
- View the progress of file transfers using a progress bar.
- Track the log of all transferred files.
- Start and stop the file copying process.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `tkinter`
  - `shutil`

If `tkinter` is not already installed, you can install it using your package manager.

For example, on Ubuntu:

```bash
sudo apt-get install python3-tk
```
````

## Files

- **`main_fun.py`**: Contains the logic for copying files from the source folder to the destination folder.
- **`ui.py`**: Contains the graphical user interface (GUI) built using `tkinter`.

## How to Run

1. Clone or download this repository.

```bash
git clone <repository_url>
```

2. Navigate to the project directory.

```bash
cd <project_directory>
```

3. Run the `ui.py` script to open the application.

```bash
python ui.py
```

## How to Use the Application

1. **Set Source Folder**:

   - Click the "Browse" button next to the **Source Folder** input field to select the source directory from where the files will be copied.

2. **Set Destination Folder**:

   - Click the "Browse" button next to the **Destination Folder** input field to select the destination directory where files will be copied.

3. **Select Copy Option**:

   - If you want to copy a specific file, check the **Copy specific file** checkbox and enter the file name in the **File Name** field.
   - If you want to copy all files in the source folder, leave the **Copy specific file** checkbox unchecked.

4. **Set Interval**:

   - Enter the time interval (in seconds) between each copy operation in the **Time between copies (seconds)** field.

5. **Start Copying**:

   - Press the **Start** button to begin copying files. The application will automatically copy files at the specified interval (or all files, depending on your selection).
   - Once copying starts, the button text will change to **Stop**. Press **Stop** to halt the copying process at any time.

6. **Progress and Log**:
   - A progress bar will show the current status of the file copying process.
   - A log of transferred files will be displayed below the progress bar.

## Folder Naming Convention

The application organizes copied files into folders based on the current date with an incremental counter. For example:

- `2024_Oct_14_1`
- `2024_Oct_14_2`
- `2024_Oct_14_3`

Each time files are copied, a new folder is created with the next incremental counter for the same day.

## License

This project is open-source. You can freely use and modify it for personal or educational purposes.

```

Just copy and paste this markdown into your `README.md` file.
```

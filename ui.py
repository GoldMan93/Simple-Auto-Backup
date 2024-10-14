import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading
import time
from main_fun import copy_files  # Import the copy function from main_fun.py

class FileTransferUI:
    import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading
import time
from main_fun import copy_files  # Import the copy function from main_fun.py

class FileTransferUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Transfer")
        self.is_running = False  # Track the state of the copying process
        self.copy_interval = tk.IntVar(value=5)  # Default to 5 seconds
        self.countdown = 0  # For showing the countdown
        self.copy_thread = None  # Thread to handle the copying process
        self.copy_specific_file = tk.BooleanVar()  # Variable to control specific file copying
        self.copy_counter = 0  # A counter to track number of copies
        self.last_folder = ""  # To track the last folder created

        # Labels and buttons
        tk.Label(root, text="Source Folder:").grid(row=0, column=0, sticky="w")
        self.source_entry = tk.Entry(root, width=40)
        self.source_entry.grid(row=0, column=1, sticky="ew")
        tk.Button(root, text="Browse", command=self.browse_source).grid(row=0, column=2)

        tk.Label(root, text="Destination Folder:").grid(row=1, column=0, sticky="w")
        self.destination_entry = tk.Entry(root, width=40)
        self.destination_entry.grid(row=1, column=1, sticky="ew")
        tk.Button(root, text="Browse", command=self.browse_destination).grid(row=1, column=2)

        tk.Checkbutton(root, text="Copy specific file", variable=self.copy_specific_file).grid(row=2, column=0, sticky="w")

        tk.Label(root, text="File Name:").grid(row=3, column=0, sticky="w")
        self.file_name_entry = tk.Entry(root, width=40)
        self.file_name_entry.grid(row=3, column=1, sticky="ew")

        # Interval setting
        tk.Label(root, text="Time between copies (seconds):").grid(row=4, column=0, sticky="w")
        self.interval_entry = tk.Entry(root, textvariable=self.copy_interval, width=5)
        self.interval_entry.grid(row=4, column=1, sticky="w")

        # Buttons in the same row
        self.copy_button = tk.Button(root, text="Copy", command=self.copy_files)
        self.copy_button.grid(row=5, column=1, sticky="e")
        self.start_button = tk.Button(root, text="Start", command=self.toggle_copying)
        self.start_button.grid(row=5, column=2)

        # Combined success message and countdown label
        self.status_label = tk.Label(root, text="", bg="white", anchor="w")
        self.status_label.grid(row=6, column=0, columnspan=3, sticky="ew")

        # Log of transferred files
        self.log_text = tk.Text(root, width=60, height=10, state=tk.DISABLED)
        self.log_text.grid(row=7, column=0, columnspan=3, sticky="ew")

        # Progress bar for copying files
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
        self.progress_bar.grid(row=8, column=0, columnspan=3, pady=5)

        # Configure column resizing behavior
        root.grid_columnconfigure(1, weight=1)

    def browse_source(self):
        folder_selected = filedialog.askdirectory()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, folder_selected)

    def browse_destination(self):
        folder_selected = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, folder_selected)

    def copy_files(self):
        """
        Perform the file copy operation.
        """
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        file_name = self.file_name_entry.get() if self.copy_specific_file.get() else None

        if not source or not destination:
            self.update_status("Please specify both source and destination folders.", "red")
            return

        # Start the progress bar
        self.progress_bar.start()

        # Simulate copying process (replace this with your actual file copying logic)
        try:
            self.last_folder = copy_files(source, destination, file_name=file_name, copy_specific_file=self.copy_specific_file.get())
            
            # After copying, update the log
            self.log_text.config(state=tk.NORMAL)  # Enable editing
            log_message = f"Copied files to folder {self.last_folder}."
            self.log_text.insert(tk.END, log_message + "\n")
            self.log_text.config(state=tk.DISABLED)  # Disable editing

            # Stop the progress bar once copying is complete
            self.progress_bar.stop()

            # Update the UI with the success message
            self.update_status("File(s) copied successfully!", "green")

        except Exception as e:
            self.update_status(f"Error: {str(e)}", "red")
            self.progress_bar.stop()

    def update_status(self, message, color):
        """Update the status label with a message and background color."""
        self.status_label.config(text=message, bg=color)

    def toggle_copying(self):
        """
        Toggle the copying process. Start copying when 'Start' is pressed, and stop when 'Stop' is pressed.
        """
        source = self.source_entry.get()
        destination = self.destination_entry.get()

        # Check if source or destination is empty and show an error if so
        if not source or not destination:
            self.update_status("Please specify both source and destination folders.", "red")
            return

        if not self.is_running:  # If not running, start the copy process
            self.is_running = True
            self.start_button.config(text="Stop")  # Change button text to "Stop"

            # Start the copying thread
            self.copy_thread = threading.Thread(target=self.start_copying)
            self.copy_thread.daemon = True  # Daemon thread to exit when the app closes
            self.copy_thread.start()

        else:  # If running, stop it
            self.is_running = False
            self.start_button.config(text="Start")  # Change button text back to "Start"

            # Stop the thread after setting the flag
            if self.copy_thread:
                self.copy_thread.join()  # Ensure


    def start_copying(self):
        """
        Start the copying process in a loop, copying files every X seconds.
        """
        while self.is_running:
            self.copy_files()  # Perform the copy operation
            time.sleep(self.copy_interval.get())  # Sleep for the specified interval (in seconds)


# Run the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = FileTransferUI(root)
    root.mainloop()

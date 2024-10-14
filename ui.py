import tkinter as tk
from tkinter import filedialog
import threading
import time
from main_fun import copy_files  # Import the copy function from your file_copy.py


class FileTransferUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Transfer")
        self.is_running = False  # Track the state of the copying process
        self.copy_interval = tk.IntVar(value=5)  # Default to 5 seconds
        self.countdown = 0  # For showing the countdown

        # Variable to control specific file copying
        self.copy_specific_file = tk.BooleanVar()

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

        # Success message and countdown
        self.status_label = tk.Label(root, text="", bg="white", anchor="w")
        self.status_label.grid(row=6, column=0, sticky="ew")

        self.countdown_label = tk.Label(root, text="", bg="white", anchor="w")
        self.countdown_label.grid(row=6, column=2, sticky="e")

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
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        file_name = self.file_name_entry.get() if self.copy_specific_file.get() else None

        if not source or not destination:
            self.update_status("Please specify both source and destination folders.", "red")
            return

        copy_files(source, destination, file_name=file_name, copy_specific_file=self.copy_specific_file.get())
        self.update_status("File(s) copied successfully!", "green")

    def update_status(self, message, color):
        """Update the status label with a message and background color."""
        self.status_label.config(text=message, bg=color)

    def start_copying(self):
        while self.is_running:
            self.copy_files()
            self.countdown = self.copy_interval.get()
            self.update_countdown()
            for _ in range(self.copy_interval.get()):
                if not self.is_running:
                    return  # If stopped, exit
                time.sleep(1)
                self.countdown -= 1
                self.update_countdown()

    def update_countdown(self):
        """Update the countdown label with the remaining time for the next copy."""
        if self.countdown > 0:
            self.countdown_label.config(text=f"Next copy in {self.countdown} sec")
        else:
            self.countdown_label.config(text="")

    def toggle_copying(self):
        if not self.is_running:
            # Start the copying process
            self.is_running = True
            self.start_button.config(text="Stop")
            threading.Thread(target=self.start_copying, daemon=True).start()
        else:
            # Stop the copying process
            self.is_running = False
            self.start_button.config(text="Start")


# Run the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = FileTransferUI(root)
    root.mainloop()

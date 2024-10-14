import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
from main_fun import copy_files  # Import the copy function from your file_copy.py

class FileTransferUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Transfer")
        
        # Variable to control specific file copying
        self.copy_specific_file = tk.BooleanVar()
        self.is_running = False  # Track the state of the copying process
        
        # Labels and buttons
        tk.Label(root, text="Source Folder:").grid(row=0, column=0)
        self.source_entry = tk.Entry(root, width=40)
        self.source_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.browse_source).grid(row=0, column=2)
        
        tk.Label(root, text="Destination Folder:").grid(row=1, column=0)
        self.destination_entry = tk.Entry(root, width=40)
        self.destination_entry.grid(row=1, column=1)
        tk.Button(root, text="Browse", command=self.browse_destination).grid(row=1, column=2)
        
        tk.Checkbutton(root, text="Copy specific file", variable=self.copy_specific_file).grid(row=2, column=0)
        
        tk.Label(root, text="File Name:").grid(row=3, column=0)
        self.file_name_entry = tk.Entry(root, width=40)
        self.file_name_entry.grid(row=3, column=1)
        
        # Buttons for one-time copy and start/stop continuous copy
        tk.Button(root, text="Copy", command=self.copy_files).grid(row=4, column=1)
        self.start_button = tk.Button(root, text="Start", command=self.toggle_copying)
        self.start_button.grid(row=5, column=1)

    def browse_source(self):
        folder_selected = filedialog.askdirectory()
        self.source_entry.insert(0, folder_selected)

    def browse_destination(self):
        folder_selected = filedialog.askdirectory()
        self.destination_entry.insert(0, folder_selected)

    def copy_files(self):
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        file_name = self.file_name_entry.get() if self.copy_specific_file.get() else None
        
        if not source or not destination:
            messagebox.showwarning("Input Error", "Please specify both source and destination folders.")
            return
        
        copy_files(source, destination, file_name=file_name, copy_specific_file=self.copy_specific_file.get())
        messagebox.showinfo("Success", "File(s) copied successfully!")
    
    def start_copying(self):
        while self.is_running:
            self.copy_files()
            time.sleep(5)  # Pause for 5 seconds between copies

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

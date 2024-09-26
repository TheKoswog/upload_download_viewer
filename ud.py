import tkinter as tk
from tkinter import Label
import psutil
import time

class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Speed Monitor")
        self.root.geometry("300x150")

        # Labels for download and upload speed
        self.download_label = Label(root, text="Download: 0 KB/s", font=("Helvetica", 14))
        self.download_label.pack(pady=10)

        self.upload_label = Label(root, text="Upload: 0 KB/s", font=("Helvetica", 14))
        self.upload_label.pack(pady=10)

        self.update_speed()

    def update_speed(self):
        # Get network stats
        net_io = psutil.net_io_counters()

        # Store previous stats
        self.last_bytes_sent = getattr(self, 'last_bytes_sent', net_io.bytes_sent)
        self.last_bytes_recv = getattr(self, 'last_bytes_recv', net_io.bytes_recv)

        # Calculate download and upload speed
        download_speed = (net_io.bytes_recv - self.last_bytes_recv) / 1024  # Convert to KB
        upload_speed = (net_io.bytes_sent - self.last_bytes_sent) / 1024    # Convert to KB

        # Update last recorded bytes
        self.last_bytes_recv = net_io.bytes_recv
        self.last_bytes_sent = net_io.bytes_sent

        # Update the labels
        self.download_label.config(text=f"Download: {download_speed:.2f} KB/s")
        self.upload_label.config(text=f"Upload: {upload_speed:.2f} KB/s")

        # Update every second
        self.root.after(1000, self.update_speed)

# Create the main window and start the app
root = tk.Tk()
app = NetworkMonitorApp(root)
root.mainloop()

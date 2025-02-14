import os
import cv2
import pyautogui
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
from datetime import datetime

# Ensure directories exist
SCREENSHOT_DIR = "./Screenshots"
RECORDING_DIR = "./Recordings"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(RECORDING_DIR, exist_ok=True)

# Global variables
recording = False
video_writer = None

# Function to generate a unique filename


def get_unique_filename(directory, base_name, extension):
    count = 1
    filename = os.path.join(directory, f"{base_name}{extension}")
    while os.path.exists(filename):
        filename = os.path.join(directory, f"{base_name}_{count}{extension}")
        count += 1
    return filename

# Function to take a screenshot


def take_screenshot():
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = get_unique_filename(
        SCREENSHOT_DIR, f"screenshot_{timestamp}", ".png")
    screenshot.save(filename)
    messagebox.showinfo("Screenshot Captured", f"Saved at: {filename}")

# Function to start screen recording


def start_recording():
    global recording, video_writer
    if recording:
        return
    recording = True

    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = get_unique_filename(
        RECORDING_DIR, f"recording_{timestamp}", ".avi")
    video_writer = cv2.VideoWriter(filename, fourcc, 10.0, screen_size)

def record():
    global video_writer
    while recording:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # ✅ Fixed conversion
        video_writer.write(frame)
        time.sleep(0.1)  # Reduce CPU usage
    video_writer.release()
    messagebox.showinfo("Recording Saved", f"Saved at: {filename}")


    threading.Thread(target=record, daemon=True).start()

# Function to stop screen recording


def stop_recording():
    global recording
    if recording:
        recording = False

# Function to exit the application safely


def exit_app():
    if recording:
        stop_recording()
    root.destroy()


# GUI Setup
root = tk.Tk()
root.title("Screen Recorder & Screenshot Tool")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# UI Elements
title_label = tk.Label(root, text="Screen Capture & Recorder", font=(
    "Arial", 14, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

screenshot_button = tk.Button(root, text="Take Screenshot", font=("Arial", 12), bg="#27AE60", fg="white",
                              command=take_screenshot)
screenshot_button.pack(pady=10, ipadx=10, ipady=5)

record_button = tk.Button(root, text="Start Recording", font=("Arial", 12), bg="#2980B9", fg="white",
                          command=start_recording)
record_button.pack(pady=10, ipadx=10, ipady=5)

stop_button = tk.Button(root, text="Stop Recording", font=("Arial", 12), bg="#E74C3C", fg="white",
                        command=stop_recording)
stop_button.pack(pady=10, ipadx=10, ipady=5)

exit_button = tk.Button(root, text="Exit", font=(
    "Arial", 12), bg="#BDC3C7", fg="black", command=exit_app)
exit_button.pack(pady=10, ipadx=10, ipady=5)

root.protocol("WM_DELETE_WINDOW", exit_app)  # Handle safe exit
root.mainloop()

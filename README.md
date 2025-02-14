# Screen Capture & Recorder

## Overview
Screen Capture & Recorder is a simple GUI-based Python application that allows users to:
- Take screenshots and save them with unique filenames.
- Record their screen and save recordings without overwriting previous files.
- Select a custom folder for saving files.
- Stop and start recordings smoothly.
- Exit the application safely.

## Features
- **GUI-based**: Easy-to-use interface built with Tkinter.
- **Screenshot Capture**: Saves images with unique filenames.
- **Screen Recording**: Records screen and saves videos in `.avi` format.
- **Custom Save Location**: Users can select a directory for saving files.
- **Error Handling**: Ensures stability and prevents crashes.

## Requirements
Make sure you have the following dependencies installed before running the script:

```bash
pip install opencv-python numpy pyautogui
```

## Usage
1. Run the script:
   ```bash
   python screen_recorder.py
   ```
2. Click **Take Screenshot** to capture and save a screenshot.
3. Click **Start Recording** to begin screen recording.
4. Click **Stop Recording** to stop and save the recording.
5. Click **Choose Save Folder** to select where to store files.
6. Click **Exit** to close the application safely.

## File Naming
- Screenshots are saved as `screenshot_YYYYMMDD_HHMMSS.png`
- Recordings are saved as `screen_record_YYYYMMDD_HHMMSS.avi`
- If a file with the same timestamp exists, a number is appended to keep it unique.

## Folder Structure
By default, all files are saved in:
```
~/Videos/ScreenRecorder/
```
Users can change the save location using the **Choose Save Folder** button.

## Compatibility
- **OS**: Works on Windows, macOS, and Linux.
- **Python Version**: Compatible with Python 3.x

## Future Enhancements
- Option to record audio along with video.
- Adjustable frame rate for recording.
- Support for different video formats (MP4, MKV, etc.).

## License
This project is open-source and available under the MIT License.

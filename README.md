# Gesture Volume Control Using OpenCV and MediaPipe

This project implements a gesture-based volume control system using OpenCV, MediaPipe, and PyCaw. The application captures hand gestures using a webcam and controls the system volume by tracking the distance between the thumb and index finger. 

## Features
- Real-time hand gesture recognition using OpenCV and MediaPipe.
- Adjusts system volume based on the distance between the thumb and index finger.
- Smooth interaction using Python's PyCaw library to control audio levels.
- Visual feedback of gestures on the screen with OpenCV.

# Demo

[Click here to download and watch the demo video](https://github.com/NimeshWijesuriya/Gesture-Volume-Control-CV/blob/main/Demo/Demo.mp4)

## Installation

### Prerequisites
- Python
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- PyCaw (`pycaw`)
- Numpy (`numpy`)
- comtypes (`comtypes`)

### OpenCV
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It provides a common infrastructure for computer vision applications, helping developers build efficient computer vision software. In this project, OpenCV is used for:
- Capturing video from the webcam.
- Displaying the video feed with hand gesture visualizations.
- Drawing landmarks such as the thumb, index finger, and center point between them.

Learn more about OpenCV [here](https://opencv.org/).

### MediaPipe
MediaPipe is a cross-platform framework developed by Google that facilitates building multimodal (e.g., video, audio, or time-series data) machine learning pipelines. It supports real-time hand tracking by detecting 21 key landmarks on each hand. In this project, MediaPipe is used for:
- Detecting and tracking hand landmarks.
- Extracting the positions of the thumb and index finger tips.
- Providing the key points necessary for gesture recognition.

Learn more about MediaPipe [here](https://mediapipe.dev/).

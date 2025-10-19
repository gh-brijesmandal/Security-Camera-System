# 🧠 Security Camera System (OpenCV)

This Python script uses OpenCV Haar Cascade Classifiers to detect faces and bodies in real-time through a webcam.
When a person is detected, it automatically starts recording video and stops after 5 seconds of inactivity.

# 🚀 Features

Real-time face & body detection

Automatic recording trigger

Timestamped video filenames

Simple and efficient OpenCV implementation

# 🧰 Requirements
pip install opencv-python

# Usage
Clone the repo using git clone Link.
Run main.py
Press 'q' to quit.
Recorded videos are saved in the same file as working directory.

# ⚙️ How It Works

Uses haarcascade_frontalface_default.xml and haarcascade_fullbody.xml for detection.
Starts video recording when a face/body appears.
Stops after 5 seconds of no detection.

# Downsides
Haar Cascade Classifier is CPU heavy and may not work well in low light environments. 


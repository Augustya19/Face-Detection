
# Face Detection System using OpenCV

## 📌 Overview

This project is a simple and efficient face detection system built using **Python** and **OpenCV**. It uses Haar Cascade Classifiers to identify human faces in static images and real-time video streams. The model is trained to detect frontal faces and can be used as a base for more complex facial recognition or tracking systems.

## 🎯 Features

- Real-time face detection via webcam
- Static image detection support
- Image preprocessing (grayscale conversion, resizing, filtering)
- Lightweight and fast execution
- Easy to customize or extend

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- NumPy

## 🧠 How It Works

1. Load the Haar cascade XML classifier provided by OpenCV.
2. Convert the input image (or video frame) to grayscale.
3. Apply the classifier to detect faces in the frame.
4. Draw bounding boxes around the detected faces.


## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenCV

### Installation

git clone https://github.com/Augustya19/Face-Detection.git
cd Face-Detection
pip install opencv-python

### Run with Image
python face_detect_image.py

### Run with Webcam
python face_detect_video.py


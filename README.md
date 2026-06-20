# YOLO Vision AI Detector

A web-based AI object detection application built using Python, Flask, and YOLOv8.

## Project Overview

This application allows users to upload an image and perform AI-based object detection using the YOLOv8 deep learning model.

The system identifies objects inside the image, draws bounding boxes around detected objects, and displays the number of detected instances.

---

## Features

* Upload image through web interface
* Detect multiple objects using YOLOv8
* Bounding box visualization
* Display original image and processed image
* Count detected objects automatically
* Professional frontend UI built using HTML and CSS

---

## Tech Stack

* Python
* Flask
* YOLOv8 (Ultralytics)
* HTML
* CSS
* Git
* GitHub

---

## How It Works

1. User uploads image
2. Flask backend receives image
3. YOLOv8 model performs object detection
4. Bounding boxes generated
5. Detected object counts calculated
6. Results displayed on frontend

---

## Challenges Faced

* Flask template rendering issues
* Static file handling
* Managing uploaded images
* Cloud deployment memory limitations on free hosting platforms

---

## Future Improvements

* Webcam object detection
* Video object detection
* Custom trained models
* Real-time detection pipeline

---

## Project Demo

Runs successfully on local machine.

Cloud deployment attempted on Render and Railway but exceeded free-tier memory limits because of PyTorch + YOLO inference requirements.

---

Built as an AI + Computer Vision  project.

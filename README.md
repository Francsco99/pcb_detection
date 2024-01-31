# YOLO Image Detection with Flask

A simple web application for object detection using YOLO (You Only Look Once) and Flask.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gallery](#gallery)
- [License](#license)

## Introduction

This project aims to demonstrate object detection using the YOLO model and provide a web interface for users to upload images and view the results of the detection.

YOLO (You Only Look Once) is a popular real-time object detection system that can detect multiple objects in images and videos.

## Features

- Upload an image for object detection.
- View the detected objects in the uploaded image.
- Save the processed image to a gallery.
- View a gallery of processed images.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Francsco99/pcb_detection.git
```
2. Navigate to the project directory:

```bash
cd yolo-image-detection
```

3. Create a virtual environment (reccomended)

```bash
python -m venv venv
```
4. Activate the virtual environment

On Windows:
```bash
venv\Scripts\activate
```
On Linux/MacOS:
```bash
source venv/bin/activate
```
5. Install the required dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Start the Flask application
```bash
python app.py
```
3. Open a web browser and go to http://localhost:5000 to access the upload page.
5. Upload an image for object detection and view the results.
## Gallery
You can view processed images in the gallery by visiting the `/gallery` route.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

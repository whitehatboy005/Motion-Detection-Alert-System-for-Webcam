# Motion Detection Alert System with OpenCV and Telegram Bot API
This Python script detects motion in a specified region of interest (ROI) from a webcam feed using OpenCV. When motion is detected, it captures a frame and sends an alert with a photo via the Telegram Bot API to a specified chat ID. This system is useful for security applications where immediate alerts are needed upon unauthorized motion detection.

## Features
- **Motion Detection**: Monitors a defined ROI for changes using background subtraction with OpenCV.
- **Alert Notification**: Sends a photo alert to a Telegram chat using the Telegram Bot API upon detecting motion.
- **Adjustable Parameters**: Allows customization of ROI coordinates, background subtraction method, minimum contour area, and alert interval.
- **Real-time Feedback**: Displays the video feed with overlaid ROI and detected contours for visual monitoring.
- **Error Handling**: Catches exceptions during photo capture and alert sending to ensure robust operation.
#  
## CCTV Motion Detection Repository
- **Check on this repository** https://github.com/whitehatboy005/Motion-Detection-Alert-System-for-CCTV

## Your webcam point of view

![Screenshot 2024-07-11 163540](https://github.com/whitehatboy005/Security-Alert/assets/147156726/06fda370-fdca-4472-b147-016612d8b60a)
#
## Your Telegram bot Alert

![Screenshot 2024-07-11 163715](https://github.com/whitehatboy005/Security-Alert/assets/147156726/e24a1980-2c63-4490-8ed1-e8b07936aac0)


## Installation
## Clone the Repository
```bash
git clone https://github.com/whitehatboy005/Motion-Detection-Alert-System-for-Webcam
```
## Move the file
```bash
cd Motion-Detection-Alert-System-for-Webcam
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Config Your Details
```bash
notepad config.env
```
## Run the Program
```bash
python alert.py
```

## Instructions

To get Chat ID visit [@GetMyChatID_Bot](https://t.me/GetMyChatID_Bot) Now you will copy the chat Id and config it.

To access the bot [@SecurityAlertBot](https://t.me/ProjectResultBot) and START it.

## License

This project is licensed under the terms of the [MIT license](LICENSE.md).

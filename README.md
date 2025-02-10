# 📸 Motion Detection Alert System with OpenCV and Telegram Bot API
[![License](https://img.shields.io/github/license/whitehatboy005/Motion-Detection-Alert-System-for-Webcam)](LICENSE.md)

This Python script detects motion in a specified region of interest (ROI) from a webcam feed using OpenCV. When motion is detected, it captures a frame and sends an alert with a photo via the Telegram Bot API to a specified chat ID. This system is useful for security applications where immediate alerts are needed upon unauthorized motion detection.

## 🚀 Features
- **Motion Detection**: Monitors a defined ROI for changes using background subtraction with OpenCV.
- **Alert Notification**: Sends a photo alert to a Telegram chat using the Telegram Bot API upon detecting motion.
- **Adjustable Parameters**: Allows customization of ROI coordinates, background subtraction method, minimum contour area, and alert interval.
- **Real-time Feedback**: Displays the video feed with overlaid ROI and detected contours for visual monitoring.
- **Error Handling**: Catches exceptions during photo capture and alert sending to ensure robust operation.
#  

## Your webcam point of view

![Screenshot 2024-07-11 163540](https://github.com/whitehatboy005/Security-Alert/assets/147156726/06fda370-fdca-4472-b147-016612d8b60a)
#
## Your Telegram bot Alert

![Screenshot 2024-11-03 183753](https://github.com/user-attachments/assets/c3d2c660-e9bf-4f02-82e1-1c14a8ad84e0)

#
## 📌 Instructions

To get Chat ID visit [@GetMyChatID_Bot](https://t.me/GetMyChatID_Bot) Now you will copy the chat Id and config it.

To access the bot [@SecurityAlertBot](http://t.me/CAMSEC_AlertBot) and START it.
#
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
## Ensure start the bot
Start it --> [@SecurityAlertBot](http://t.me/CAMSEC_AlertBot)
#
## Run the Main Program
```bash
python WEBCAM_Alert.py
```
#
## To check on configuration in Telegram
Type [/check] Then check it out.
#
## CCTV Motion Detection Alert System Repository
  **Check on this repository** https://github.com/whitehatboy005/Motion-Detection-Alert-System-for-CCTV
# 
## License

This project is licensed under the terms of the [MIT license](LICENSE.md).

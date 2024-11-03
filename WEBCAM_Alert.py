import cv2
import requests
from time import time
import os
import threading
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
load_dotenv('config.env')
BOT_TOKEN = "7787875894:AAFUdd-82IZbgg33vgViV70fHBIRJDOfZlQ"
CHAT_ID = os.getenv("CHAT_ID")
roi_start_point_str = 100,100
roi_end_point_str = 300,300


def send_alert(photo_path):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
    photo = open(photo_path, 'rb')
    files = {'photo': photo}
    payload = {
        'chat_id': CHAT_ID,
        'caption': 'Alert! Someone entered the restricted area.'
    }
    try:
        response = requests.post(url, data=payload, files=files)
        if response.status_code == 200:
            print("Alert with photo sent successfully!")
        else:
            print(f"Failed to send alert: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        photo.close()
async def check_configuration(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    config_message = (
        f"Chat ID: {CHAT_ID}\n"
        f"ROI Start Point: {roi_start_point_str}\n"
        f"ROI End Point: {roi_end_point_str}\n"
    )
    await update.message.reply_text(config_message)
def motion_detection():
    cap = cv2.VideoCapture(0)

    # Convert ROI start and end points
    roi_start_point = tuple(map(int, roi_start_point_str.split(','))) if isinstance(roi_start_point_str,
                                                                                    str) else roi_start_point_str
    roi_end_point = tuple(map(int, roi_end_point_str.split(','))) if isinstance(roi_end_point_str,
                                                                                str) else roi_end_point_str

    # Set up background subtractor and thresholds
    background_subtractor = cv2.createBackgroundSubtractorMOG2()
    min_contour_area = 3000  # Minimum contour area to consider it an object
    persistence_threshold = 5  # Frames for object to be considered as "entered"
    alert_interval = 10  # Seconds between alerts

    last_alert_time = 0
    object_detected_frames = 0  # Counter for persistent detection

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Draw the ROI on the frame for visualization
        cv2.rectangle(frame, roi_start_point, roi_end_point, (0, 255, 0), 2)

        # Define and preprocess the ROI
        roi = frame[roi_start_point[1]:roi_end_point[1], roi_start_point[0]:roi_end_point[0]]
        fg_mask = background_subtractor.apply(roi)
        _, fg_mask = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)
        fg_mask = cv2.dilate(fg_mask, None, iterations=2)

        # Find contours in the thresholded mask
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        object_in_roi = False
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area:
                # Count only significant contours
                object_in_roi = True
                break

        # If an object is consistently detected within the ROI, increment the counter
        if object_in_roi:
            object_detected_frames += 1
        else:
            object_detected_frames = 0

        # Check if the object has remained in the ROI for enough frames to trigger an alert
        current_time = time()
        if object_detected_frames >= persistence_threshold and (current_time - last_alert_time) > alert_interval:
            photo_path = 'motion_alert.jpg'
            cv2.imwrite(photo_path, frame)
            send_alert(photo_path)
            last_alert_time = current_time
            object_detected_frames = 0  # Reset after alert

        # Display the frame with the ROI
        cv2.imshow('Frame', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


def main() -> None:
    print("Alert System Activated...")
    # Initialize the Application with the bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("check", check_configuration))

    # Start the motion detection in a separate thread
    motion_thread = threading.Thread(target=motion_detection)
    motion_thread.start()

    # Start the bot
    application.run_polling()
if __name__ == '__main__':
    main()

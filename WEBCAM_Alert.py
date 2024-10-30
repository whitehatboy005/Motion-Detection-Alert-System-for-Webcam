import cv2
import requests
from time import time
import os
from dotenv import load_dotenv

load_dotenv('config.env')
BOT_TOKEN = "7787875894:AAFUdd-82IZbgg33vgViV70fHBIRJDOfZlQ"
CHAT_ID = os.getenv("CHAT_ID")


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


cap = cv2.VideoCapture(0)

roi_start_point = (100, 100)
roi_end_point = (300, 300)

background_subtractor = cv2.createBackgroundSubtractorMOG2()
min_contour_area = 5000
motion_detected = False
last_alert_time = 0
alert_interval = 10

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.rectangle(frame, roi_start_point, roi_end_point, (0, 255, 0), 2)

    roi = frame[roi_start_point[1]:roi_end_point[1], roi_start_point[0]:roi_end_point[0]]

    fg_mask = background_subtractor.apply(roi)
    _, fg_mask = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)
    fg_mask = cv2.dilate(fg_mask, None, iterations=2)

    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            motion_detected = True
            break

    current_time = time()
    if motion_detected and (current_time - last_alert_time) > alert_interval:
        photo_path = 'motion_alert.jpg'
        cv2.imwrite(photo_path, frame)
        send_alert(photo_path)
        last_alert_time = current_time
        motion_detected = False

    cv2.imshow('Frame', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

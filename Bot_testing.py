import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv('config.env')

BOT_TOKEN = "7277236805:AAFNFtqNHKUzbKle0UqjEguMco6gOmrM7gQ"
CHAT_ID = os.getenv("CHAT_ID")

def send_test_message():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': 'This is a test message from my bot!'
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    send_test_message()

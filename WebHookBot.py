import requests
import time
import random

def send_message(webhook_url, message):
    try:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print("Message sent successfully")
        else:
            print(f"Failed to send message: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def main():
    webhook_url = 'YOUR_DISCORD_WEBHOOK'  # Input your Discord WebHook
    messages = [
        'YOUR_MESSAGE_1',  # Set your messages
        'YOUR_MESSAGE_2',
        'YOUR_MESSAGE_3',
        'YOUR_MESSAGE_4',
        'YOUR_MESSAGE_5',
    ]
    interval = 1  # Set your interval in seconds

    message_index = 0

    while True:
        send_message(webhook_url, messages[message_index])
        message_index = (message_index + random.randint(1, 5)) % len(messages)
        time.sleep(interval)

if __name__ == "__main__":
    main()

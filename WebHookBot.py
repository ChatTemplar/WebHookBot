import requests
import time
import random


def send_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

def main():
    webhook_url = 'YOUR_DISCORD_WEBHOOK' #Input your Discord WebHook
    messages = [
        'YOUR_MESSAGE_1', #Set your Messages
        'YOUR_MESSAGE_2',
        'YOUR_MESSAGE_3',
        'YOUR_MESSAGE_4',
        'YOUR_MESSAGE_5',
    ]
    interval = 1  # Set your time

    message_index = 0

    while True:
        send_message(webhook_url, messages[message_index])
        message_index = (message_index + (random.randint(1, 5))) % len(messages) #Change the second number from 5 to 1, if u only want first message to be send
        time.sleep(interval)

if __name__ == "__main__":
    main()

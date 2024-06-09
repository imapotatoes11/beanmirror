import requests, json, time, os
import pprint

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = 921607732384108575
MSG_LIMIT = 50
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

headers = {
    "Authorization": f"{TOKEN}"
}

# r = requests.get(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit={MSG_LIMIT}", headers=headers)
# read = [i for i in r.json()]
# [print(i['content']) for i in read]
# while True:
#     r = requests.get(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit={MSG_LIMIT}", headers=headers)
#
#     time.sleep(5)
def get_messages(channel_id, limit):
    response = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

def send_to_webhook(author, content):
    data = {
        "username": author,
        "content": content
    }
    response = requests.post(WEBHOOK_URL, json=data)
    response.raise_for_status()  # Raise an error for bad status codes


# Get initial messages and print them in the correct order
initial_messages = get_messages(CHANNEL_ID, MSG_LIMIT)
initial_messages.reverse()  # Reverse the order for correct printing
printed_message_ids = set(message['id'] for message in initial_messages)
for message in initial_messages:
    print(message['content'])


if __name__ == '__main__':
    while True:
        time.sleep(5)

        new_messages = get_messages(CHANNEL_ID, MSG_LIMIT)
        new_messages.reverse()  # Reverse the order for correct printing
        new_message_ids = set(message['id'] for message in new_messages)

        # Identify new messages by checking which IDs are not in printed_message_ids
        for message in new_messages:
            if message['id'] not in printed_message_ids:
                print(f"{message['author']['username']}: {message['content']}")
                try: send_to_webhook(message['author']['username'], message['content'])
                except: send_to_webhook("error", "attachments not supported yet")
                printed_message_ids.add(message['id'])
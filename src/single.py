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

if __name__ == "__main__":
    import pprint
    pprint.pprint(get_messages(CHANNEL_ID, 10))
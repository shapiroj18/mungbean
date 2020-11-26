import os
import requests

telegram_bot_token = os.getenv('TELEGRAM_KEY')
chat_id = os.getenv('CHAT_ID')

# Get chat_id with https://api.telegram.org/bot<YourBOTToken>/getUpdates
# Look at https://github.com/python-telegram-bot/python-telegram-bot
# Have bot send messages to user when they opt in
# Have bot respond to messages

def send_message(message_content):
    """
    message_content is a string. emojis can be included using UTF-8 encoding (https://unicode.org/emoji/charts/full-emoji-list.html)
    """

    method_name = 'sendMessage'
    telegram_endpoint = f'https://api.telegram.org/bot{telegram_bot_token}/{method_name}'

    payload = {
        'chat_id': chat_id,
        'text': message_content
    }

    response = requests.get(
        url=telegram_endpoint,
        params=payload,
    )

    return response.json(), 'Successfully sent message!'

print(send_message('\U0001F420 Have a Phishy Day!')[1])
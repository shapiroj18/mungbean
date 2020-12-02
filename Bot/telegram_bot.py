import os
import requests
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.ext import MessageHandler, Filters

telegram_bot_token = os.getenv('TELEGRAM_KEY')
chat_id = os.getenv('CHAT_ID')

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    
def callback_alarm(context: CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text='Ba-Beep!')
    
def callback_timer(update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat.id, text='Setting 1 min timer')
    context.job_queue.run_once(callback_alarm, 60, context=update.message.chat_id)
    
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oops! Didn't understand that command.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

cap_handler = CommandHandler('caps', caps)
dispatcher.add_handler(cap_handler)

timer_handler = CommandHandler('timer', callback_timer)
dispatcher.add_handler(timer_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()

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

# print(send_message('\U0001F420 Have a Phishy Day!')[1])
from telegram import Update
from telegram.ext import Updater, CallbackContext, dispatcher
from telegram.ext import CommandHandler, MessageHandler, Filters
from json import loads, dumps
from os import listdir
from decouple import config

api_token = config("API_TOKEN")

def str2Json(str):
    with open('01x02/sample.json', 'w') as f:
        f.write(dumps(loads(str), index=4))
        return 0
images = {}
for img in listdir('img'):
    with open (f'img/{img}', 'br') as f:
        images[img] = f.read()


updater = Updater(api_token)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    # این قسمت برای دریافت آرگومان است زمانی که میخواهید
    # دستوری را پشت سر هم در ربات وارد کنید
    # args = context.args
    # context.bot.send_message(chat_id=chat_id, text=f"arg args {args}")

    chat_id = update.message.chat_id
    message_id = update.message.message_id
    context.bot.send_message(chat_id=chat_id, text="hello world")

def echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message_id
    text = update.message.text
    context.bot.send_message(chat_id, text=text)

def list_img(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    text = "all image is\n\n"
    for img in listdir("img/"):
        text += f"{img}\n"
    context.bot.send_message(chat_id, text=text, reply_to_message_id=message_id)

def send_img(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    args = context.args
    for arg in args:
        try:
            context.bot.send_photo(chat_id, photo=images[arg], caption=arg)
        except:
            context.bot.send_message(chat_id, "you")
    return

    #context.bot.send_photo(chat_id=chat_id, photot=)
dispatcher.add_handler(CommandHandler(['START', 'start'], start))
dispatcher.add_handler(CommandHandler('list_all', list_img))
dispatcher.add_handler(CommandHandler('img', send_img))
dispatcher.add_handler(MessageHandler(Filters.text, echo))
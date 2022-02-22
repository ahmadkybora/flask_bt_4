from unittest import result
from telegram import Update
from telegram.ext import Updater, CallbackContext, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler, InlineQueryHandler

from telegram.utils import helpers

from decouple import config
from uuid import uuid4

def deep_link(update: Update, context: CallbackContext):
    update.message.reply_text('as')

def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = f"asa"
    bot_username = context.bot.username

    try:
        arg = context.args[0]
    except:
        arg = ""

    text += f"\n\n{arg=}"

    url = helpers.create_deep_linked_url(bot_username, str(1234))
    text += f"\n\n{url}"

    if arg == 'vip':
        deep_link(update, context)
    else:
        context.bot.send_message(chat_id, text)
    context.bot.send_message(chat_id, text)


def main():
    API_TOKEN = config('api_token')
    bot = Updater(API_TOKEN)
    dis = bot.dispatcher

    dis.add_handler(CommandHandler('start', start))
    dis.add_handler(CommandHandler('start', deep_link, Filters.regex()))
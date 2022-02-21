from asyncore import dispatcher
from decouple import config
from telegram import Update
from telegram.ext import Updater, CallbackContext, dispatcher
from telegram.ext import CommandHandler, MessageHandler, Filters

api_token = config("API_TOKEN")
updater = Updater(api_token)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    context.bot.send_message(chat_id=chat_id, text="hello world")

def echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message_id
    text = update.message.text
    context.bot.send_message(chat_id, text=text)

dispatcher.add_handler(CommandHandler(['START', 'start'], start))
# فیلتر تکست فقط تکست را دریافت میکند
dispatcher.add_handler(MessageHandler(Filters.text, echo))

# در کد زیر اجازه نمیدهد که کامند را به اکو بفرستیم یا 
# چک نمیکند میتوانید چندین رگومان بدهید
# dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
updater.start_polling()
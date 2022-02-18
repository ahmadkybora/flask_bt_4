from asyncore import dispatcher
from turtle import update
from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove,Bot,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,CallbackQuery,ParseMode
from telegram.ext import CommandHandler,Updater,Dispatcher,MessageHandler,Filters,CallbackContext,CallbackQueryHandler
import logging
import os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# token = os.getenv('TOKEN')
token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

def start(update: Update,context: CallbackContext):
    update.message.reply_text("hi")

def main():
    updater = Updater(token, use_context=True)
    bot = Bot(token)
    dispatcher: Dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

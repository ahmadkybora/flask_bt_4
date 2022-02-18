from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove,Bot,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,CallbackQuery,ParseMode
from telegram.ext import CommandHandler,Updater,Dispatcher,MessageHandler,Filters,CallbackContext,CallbackQueryHandler
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = os.getenv("TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text('start!')


def help(update: Update, context: CallbackContext):
    update.message.reply_text('Help!')


def contact_us(update: Update, context: CallbackContext):
    update.message.reply_text("Contact us")


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    keyboard = [
        [KeyboardButton('Start')],
        [KeyboardButton('Contact us')],
        [KeyboardButton('Help')], 
        [KeyboardButton('File')]
    ]
    key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("contact us", contact_us))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
import logging
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pygame import mixer

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton('شروع', callback_data='1'), InlineKeyboardButton('درباره ما', callback_data='2')], 
        [InlineKeyboardButton('سوال', callback_data='3'), InlineKeyboardButton('فایل', callback_data='4')], 
    ]
    message = "لطفا انتخاب کنید"
    reply_markup = InlineKeyboardMarkup(keyboard)
    # reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)


def help(update: Update, context: CallbackContext):
    update.message.reply_text('کمک')


def contact_us(update: Update, context: CallbackContext):
    update.message.reply_text('درباره ما')


def question(update: Update, context: CallbackContext):
    update.message.reply_text("بنال")

def file(update: Update, context: CallbackContext):
    # mixer.init()
    # mixer.music.load("1.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()
    file = context.bot.send_audio(update.effective_chat.id, audio=open('1.mp3', 'rb'))
    # bot.send_audio(chat_id=chat_id, audio=open('tests/test.mp3', 'rb'))
    update.message.reply_text(file)


def echo(update: Update, context: CallbackContext):
    update.message.reply_text("نمیفهمم چی میگی")


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("Start", start))
    dispatcher.add_handler(CommandHandler("Help", help))
    dispatcher.add_handler(CommandHandler("contactUs", contact_us))
    dispatcher.add_handler(CommandHandler("Question", question))
    dispatcher.add_handler(CommandHandler("File", file))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
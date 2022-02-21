import logging
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from pygame import mixer
from os import listdir

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
    images = []
    for img in listdir('img'):
        with open(f'img/{img}', 'br') as f:
            images.append(f.read())
    # file = context.bot.get_file(update.message.document).download()
    # update.message.reply_text(file)
    # mixer.init()
    # mixer.music.load("1.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()
    # file = context.bot.getFile(update.message.voice.file_id)
    # print ("file_id: " + str(update.message.voice.file_id))
    # file.download('voice.ogg')
    # file = context.bot.send_audio(update.effective_chat.id, audio=open('1.mp3', 'rb'))
    # # bot.send_audio(chat_id=chat_id, audio=open('tests/test.mp3', 'rb'))
    # update.message.reply_text(file)
    # file = context.bot.getFile(update.message.document.file_id)
    # mp3 = file.download(update.message.document.file_name)
    # file = context.bot.send_audio(update.effective_chat.id, audio=open(mp3, 'rb'))
    # update.message.reply_text("نمیفهمم چی میگی")
    # update.message.reply_text(file)
    # context.bot.get_file(update.message.document).download()

    # # writing to a custom file
    # with open("1.mp3", 'wb') as f:
    #     context.bot.get_file(update.message.document).download(out=f)


def get_file():
    get_file_api_url = f''
def echo(update: Update, context: CallbackContext):
    update.message.reply_text("نمیفهمم چی میگی")


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("Start", start))
    # dispatcher.add_handler(MessageHandler(["Start", "s", "START", "start"], start))
    dispatcher.add_handler(CommandHandler("Help", help))
    dispatcher.add_handler(CommandHandler("contactUs", contact_us))
    dispatcher.add_handler(CommandHandler("Question", question))
    # dispatcher.add_handler(CommandHandler("File", file))
    # dispatcher.add_handler(MessageHandler(Filters.text, file))
    dispatcher.add_handler(MessageHandler(Filters.document, file))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
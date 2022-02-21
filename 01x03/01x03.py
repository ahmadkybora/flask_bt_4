from telegram import Update
from telegram.ext import Updater, CallbackContext
from telegram.ext import CommandHandler
from telegram import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    KeyboardButton
)

from decouple import config

api_token = config("API_TOKEN")
lorem = ""

inlineKeys = [
    [InlineKeyboardButton('1', url='google.com', callback_data='1'), InlineKeyboardButton('2', url='google.com')], 
    [InlineKeyboardButton('3', url='google.com'), InlineKeyboardButton('4', url='google.com'), InlineKeyboardButton('5', url='google.com')], 
]

# کیبورد ها زو بصورت لیستی از لیست
# ساخته شده
solidKeys = [
    [KeyboardButton('1'), KeyboardButton('2')], #سطر اول 
    [KeyboardButton('3'), KeyboardButton('4'), KeyboardButton('5')], #سطر دوم 
]

def start(update: Update, context: CallbackContext):
    update.message.reply_text('h')

def solid_reply(update: Update, context: CallbackContext):
    # دکمه ها را بوسیله متد زیر میتوان 
    # ارسال کرد
    solidMarkup = ReplyKeyboardMarkup(
        keyboard=solidKeys, 
        resize_keyboard=True, 
        input_field_placeholder="hello")

    update.message.reply_text(lorem, reply_markup=solidMarkup)

def inline_reply(update: Update, context: CallbackContext):
    inlineMarkup = InlineKeyboardMarkup(inlineKeys)
    update.message.reply_text(lorem, reply_markup=inlineMarkup)

def remove_solid_reply(update: Update, context: CallbackContext):
    update.message.reply_text('h', reply_markup=ReplyKeyboardRemove)

def main():
    bot = Updater(API_TOKEN)
    dis = bot.dispatcher

    dis.add_handler(CommandHandler('start', start))
    dis.add_handler(CommandHandler('solid', solid_reply))
    dis.add_handler(CommandHandler('inline', inline_reply))
    dis.add_handler(CommandHandler('remove_reply', remove_solid_reply))

if __name__ == 'main':
    main()
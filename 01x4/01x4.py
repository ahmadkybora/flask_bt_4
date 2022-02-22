from unittest import result
from telegram.ext import Updater, CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler, InlineQueryHandler

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from decouple import config
from uuid import uuid4

def start(update: Update, context: CallbackContext):
    markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('callbackData', callback_data="hello")], 
            [InlineKeyboardButton('callbackData', switch_inline_query="hello")], 
            [InlineKeyboardButton('callbackData', switch_inline_query_current_chat="hello")], 
            [InlineKeyboardButton('callbackData', callback_data="hello")], 
        ] 
    )
    update.effective_message.reply_text('12', reply_markup=markup)

def randomMsg(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, 'hello')

def callBackQuery(update: Update, context: CallbackContext):
    data = update.callback_query.data
    id = update.callback_query.id
    if data == 'hello':
        update.callback_query.answer('this', show_alert=True)
        context.bot.answer_callback_query(id, '')
    else:
        print('Invalid')
        randomMsg(update, context)

# برای استفاده از 
# inlineQuery
# باید تنظیمات بات
# inline feedback
# را انجام دهید در بات تلگرامی خود
def inlineQuery(update: Update, context: CallbackContext):
    data = update.inline_query.query
    if data == "hello":
        result = [
            InlineQueryResultArticle(
                id = uuid4(), 
                title = "Article", 
                input_message_content=InputTextMessageContent("asda"), 
                description="asdasdas", 
                thumb_url="ggogl.c"
            ), 
            InlineQueryResultArticle(
                id = uuid4(), 
                title = "Article", 
                input_message_content=InputTextMessageContent("asda"), 
                description="asdasdas", 
                thumb_url="ggogl.c"
            )
        ]
    else:
        result = [
            InlineQueryResultArticle(
                id = uuid4(), 
                title = "Article", 
                input_message_content=InputTextMessageContent("asda"), 
                description="asdasdas", 
                thumb_url="ggogl.c"
            )
        ]
    update.inline_query.answer(result, cache_time=2)
    context.bot.answer_inline_query(update.inline_query.id, )

def main():
    API_TOKEN = config("api_token")
    bot = Updater(API_TOKEN)
    dis = bot.dispatcher

    dis.add_handler(CommandHandler('start', start))
    dis.add_handler(CallbackQueryHandler(callBackQuery))
    dis.add_handler(InlineQueryHandler(inlineQuery))

    bot.start_polling()
    bot.idle()

if __name__ == '__main__':
    main()
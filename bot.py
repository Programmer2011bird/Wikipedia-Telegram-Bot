from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from configs import API_KEY
import telebot


BOT: telebot.TeleBot = telebot.TeleBot(API_KEY)

def Output_Markup():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Full Article - HTML File", callback_data="html")
    button2 = InlineKeyboardButton("Full Article - PDF File", callback_data="pdf")
    button3 = InlineKeyboardButton("Summary - No File", callback_data="summary")

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    return markup

@BOT.callback_query_handler(func=lambda call:True)
def get_output_type(call: CallbackQuery):
    if call.data == "html":
        print("html")

    elif call.data == "pdf":
        print("pdf")

    elif call.data == "summary":
        print("summary")


@BOT.message_handler(commands=["start"])
def start_msg(message) -> None:
    BOT.reply_to(message, "Welcome to WikiPedia Telegram Bot, To Start, Please Send The Title Of The Article")

@BOT.message_handler(func=lambda message:True)
def get_Article_Title(message:Message) -> None:
    TITLE: str = str(message.text)
    BOT.reply_to(message, f"Received title: {TITLE}")

    BOT.send_message(
        message.chat.id,
        "Now Please Select The Output Type Of Your Article",
        reply_markup=Output_Markup()
    )

BOT.infinity_polling(timeout=None)


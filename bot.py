from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from configs import API_KEY
from os import remove
import telebot
import api


BOT: telebot.TeleBot = telebot.TeleBot(API_KEY)
TITLES: dict[int, str] = {}

def download_article(message:Message, Title:str, OutType:str):
    user_id: int = message.from_user.id
    chat_id: int = message.chat.id
    
    API: api.API_HANDLER = api.API_HANDLER()

    match OutType:
        case "html":
            F_CONTENT: str = API.getFullHTML(Title)
            FILENAME: str = f"{user_id}.html"
            DONWLOADER: api.Downloader = api.Downloader(F_CONTENT, f"./{FILENAME}")

            send_file(user_id, chat_id, "html")

        case "pdf":
            CONTENT: bytes = API.getFullPDF(Title)
            FILENAME: str = f"{user_id}.pdf"
            DONWLOADER: api.Downloader = api.Downloader(CONTENT, f"./{FILENAME}")

            send_file(user_id, chat_id, "pdf")

def send_summary(Title: str, chat_id: int):
    API: api.API_HANDLER = api.API_HANDLER()
    CONTENT: str = API.getSummary(Title)

    BOT.send_message(chat_id, CONTENT)

    TITLES.pop(chat_id)

def send_file(user_id: int, chat_id: int, file_type: str):
    FilePath: str = f"./{user_id}.{file_type}"
    
    with open(FilePath, "rb") as document:
        BOT.send_document(chat_id, document, timeout=180)

    remove(FilePath)
    TITLES.pop(chat_id)

def Output_Markup():
    markup: InlineKeyboardMarkup = InlineKeyboardMarkup()
    button1: InlineKeyboardButton = InlineKeyboardButton("Full Article - HTML File", callback_data="html")
    button2: InlineKeyboardButton = InlineKeyboardButton("Full Article - PDF File", callback_data="pdf")
    button3: InlineKeyboardButton = InlineKeyboardButton("Summary - No File", callback_data="summary")

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    return markup

@BOT.callback_query_handler(func=lambda call:True)
def get_output_type(call: CallbackQuery):
    if call.data == "html":
        download_article(call.message, TITLES[call.message.chat.id], "html")

    elif call.data == "pdf":
        download_article(call.message, TITLES[call.message.chat.id], "pdf")

    elif call.data == "summary":
        send_summary(TITLES[call.message.chat.id], call.message.chat.id)

@BOT.message_handler(commands=["start"])
def start_msg(message:Message) -> None:
    BOT.reply_to(message, "Welcome to WikiPedia Telegram Bot, To Start, Please Send The Title Of The Article")

@BOT.message_handler(func=lambda message:True)
def get_Article_Title(message:Message) -> None:
    TITLE: str = str(message.text)
    TITLES[message.from_user.id] = TITLE

    BOT.send_message(
        message.chat.id,
        "Now Please Select The Output Type Of Your Article",
        reply_markup=Output_Markup()
    )

BOT.infinity_polling()

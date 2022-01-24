from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

Bot = Client(
    "Web2PDF-Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
Hi {}, I am web2pdf Bot.
> `I can download webpages as PDF.`
Send any URL to get started.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/web2pdf-bot'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.text)
async def webtopdf(_, m):




Bot.run()
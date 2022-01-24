from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, time
import requests

BOT_TOKEN = " "
API_ID = " "
API_HASH = " "

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

    url = m.text

    

    time_limit = 30
    time_elapsed = 0
    start_time_in_seconds = time.time()
    with requests.get(url, stream=True, allow_redirects=True) as r :
        with open('video.mp4', 'wb') as f :
            for chunk in r.iter_content(chunk_size=1024*1024) :
                if (chunk) :
                    f.write(chunk)
                if time_elapsed > time_limit:
                    break
                if int(time.time() - start_time_in_seconds)- time_elapsed > 0 :
                    time_elapsed = int(time.time() - start_time_in_seconds)
    await m.reply_video('video.mp4')



Bot.run()

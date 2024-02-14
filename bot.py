import os, wave
from piper.voice import PiperVoice as piper #Backbone of text to speech
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

Bot = Client(
    "PersianT2SBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
voice = piper.load("model/epoch=5261-step=2455712.onnx")


START_TXT = """
Hi {}, I'm Persian TTS Bot.

Just send me your text.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/soebb'),
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
async def t2s(bot, m):
    input = m.text
    msg = await m.reply("Processing..")
    output_name = "output.wav"
    with wave.open(output_name, "wb") as wav_file:
        voice.synthesize(input, wav_file)
    await bot.send_audio(chat_id=m.chat.id, audio=output_name)
    await msg.delete()
    os.remove(output_name)


Bot.run()
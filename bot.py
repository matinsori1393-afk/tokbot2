from nicotin import Client, filters
from flask import Flask
import threading
import os

TOKEN = "CGHDBG0GPEBTDACIEDRKLPQXIVFHAAOQUBVSGFYJSFEJKDAVMSIVFSOXMKTBJBKD"
JOIN_LINK = "https://rubika.ir/Linkdnoni_Parsi"
ADMIN_CHAT = None

app = Client(bot_token=TOKEN)
web = Flask(name)

@web.route('/')
def health():
    return "OK"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web.run(host='0.0.0.0', port=port)

@app.on_message(filters.command("start"))
async def start(client, message):
    global ADMIN_CHAT
    chat_id = message.chat_id
    if not ADMIN_CHAT:
        ADMIN_CHAT = chat_id
        await message.reply("✅ ثبت شد! از این به بعد لینک‌ها برات میاد.")
        return
    await message.reply(f"سلام!\n\nاول توی کانال ما عضو شو:\n{JOIN_LINK}\n\nبعد لینکت رو بفرست.")

@app.on_message()
async def handler(client, message):
    global ADMIN_CHAT
    text = message.text
    chat_id = message.chat_id
    if not text or text.startswith("/"):
        return
    if ADMIN_CHAT and str(chat_id) == str(ADMIN_CHAT):
        return
    if ADMIN_CHAT:
        await client.send_message(ADMIN_CHAT, f"📥 لینک جدید:\nمتن: {text}\nاز چت: {chat_id}")
        await message.reply("✅ لینکت ثبت شد. منتظر تایید ادمین باش.")
    else:
        await message.reply("⚠️ ادمین هنوز ربات رو تنظیم نکرده.")

threading.Thread(target=run_web, daemon=True).start()

app.run()

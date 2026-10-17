from nicotin import Client, filters

TOKEN = "CGHDBG0GPEBTDACIEDRKLPQXIVFHAAOQUBVSGFYJSFEJKDAVMSIVFSOXMKTBJBKD"
JOIN_LINK = "https://rubika.ir/Linkdnoni_Parsi"
ADMIN_CHAT = None

app = Client(bot_token=TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    global ADMIN_CHAT
    chat_id = message.chat_id
    if not ADMIN_CHAT:
        ADMIN_CHAT = chat_id
        await message.reply("✅ ثبت شد!")
        return
    await message.reply(f"سلام!\n\nاول توی کانال ما عضو شو:\n{JOIN_LINK}\n\nبعد لینکت رو بفرست.")

@app.on_message()
async def handler(client, message):
    global ADMIN_CHAT
    text = message.text
    chat_id = message.chat_id
    user = getattr(message, 'from_user', None)
    uid = getattr(user, 'id', None) if user else None
    if not text or text.startswith("/"):
        return
    if ADMIN_CHAT and str(chat_id) == str(ADMIN_CHAT):
        return
    if ADMIN_CHAT:
        await client.send_message(ADMIN_CHAT, f"📥 لینک جدید:\nآیدی کاربر: {uid}\nGUID چت: {chat_id}\nمتن: {text}")
        await message.reply("✅ لینکت ثبت شد.")
    else:
        await message.reply("⚠️ ادمین هنوز ربات رو تنظیم نکرده.")

app.run()

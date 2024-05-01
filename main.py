from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

DrJay = Client(
      name="DrAstrobot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
)

print("Bot started")

DrJay.run()

from pyrogram import Client, filters


API_ID = "26982594"
API_HASH = "313be9b7265ea53cdd381bf4f99681ac"
BOT_TOKEN = "7166595418:AAHtd7yqvDFMzXaTBgaxHh9NFZi5PxHPJ0Q"

DrJay = Client(
      name="DrAstrobot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
)


@DrJay.on_message(filters.command("start"))
async def start_cmd(client, message):
      print("START Command")

@DrJay.on_message(filters.command("help"))
async def help_cmd(client, message):
      print("HELP Command")


print("Bot started")

DrJay.run()

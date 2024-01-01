import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="DAXXSTRINGBOT"),
)


if __name__ == "__main__":
    print("Sᴛᴀʀᴛɪɴɢ Yᴏᴜʀ Sᴛʀɪɴɢ Bᴏᴛ...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Sᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ, Mᴀᴅᴇ Bʏ @Tʜᴇ_RᴇᴀʟRᴀᴅɪᴜx ❤️")
    idle()
    app.stop()
    print("Bᴏᴛ Sᴛᴏᴘᴘᴇᴅ !")

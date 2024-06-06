import sys
import heroku3

from config import X1, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from pyrogram import enums
from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        start = datetime.now()
        altron = await e.reply(f"🐙")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"✦ ᴘɪɴɢ sᴛᴀᴛs ⏤͟͟͞͞★\n➥ `{mp} ᴍꜱ`")

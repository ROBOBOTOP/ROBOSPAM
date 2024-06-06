import asyncio

from random import choice

from telethon import events
from pyrogram import enums

from config import X1, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from ROYEDITX.data import PBIRAID, AVISHA

REPLY_RAID = []

@X1.on(events.NewMessage(incoming=True))
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(PBIRAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sprraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in AVISHA:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ xsᴘᴀᴍ'ꜱ ᴏᴡɴᴇʀ.")
            elif user_id == OWNER_ID:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif user_id in SUDO_USERS:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("✦ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʜɪʀᴇᴘʟʏʀᴀɪᴅ ✅")
        except NameError:
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐏𝐁𝐈𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝 ➥ {hl}prraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}prraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdprraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("✦ ʀᴇᴘʟʏ ʜɪʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")
        except NameError:
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐏𝐁𝐈𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝 ➥ {hl}dprraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}dprraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

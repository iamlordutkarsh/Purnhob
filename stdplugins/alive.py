""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd

###additional stuff 

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node

######


@borg.on(admin_cmd("alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = " Working Fine Keks \n My Owner: {DEFAULTUSER} \n Server:Online \n Telethon version: 1.11.3 \n Python: 3.8.3 "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

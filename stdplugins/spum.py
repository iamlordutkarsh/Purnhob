# For UniBorg
# By Priyam Kalra
# Syntax (.spam <number of msgs> <text>)

from asyncio import wait
from telethon import events
from uniborg.util import admin_cmd
import asyncio
from telethon.tl import functions, types
from time import sleep


@borg.on(admin_cmd(pattern="spam ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = str(event.pattern_match.group(1))
    input_split = input.split()
    chat = event.chat_id
    try:
        count = str(input_split[0])
    except ValueError:
        await event.edit("Invalid Syntax!\nTip: Use ```.syntax spam``` for help.")
        return
    if input.startswith(count):
        strip = len(count)
        text = input[strip:]
    else:
        await event.edit("Fatal Error!\nPlease contact the developer of this module [@A_FRICKING_GAMER] for support.")
        return
    if text and count != None:
        for spam in range(int(count)):
            await event.reply(text)
        msg = await event.reply(f".spam 5555 SPAM")
        sleep(5)
        await msg.delete()
        status = f"SPAMMED\n```{text}```\n in {chat} ```{count}``` times."
        await log(status)
    else:
        await event.edit("Unexpected Error! Aborting..")
        return

async def log(text):
    LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
    await borg.send_message(LOGGER, text)

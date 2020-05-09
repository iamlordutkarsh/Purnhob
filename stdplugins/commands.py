"""COMMAND : .command"""
"""Fucking Plugin written By iamlordutkarsh"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("command"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Plugin Written By Lord witcher (@lordwitcher , @iamlordutkarsh)** \n Info = .info \n Afk = .afk \n Carbon = .kargb \n Kill = .kill \n Alive = .alive \n Animate = .load , .square , .up , .round , .heart , .anim , .fml ,.monkey \n Aria = .magnet, .tor, .url, .show, .ariaRM \n Blacklist = .addblacklist ,.listblacklist , .rmblacklist \n Calculator = .calc \n Calendar = .calender \n Chain = .chain \n Kang Sticker = .kang \n SpeedTest = .speedtest \n Gaali = .gaali \n Abuse = .abuse \n React = .react \n Spam = .spam (number) (text) \n Ping = .porn \n Whois = .whois \n Ban = .ban \n Other Commands Adding Soon...."
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

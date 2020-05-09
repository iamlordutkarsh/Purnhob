#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Chaliye Shuru Karte Hai String Session ==>> my.telegram.com (vpn use karna) <<==
Apna Telegram Account login karna !
Click on API Development Tools ,
Create a new application, by Entering the Required Details """)
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("API HASH Enter Kar: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())

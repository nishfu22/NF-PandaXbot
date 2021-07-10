# PORT BY ILHAM MANSIEZ
# KARENA GABUT JADI GUE BUAT ASTAGA NGAKAK

"""
💐 Commands Available : payudara
• `{i}payudara`
   mengirim gambar tetek besar 😂.
"""


import asyncio
import os
import urllib

import requests

from . import *

from PandaX_Userbot.misc._supporter import TMP_DOWNLOAD_DIRECTORY

TMP_DOWNLOAD_DIRECTORY = "resources/downloads/"


@ilhammansiz_cmd(pattern="payudara ?(.*)")
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(TMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Menemukan beberapa payudara besar untukmu 😂")
    await asyncio.sleep(0.5)
    await a.edit("Ini besar banget nih 😂")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()

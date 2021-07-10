"""
💐 Commands Available -
•`{i}addprofanity`
   If someone sends bad word in a chat, Then bot will delete that message.
•`{i}remprofanity`
   From chat from Profanity list.
"""


from ProfanityDetector import detector

from . import *


@ilhammansiz_cmd(pattern="addprofanity$", admins_only=True)
async def addp(e):
    # action features not added yet or not needed ig 😂😂
    profan_chat(e.chat_id, "mute")
    await eod(e, "`Added This Chat for Profanity Filtering!`", time=10)


@ilhammansiz_cmd(pattern="remprofanity", admins_only=True)
async def remp(e):
    rem_profan(e.chat_id)
    await eod(e, "`Removed This Chat from Profanity Filtering!`", time=10)


@petercordpanda_bot.on(events.NewMessage(incoming=True))
async def checkprofan(e):
    chat = e.chat_id
    if is_profan(chat) and e.text:
        x, y = detector(e.text)
        if y:
            await e.delete()

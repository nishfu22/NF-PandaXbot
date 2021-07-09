# ilham mansiez

import asyncio
import os
import time
import traceback
import urllib
from pathlib import Path
from random import randint
from urllib.request import urlretrieve

import telethon.utils
from pytz import timezone
from telethon import TelegramClient
from telethon import __version__ as vers
from telethon.errors.rpcerrorlist import (
    AccessTokenExpiredError,
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    ChannelsTooMuchError,
    PhoneNumberInvalidError,
)
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

from . import *
from .dB import DEVLIST
from .dB.database import Var
from .functions.all import updater
from .utils import load_assistant, load_modules, load_plugins, load_pmbot
from .version import __version__ as ver

x = ["resources/auths", "resources/downloads", "addons"]
for x in x:
    if not os.path.isdir(x):
        os.mkdir(x)

if udB.get("CUSTOM_THUMBNAIL"):
    urlretrieve(udB.get("CUSTOM_THUMBNAIL"), "resources/extras/petercordpanda.jpg")

if udB.get("GDRIVE_TOKEN"):
    with open("resources/auths/auth_token.txt", "w") as t_file:
        t_file.write(udB.get("GDRIVE_TOKEN"))

if udB.get("MEGA_MAIL") and udB.get("MEGA_PASS"):
    with open(".megarc", "w") as mega:
        mega.write(
            f'[Login]\nUsername = {udB.get("MEGA_MAIL")}\nPassword = {udB.get("MEGA_PASS")}'
        )

if udB.get("TIMEZONE"):
    try:
        timezone(udB.get("TIMEZONE"))
        os.environ["TZ"] = timezone(udB.get("TIMEZONE"))
        time.tzset()
    except BaseException:
        LOGS.info(
            "Incorrect Timezone ,\nCheck Available Timezone From Here https://telegra.ph/iLHam-MansiezZ-06-27\nSo Time is Default UTC"
        )
        os.environ["TZ"] = "UTC"
        time.tzset()


async def autobot():
    await petercordpanda_bot.start()
    if Var.BOT_TOKEN:
        udB.set("BOT_TOKEN", str(Var.BOT_TOKEN))
        return
    if udB.get("BOT_TOKEN"):
        return
    LOGS.info("MAKING A TELEGRAM BOT FOR YOU AT @BotFather , Please Kindly Wait")
    who = await petercordpanda_bot.get_me()
    name = who.first_name + "'s Assistant Bot"
    if who.username:
        username = who.username + "_bot"
    else:
        username = "petercordpanda_" + (str(who.id))[5:] + "_bot"
    bf = "Botfather"
    await petercordpanda_bot(UnblockRequest(bf))
    await petercordpanda_bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await petercordpanda_bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await petercordpanda_bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
        )
        exit(1)
    await petercordpanda_bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await petercordpanda_bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
            )
            exit(1)
    await petercordpanda_bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
    await petercordpanda_bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "petercordpanda_" + (str(who.id))[6:] + str(ran) + "_bot"
        await petercordpanda_bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            udB.set("BOT_TOKEN", token)
            await petercordpanda_bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(bf, "Search")
            LOGS.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
        else:
            LOGS.info(
                f"Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
            )
            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        udB.set("BOT_TOKEN", token)
        await petercordpanda_bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await petercordpanda_bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await petercordpanda_bot.send_message(bf, "Search")
        LOGS.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
    else:
        LOGS.info(
            f"Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
        )
        exit(1)


if not udB.get("BOT_TOKEN"):
    petercordpanda_bot.loop.run_until_complete(autobot())


async def istart(ult):
    await petercordpanda_bot.start(ult)
    petercordpanda_bot.me = await petercordpanda_bot.get_me()
    petercordpanda_bot.uid = telethon.utils.get_peer_id(petercordpanda_bot.me)
    petercordpanda_bot.first_name = petercordpanda_bot.me.first_name
    if not petercordpanda_bot.me.bot:
        udB.set("OWNER_ID", petercordpanda_bot.uid)


async def autopilot():
    await petercordpanda_bot.start()
    if Var.LOG_CHANNEL and str(Var.LOG_CHANNEL).startswith("-100"):
        udB.set("LOG_CHANNEL", str(Var.LOG_CHANNEL))
    k = []  # To Refresh private ids
    async for x in petercordpanda_bot.iter_dialogs():
        k.append(x.id)
    if udB.get("LOG_CHANNEL"):
        try:
            await petercordpanda_bot.get_entity(int(udB.get("LOG_CHANNEL")))
            return
        except BaseException:
            udB.delete("LOG_CHANNEL")
    try:
        r = await petercordpanda_bot(
            CreateChannelRequest(
                title="🐼 Panda Privat Grup",
                about="🐼 Panda Privat Grup\n\n Join @TEAMSquadUserbotSupport",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "You Are On Too Many Channels & Groups , Leave some And Restart The Bot"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "Something Went Wrong , Create A Group and set its id on config var LOG_CHANNEL."
        )
        exit(1)
    chat_id = r.chats[0].id
    if not str(chat_id).startswith("-100"):
        udB.set("LOG_CHANNEL", "-100" + str(chat_id))
    else:
        udB.set("LOG_CHANNEL", str(chat_id))
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )
    await petercordpanda_bot(
        EditAdminRequest(chat_id, asst.me.username, rights, "Assistant")
    )
    pfpa = await petercordpanda_bot.download_profile_photo(chat_id)
    if not pfpa:
        urllib.request.urlretrieve(
            "https://telegra.ph/file/0d025dc216d0ae5d36b07.jpg", "channelphoto.jpg"
        )
        ll = await petercordpanda_bot.upload_file("channelphoto.jpg")
        await petercordpanda_bot(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
        os.remove("channelphoto.jpg")
    else:
        os.remove(pfpa)


petercordpanda_bot.asst = None


async def bot_info(asst):
    await asst.start()
    asst.me = await asst.get_me()
    return asst.me


LOGS.info("Initialising...")
LOGS.info(f"PandaX_Userbot Version - {ver}")
LOGS.info(f"🤖 Telethon Version 🤖- {vers}")
LOGS.info("🐼 PandaUserbot Version - 0.0.8.1")


# log in
BOT_TOKEN = udB.get("BOT_TOKEN")
LOGS.info("Starting 🐼 PandaUserbot...")
try:
    petercordpanda_bot.asst = TelegramClient(
        "asst-session", api_id=Var.API_ID, api_hash=Var.API_HASH
    ).start(bot_token=BOT_TOKEN)
    asst = petercordpanda_bot.asst
    petercordpanda_bot.loop.run_until_complete(istart(asst))
    petercordpanda_bot.loop.run_until_complete(bot_info(asst))
    LOGS.info("Done, startup completed")
    LOGS.info("UserBot - Started")
except AuthKeyDuplicatedError or PhoneNumberInvalidError or EOFError:
    LOGS.info(
        "Session String expired. Please create a new one! 🐼 PandaUserbot stopping..."
    )
    exit(1)
except ApiIdInvalidError:
    LOGS.info("Your API ID/API HASH combination is invalid. Kindly recheck.")
    exit(1)
except AccessTokenExpiredError:
    udB.delete("BOT_TOKEN")
    LOGS.info(
        "BOT_TOKEN expired , So Quitted The Process, Restart Again To create A new Bot. Or Set BOT_TOKEN env In Vars"
    )
    exit(1)
except BaseException:
    LOGS.info("Error: " + str(traceback.print_exc()))
    exit(1)


if str(petercordpanda_bot.uid) not in DEVLIST:
    chat = eval(udB.get("BLACKLIST_CHATS"))
    if -1001159103924 not in chat:
        chat.append(-1001159103924)
        udB.set("BLACKLIST_CHATS", str(chat))

petercordpanda_bot.loop.run_until_complete(autopilot())

# for userbot
files = sorted(os.listdir("plugins"))
for plugin_name in files:
    try:
        if plugin_name.endswith(".py"):
            load_plugins(plugin_name[:-3])
            if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                LOGS.info(f"🐼 PandaUserbot - Official -  Installed - {plugin_name}")
    except Exception:
        LOGS.info(f"🐼 PandaUserbot - Official - ERROR - {plugin_name}")
        LOGS.info(str(traceback.print_exc()))


# for assistant
files = sorted(os.listdir("assistant"))
for plugin_name in files:
    try:
        if plugin_name.endswith(".py"):
            load_assistant(plugin_name[:-3])
            if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                LOGS.info(f"🐼 PandaUserbot - Assistant -  Installed - {plugin_name}")
    except Exception:
        LOGS.info(f"🐼 PandaUserbot - Assistant - ERROR - {plugin_name}")
        LOGS.info(str(traceback.print_exc()))

# for addons
modules = udB.get("MODULES")
if modules == "True" or modules is None:
    try:
        os.system(
            "git clone https://github.com/ilhammansiz/PandaX_UserbotModules modules/"
        )
    except BaseException:
        pass
    LOGS.info("Installing packages for modules")
    os.system("pip install -r modules/modules.txt")
    files = sorted(os.listdir("modules"))
    for plugin_name in files:
        try:
            if plugin_name.endswith(".py"):
                load_modules(plugin_name[:-3])
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    LOGS.info(f"🐼 PandaUserbot - Modules -  Installed - {plugin_name}")
        except Exception:
            LOGS.info(f"🐼 PandaUserbot - Modules - ERROR - {plugin_name}")
            LOGS.info(str(traceback.print_exc()))
else:
    os.system("cp plugins/__init__.py modules/")

# for channel plugin
Plug_channel = udB.get("PLUGIN_CHANNEL")
if Plug_channel:

    async def plug():
        try:
            if Plug_channel.startswith("@"):
                chat = Plug_channel
            else:
                try:
                    chat = int(Plug_channel)
                except BaseException:
                    return
            async for x in petercordpanda_bot.iter_messages(
                chat, search=".py", filter=InputMessagesFilterDocument
            ):
                await asyncio.sleep(0.6)
                files = await petercordpanda_bot.download_media(x.media, "./addons/")
                file = Path(files)
                plugin = file.stem
                if "(" not in files:
                    try:
                        load_modules(plugin.replace(".py", ""))
                        LOGS.info(
                            f"🐼 PandaUserbot - PLUGIN_CHANNEL - Installed - {plugin}"
                        )
                    except Exception as e:
                        LOGS.info(f"🐼 PandaUserbot - PLUGIN_CHANNEL - ERROR - {plugin}")
                        LOGS.info(str(e))
                else:
                    LOGS.info(f"Plugin {plugin} is Pre Installed")
                    os.remove(files)
        except Exception as e:
            LOGS.info(str(e))


# chat via assistant
pmbot = udB.get("PMBOT")
if pmbot == "True":
    files = sorted(os.listdir("assistant/pmbot"))
    for plugin_name in files:
        if plugin_name.endswith(".py"):
            load_pmbot(plugin_name[:-3])
    LOGS.info(f"PetercordPanda - PM Bot Message Forwards - Enabled.")

# customize assistant


async def customize():
    try:
        chat_id = int(udB.get("LOG_CHANNEL"))
        xx = await petercordpanda_bot.get_entity(asst.me.username)
        if xx.photo is None:
            LOGS.info("Customising Ur Assistant Bot in @BOTFATHER")
            UL = f"@{asst.me.username}"
            if (petercordpanda_bot.me.username) is None:
                sir = petercordpanda_bot.me.first_name
            else:
                sir = f"@{petercordpanda_bot.me.username}"
            await petercordpanda_bot.send_message(
                chat_id, "Auto Customisation Started on @botfather"
            )
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", "/cancel")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", "/start")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", "/setuserpic")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await petercordpanda_bot.send_file(
                "botfather", "resources/extras/petercordpanda_assistant.jpg"
            )
            await asyncio.sleep(2)
            await petercordpanda_bot.send_message("botfather", "/setabouttext")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(
                "botfather", f"🙋 Hello ✨ Saya Assistant Bot of {sir}"
            )
            await asyncio.sleep(2)
            await petercordpanda_bot.send_message("botfather", "/setdescription")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(
                "botfather",
                f"🐼 PandaUserbot Assistant\nPengguna ~ {sir}\n\nBy ~ @diemmmmmmmmmm\nSupport ~ @TEAMSquadUserbotSupport ",
            )
            await asyncio.sleep(2)
            await petercordpanda_bot.send_message(
                chat_id, "**Auto membuat bot asisten** selesai @BotFather"
            )
            LOGS.info("Customisation Done")
    except Exception as e:
        LOGS.warning(str(e))


# some stuffs
async def ready():
    chat_id = int(udB.get("LOG_CHANNEL"))
    MSG = f"**🐼 PandaUserbot Menyala **\n➖➖➖➖➖➖➖➖➖\n**UserMode**: [{petercordpanda_bot.me.first_name}](tg://user?id={petercordpanda_bot.me.id})\n**Assistant**: @{asst.me.username}\n➖➖➖➖➖➖➖➖➖\n**Support**: @TEAMSquadUserbotSupport\n➖➖➖➖➖➖➖➖➖"
    BTTS = [Button.inline("Help", "open")]
    updava = await updater()
    try:
        if updava:
            BTTS = [
                [Button.inline("Update Available", "updtavail")],
                [Button.inline("Help", "open")],
            ]
        await petercordpanda_bot.asst.send_message(chat_id, MSG, buttons=BTTS)
    except BaseException:
        try:
            await petercordpanda_bot.send_message(chat_id, MSG)
        except Exception as ef:
            LOGS.info(ef)
    try:
        # To Let Them know About New Updates and Changes
        await petercordpanda_bot(JoinChannelRequest("@TEAMSquadUserbotSupport"))
    except BaseException:
        pass


ws = f"WEBSOCKET_URL=http://localhost:6969"
lg = f"LOG_CHANNEL={udB.get('LOG_CHANNEL')}"
bt = f"BOT_TOKEN={udB.get('BOT_TOKEN')}"
try:
    with open(".env", "r") as x:
        m = x.read()
    if "WEBSOCKET_URL" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + ws)
    if "LOG_CHANNEL" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + lg)
    if "BOT_TOKEN" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + bt)
except BaseException:
    with open(".env", "w") as t:
        t.write(ws + "\n" + lg + "\n" + bt)


petercordpanda_bot.loop.run_until_complete(customize())
if Plug_channel:
    petercordpanda_bot.loop.run_until_complete(plug())
petercordpanda_bot.loop.run_until_complete(ready())

LOGS.info(
    """
                ----------------------------------------------------------------------
                   🐼 PandaUserbot berhasil deployed! Contact @diemmmmmmmmmm for updates!!
                ----------------------------------------------------------------------
"""
)


petercordpanda_bot.run_until_disconnected()

import re
import time
from datetime import datetime
from math import ceil
from os import remove

from git import Repo
from support import *
from telethon.tl.types import InputBotInlineResult, InputWebDocument

from PandaX_Userbot.misc import owner_and_sudos

from . import *

# ================================================#
notmine = f"ini adalah bot milik {OWNER_NAME}"

TLINK = "https://telegra.ph/file/0d025dc216d0ae5d36b07.jpg"
helps = get_string("inline_1")

add_ons = udB.get("MODULES")
if add_ons == "True" or add_ons is None:
    zhelps = get_string("inline_2")
else:
    zhelps = get_string("inline_3")

C_PIC = udB.get("INLINE_PIC")

if C_PIC:
    _file_to_replace = C_PIC
    TLINK = C_PIC
else:
    _file_to_replace = "resources/extras/inline.jpg"
# ============================================#


# --------------------BUTTONS--------------------#

_main_help_menu = [
    [
        Button.url("🏅 SUPPORT 🏅", url=f"https://t.me/TEAMSquadUserbotSupport"),
    ],
    [
        Button.inline("📙 𝙿𝙻𝚄𝙶𝙸𝙽𝚂 📙", data="hrrrr"),
        Button.inline("📗 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 📗", data="frrr"),
    ],
    [
        Button.inline("📒Exra Panda📒", data="ilham"),
    ],
    [
        Button.inline("🐼 DATA PANDA 🐼", data="ownr"),
        Button.inline("🎗 PlayStore 🎗", data="inlone"),
    ],
    [
        Button.url("⚙️ 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂 ⚙️", url=f"https://t.me/{asst.me.username}?start=set"),
    ],
    [Button.inline("✖ 𝙲𝙻𝙾𝚂𝙴 ✖", data="close")],
]

SUP_BUTTONS = [
    [
        Button.url("𝚁𝙴𝙿𝙾", url="https://github.com/IlhamMansiz/PandaX_Userbot"),
        Button.url(
            "𝐌𝐨𝐝𝐮𝐥𝐞𝐬", url="https://github.com/IlhamMansiz/PandaX_UserbotModules"
        ),
    ],
    [Button.url("SUPPORT", url="https://t.me/TEAMSquadUserbotSupport")],
]

# --------------------BUTTONS--------------------#


@in_pattern("")
@in_owner
async def inline_alive(o):
    if len(o.text) == 0:
        b = o.builder
        MSG = "🐼 **Panda Userbot** 🐼"
        uptime = grt(time.time() - start_time)
        MSG += f"\n\n⚡ **UPTIME** - `{uptime}`\n"
        MSG += f"👾 **OWNER** - `{OWNER_NAME}`"
        WEB0 = InputWebDocument(
            "https://telegra.ph/file/0d025dc216d0ae5d36b07.jpg", 0, "image/jpg", []
        )
        RES = [
            InputBotInlineResult(
                str(o.id),
                "photo",
                send_message=await b._message(
                    text=MSG,
                    media=True,
                    buttons=SUP_BUTTONS,
                ),
                title="🐼 PANDAUSERBOT 🐼",
                description="USERBOT | TELETHON",
                url=TLINK,
                thumb=WEB0,
                content=InputWebDocument(TLINK, 0, "image/jpg", []),
            )
        ]
        await o.answer(RES, switch_pm=f"🐼 PandaUserbot PORTAL", switch_pm_param="start")


@in_pattern("ultd")
@in_owner
async def inline_handler(event):
    z = []
    for x in LIST.values():
        for y in x:
            z.append(y)
    result = event.builder.photo(
        file=_file_to_replace,
        link_preview=False,
        text=get_string("inline_4").format(
            OWNER_NAME,
            len(PLUGINS),
            len(MODULES),
            len(z),
        ),
        buttons=_main_help_menu,
    )
    await event.answer([result], gallery=True)


@in_pattern("paste")
@in_owner
async def _(event):
    ok = event.text.split(" ")[1]
    link = "https://nekobin.com/"
    result = event.builder.article(
        title="Paste",
        text="ᴘᴀsᴛᴇᴅ ᴛᴏ ɴᴇᴋᴏʙɪɴ.",
        buttons=[
            [
                Button.url("NEKOBIN", url=f"{link}{ok}"),
                Button.url("RAW", url=f"{link}raw/{ok}"),
            ],
        ],
    )
    await event.answer([result])


@in_pattern("dog")
@in_owner
async def _(event):
    ok = event.text.split(" ")[1]
    link = "https://del.dog/"
    result = event.builder.article(
        title="Paste",
        text="ᴘᴀsᴛᴇᴅ ᴛᴏ ᴅᴏɢʙɪɴ.",
        buttons=[
            [
                Button.url("DOGBIN", url=f"{link}{ok}"),
                Button.url("RAW", url=f"{link}raw/{ok}"),
            ],
        ],
    )
    await event.answer([result])


@callback("ownr")
@owner
async def setting(event):
    z = []
    for x in LIST.values():
        for y in x:
            z.append(y)
    cmd = len(z)
    await event.edit(
        get_string("inline_4").format(
            OWNER_NAME,
            len(PLUGINS),
            len(MODULES),
            cmd,
        ),
        file=_file_to_replace,
        link_preview=False,
        buttons=[
            [
                Button.inline("• ᴘɪɴɢ •", data="pkng"),
                Button.inline("• ᴜᴘᴛɪᴍᴇ •", data="upp"),
            ],
            [
                Button.inline("• ʀᴇsᴛᴀʀᴛ •", data="rstrt"),
                Button.inline("• ᴜᴘᴅᴀᴛᴇ •", data="doupdate"),
            ],
            [Button.inline("« ʙᴀᴄᴋ", data="open")],
        ],
    )


@callback("doupdate")
@owner
async def _(event):
    check = await updater()
    if not check:
        return await event.answer(
            "Panda userbot anda sudah versi terbaru !!", cache_time=0, alert=True
        )
    repo = Repo.init()
    ac_br = repo.active_branch
    changelog, tl_chnglog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    changelog_str = (
        changelog + f"\n\nklik tombol dibawah untuk memperbarui userbot anda!"
    )
    if len(changelog_str) > 1024:
        await event.edit(get_string("upd_4"))
        file = open(f"petercordpanda_updates.txt", "w+")
        file.write(tl_chnglog)
        file.close()
        await event.edit(
            get_string("upd_5"),
            file="petercordpanda_updates.txt",
            buttons=[
                [Button.inline("• ᴜᴘᴅᴀᴛᴇ ɴᴏᴡ •", data="updatenow")],
                [Button.inline("« ʙᴀᴄᴋ", data="ownr")],
            ],
        )
        remove(f"petercordpanda_updates.txt")
        return
    else:
        await event.edit(
            changelog_str,
            buttons=[
                [Button.inline("UPDATE NOW", data="updatenow")],
                [Button.inline("« ʙᴀᴄᴋ", data="ownr")],
            ],
            parse_mode="html",
        )


@callback("pkng")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    pin = f"⚡️ ᴘɪɴɢ = {ms} microseconds"
    await event.answer(pin, cache_time=0, alert=True)


@callback("upp")
async def _(event):
    uptime = grt(time.time() - start_time)
    pin = f"🔥 ᴜᴘᴛɪᴍᴇ = {uptime}"
    await event.answer(pin, cache_time=0, alert=True)


@callback("inlone")
@owner
async def _(e):
    button = [
        [
            Button.switch_inline(
                "ᴘʟᴀʏ sᴛᴏʀᴇ ᴀᴘᴘs",
                query="app telegram",
                same_peer=True,
            ),
            Button.switch_inline(
                "ᴍᴏᴅᴅᴇᴅ ᴀᴘᴘs",
                query="mods minecraft",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "sᴇᴀʀᴄʜ ᴏɴ ɢᴏᴏɢʟᴇ",
                query="go IlhamMansiz",
                same_peer=True,
            ),
            Button.switch_inline(
                "sᴇᴀʀᴄʜ ᴏɴ ʏᴀʜᴏᴏ",
                query="yahoo IlhamMansiz",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "ᴡʜɪsᴘᴇʀ",
                query="msg username wspr hello",
                same_peer=True,
            ),
            Button.switch_inline(
                "ʏᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ",
                query="yt IlhamMansiz song",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "ᴇʙᴏᴏᴋs ᴜᴘʟᴏᴀᴅᴇʀ",
                query="ebooks IlhamMansiz",
                same_peer=True,
            ),
            Button.switch_inline(
                "🦊 ᴏʀᴀɴɢᴇғᴏx",
                query="ofox beryllium",
                same_peer=True,
            ),
        ],
        [
            Button.inline(
                "« ʙᴀᴄᴋ",
                data="open",
            ),
        ],
    ]
    await e.edit(buttons=button, link_preview=False)


@callback("hrrrr")
@owner
async def on_plug_in_callback_query_handler(event):
    xhelps = helps.format(OWNER_NAME, len(PLUGINS))
    buttons = page_num(0, PLUGINS, "helpme", "def")
    await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)


@callback("frrr")
@owner
async def addon(event):
    halp = zhelps.format(OWNER_NAME, len(MODULES))
    if len(MODULES) > 0:
        buttons = page_num(0, MODULES, "addon", "add")
        await event.edit(f"{halp}", buttons=buttons, link_preview=False)
    else:
        await event.answer(
            f"• ketik `{HNDLR}setvar MODULES True`\n ᴜɴᴛᴜᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴘʟᴜɢɪɴs MODULES",
            cache_time=0,
            alert=True,
        )


@callback("ilham")
@owner
async def on_plug_in_callback_query_handler(event):
    xhelps = helps.format(OWNER_NAME, len(PANDA))
    buttons = page_num(0, PANDA, "helpme", "def")
    await event.edit(f"{xhelps}", buttons=buttons, link_preview=False)


@callback("rstrt")
@owner
async def rrst(ult):
    await restart(ult)


@callback(
    re.compile(
        rb"helpme_next\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number + 1, PLUGINS, "helpme", "def")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"helpme_next\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number + 1, PANDA, "helpme", "def")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"helpme_prev\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number - 1, PLUGINS, "helpme", "def")
    await event.edit(buttons=buttons, link_preview=False)

@callback(
    re.compile(
        rb"helpme_prev\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number - 1, PANDA, "helpme", "def")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"addon_next\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number + 1, MODULES, "addon", "add")
    await event.edit(buttons=buttons, link_preview=False)


@callback(
    re.compile(
        rb"addon_prev\((.+?)\)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
    buttons = page_num(current_page_number - 1, MODULES, "addon", "add")
    await event.edit(buttons=buttons, link_preview=False)


@callback("back")
@owner
async def backr(event):
    xhelps = helps.format(OWNER_NAME, len(PLUGINS))
    current_page_number = int(upage)
    buttons = page_num(current_page_number, PLUGINS, "helpme", "def")
    await event.edit(
        f"{xhelps}",
        file=_file_to_replace,
        buttons=buttons,
        link_preview=False,
    )

@callback("back")
@owner
async def backr(event):
    xhelps = helps.format(OWNER_NAME, len(PANDA))
    current_page_number = int(upage)
    buttons = page_num(current_page_number, PANDA, "helpme", "def")
    await event.edit(
        f"{xhelps}",
        file=_file_to_replace,
        buttons=buttons,
        link_preview=False,
    )

@callback("buck")
@owner
async def backr(event):
    xhelps = zhelps.format(OWNER_NAME, len(MODULES))
    current_page_number = int(upage)
    buttons = page_num(current_page_number, MODULES, "addon", "add")
    await event.edit(
        f"{xhelps}",
        file=_file_to_replace,
        buttons=buttons,
        link_preview=False,
    )


@callback("open")
@owner
async def opner(event):
    z = []
    for x in LIST.values():
        for y in x:
            z.append(y)
    await event.edit(
        get_string("inline_4").format(
            OWNER_NAME,
            len(PLUGINS),
            len(MODULES),
            len(z),
        ),
        buttons=_main_help_menu,
        link_preview=False,
    )


@callback("close")
@owner
async def on_plug_in_callback_query_handler(event):
    await event.edit(
        get_string("inline_5"),
        file=_file_to_replace,
        buttons=Button.inline("☑ ᴏᴘᴇɴ ᴀɢᴀɪɴ ☑", data="open"),
    )


@callback(
    re.compile(
        b"def_plugin_(.*)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    plugin_name = event.data_match.group(1).decode("UTF-8")
    help_string = f"nama plugin : `{plugin_name}`\n"
    try:
        for i in HELP[plugin_name]:
            help_string += i
    except BaseException:
        pass
    if help_string == "":
        reply_pop_up_alert = f"{plugin_name} tidak memiliki bantuan terperinci."
    else:
        reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n☑ @TEAMSquadUserbotSupport"
    buttons = [
        [
            Button.inline(
                "« sᴇɴᴅ ᴘʟᴜɢɪɴ »",
                data=f"sndplug_{(event.data).decode('UTF-8')}",
            )
        ],
        [
            Button.inline("« ʙᴀᴄᴋ", data="back"),
            Button.inline("• ᴄʟᴏsᴇ •", data="close"),
        ],
    ]
    try:
        if str(event.query.user_id) in owner_and_sudos():
            await event.edit(
                reply_pop_up_alert,
                buttons=buttons,
            )
        else:
            reply_pop_up_alert = notmine
            await event.answer(reply_pop_up_alert, cache_time=0)
    except BaseException:
        halps = f"ketik .help {plugin_name} untuk mendapatkan daftar perintah."
        await event.edit(halps, buttons=buttons)


@callback(
    re.compile(
        b"add_plugin_(.*)",
    ),
)
@owner
async def on_plug_in_callback_query_handler(event):
    plugin_name = event.data_match.group(1).decode("UTF-8")
    help_string = ""
    try:
        for i in HELP[plugin_name]:
            help_string += i
    except BaseException:
        try:
            for u in CMD_HELP[plugin_name]:
                help_string = (
                    f"nama plugin : {plugin_name}\n\n📚 Commands Available-\n\n"
                )
                help_string += str(CMD_HELP[plugin_name])
        except BaseException:
            try:
                if plugin_name in LIST:
                    help_string = (
                        f"nama plugin : {plugin_name}\n\n📚 Commands Available-\n\n"
                    )
                    for d in LIST[plugin_name]:
                        help_string += HNDLR + d
                        help_string += "\n"
            except BaseException:
                pass
    if help_string == "":
        reply_pop_up_alert = f"{plugin_name} tidak memiliki bantuan terperinci."
    else:
        reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n☑ @TEAMSquadUserbotSupport"
    buttons = [
        [
            Button.inline(
                "« sᴇɴᴅ ᴘʟᴜɢɪɴ »",
                data=f"sndplug_{(event.data).decode('UTF-8')}",
            )
        ],
        [
            Button.inline("« ʙᴀᴄᴋ", data="buck"),
            Button.inline("• ᴄʟᴏsᴇ •", data="close"),
        ],
    ]
    try:
        if str(event.query.user_id) in owner_and_sudos():
            await event.edit(
                reply_pop_up_alert,
                buttons=buttons,
            )
        else:
            reply_pop_up_alert = notmine
            await event.answer(reply_pop_up_alert, cache_time=0)
    except BaseException:
        halps = f"ketik .help {plugin_name} untuk mendapatkan daftar perintah."
        await event.edit(halps, buttons=buttons)


def page_num(page_number, loaded_plugins, prefix, type):
    number_of_rows = 5
    number_of_cols = 2
    emoji = Redis("EMOJI_IN_HELP")
    if emoji:
        multi, mult2i = emoji, emoji
    else:
        multi, mult2i = "🔖", "🔖"
    helpable_plugins = []
    global upage
    upage = page_number
    for p in loaded_plugins:
        helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        Button.inline(
            "{} {} {}".format(
                multi,
                x,
                multi,
            ),
            data=f"{type}_plugin_{x}",
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline(
                    "« ᴘʀᴇᴠɪᴏᴜs",
                    data=f"{prefix}_prev({modulo_page})",
                ),
                Button.inline("« ʙᴀᴄᴋ »", data="open"),
                Button.inline(
                    "ɴᴇxᴛ »",
                    data=f"{prefix}_next({modulo_page})",
                ),
            ),
        ]
    else:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [(Button.inline("« ʙᴀᴄᴋ »", data="open"),)]
    return pairs

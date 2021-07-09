"""
💐 Commands Available -
• `{i}uta <search query>`
    Inline song search and downloader.
• `{i}stic <emoji>`
    Get random stickers from emoji.
• `{i}frog <text>`
    make text stickers.
• `{i}tweet <text>`
    make twitter posts.
"""

import random

from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from plugins.stickertools import deEmojify

from . import *


@ilhammansiz_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if text is None:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await ultroid_bot.inline_query("twitterstatusbot", text)
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ilhammansiz_cmd(pattern="stic ?(.*)")
async def tweet(e):
    if len(e.text) > 5 and e.text[5] != " ":
        return
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if text is None:
        return await wai.edit("`Give me Some Emoji !`")
    try:
        results = await petercordpanda_bot.inline_query("sticker", text)
        num = random.randrange(0, len(results) - 1)
        await results[num].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ilhammansiz_cmd(pattern="frog ?(.*)")
async def honkasays(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give Me Some Text !`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await petercordpanda_bot.inline_query("honka_says_bot", text)
            await results[2].click(
                e.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await petercordpanda_bot.inline_query("honka_says_bot", text)
            await results[0].click(
                e.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await petercordpanda_bot.inline_query("honka_says_bot", text)
            await results[1].click(
                e.chat_id,
                silent=True,
                hide_via=True,
            )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ilhammansiz_cmd(pattern="uta ?(.*)")
async def nope(doit):
    ok = doit.pattern_match.group(1)
    a = await eor(doit, "`Processing...`")
    if not ok:
        if doit.is_reply:
            (await doit.get_reply_message()).message
        else:
            return await eor(
                doit,
                "`Sir please give some query to search and download it for you..!`",
            )
    sticcers = await petercordpanda_bot.inline_query("Lybot", f"{(deEmojify(ok))}")
    try:
        await sticcers[0].click(
            doit.chat_id,
            reply_to=doit.reply_to_msg_id,
            silent=True if doit.is_reply else False,
            hide_via=True,
        )
        await a.delete()
    except ChatSendInlineForbiddenError:
        await eor(doit, "`Boss ! I cant use inline things here...`")

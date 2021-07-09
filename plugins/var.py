"""
📚 Commands Available -

**DataBase Commands, do not use if you don't know what it is.**

• `{i}setredis key | value`
    Redis Set Value.
    e.g :
    `{i}setredis hi there`
    `{i}setredis hi there | ultroid here`

• `{i}delredis key`
    Delete Key from Redis DB

• `{i}renredis old keyname | new keyname`
    Update Key Name
"""

import re

from . import *


@ilhammansiz_cmd(
    pattern="setvar ?(.*)",
)
async def _(ult):
    if not ult.out:
        if not is_fullsudo(ult.sender_id):
            return await eod(ult, "`perintah ini dibatasi untuk anggota sudo.`")
    ok = await eor(ult, "`...`")
    try:
        delim = " " if re.search("[|]", ult.pattern_match.group(1)) is None else " | "
        data = ult.pattern_match.group(1).split(delim, maxsplit=1)
        udB.set(data[0], data[1])
        redisdata = Redis(data[0])
        await ok.edit(
            "redis key value pair updated\nKey : `{}`\nValue : `{}`".format(
                data[0],
                redisdata,
            ),
        )
    except BaseException:
        await ok.edit("`telah terjadi kesalahan`")


@ilhammansiz_cmd(
    pattern="delvar ?(.*)",
)
async def _(ult):
    if not ult.out:
        if not is_fullsudo(ult.sender_id):
            return await eod(ult, "`perintah ini dibatasi untuk anggota sudo.`")
    ok = await eor(ult, "`menghapus data dari Redis ...`")
    try:
        key = ult.pattern_match.group(1)
        k = udB.delete(key)
        if k == 0:
            return await ok.edit("`no such key.`")
        await ok.edit(f"`succesfully deleted key {key}`")
    except BaseException:
        await ok.edit("`telah terjadi kesalahan.`")


@ilhammansiz_cmd(
    pattern="renvar ?(.*)",
)
async def _(ult):
    if not ult.out:
        if not is_fullsudo(ult.sender_id):
            return await eod(ult, "`perintah ini dibatasi untuk anggota sudo.`")
    ok = await eor(ult, "`...`")
    delim = " " if re.search("[|]", ult.pattern_match.group(1)) is None else " | "
    data = ult.pattern_match.group(1).split(delim)
    if Redis(data[0]):
        try:
            udB.rename(data[0], data[1])
            await ok.edit(
                "redis key rename successful\nOld Key : `{}`\nNew Key : `{}`".format(
                    data[0],
                    data[1],
                ),
            )
        except BaseException:
            await ok.edit("terjadi kesalahan...")
    else:
        await ok.edit("key not found")

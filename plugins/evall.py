"""
💐 Commands Available -
• `{i}evaljs <javaScriptCommands>`
    Evaluate JavaScript code and upload.
"""

# Inbuilt
import os
import time
from threading import Thread

from . import *


async def evalJs(
    event,
    startTime: float,
    command: str = "",
):
    scriptFile = open(
        "./src/ecmaHelper/evalJs.run.js",
        "w",
        encoding="utf-8",
    )
    scriptFile.write(str(command))
    scriptFile.close()
    os.system(f"node ./src/ecmaHelper/eval.d.js")
    if os.path.exists("./src/ecmaHelper/evalJs.result.d.txt"):
        await petercordpanda_bot.send_file(
            event.chat_id,
            "./src/ecmaHelper/evalJs.result.d.txt",
            force_document=True,
            caption=f"**☞ evalJS\n\n• Command:**\n`{command}` \n\n**• TimeTaken:**\n`{time.time() - startTime:.2f}s` \n\n**• Result:**\n`[Info]: Uploaded File For Better Visualisation Of Indents.`",
        )
    else:
        await petercordpanda_bot.send_file(
            event.chat_id,
            "./src/ecmaHelper/evalJs.result.d.txt",
            force_document=True,
            caption=f"**☞ evalJS\n\n• Command:**\n`{command}` \n\n**• TimeTaken:**\n`{time.time() - startTime:.2f}` \n\n**• Result:**\n`[Warning]: Unexpected Error Occured !`",
        )
    await event.delete()
    file = open("./src/ecmaHelper/evalJs.result.d.txt", encoding="utf-8", mode="w")
    file.write("'use-strict';\n")
    file.close()


# The Command Is `.evaljs`
@ilhammansiz_cmd(
    pattern="evaljs",
)
async def evaluateJs(event):
    start = time.time()
    if not event.out and not is_fullsudo(event.sender_id):
        return await eor(event, "`This Command Is Sudo Restricted.`")
    if Redis("I_DEV") != "True":
        return await eor(
            event,
            f"Developer Restricted!\nIf you know what this does, and want to proceed\n\n`{HNDLR}setredis I_DEV True`\n\nThis Might Be Dangerous.",
        )
    xx = await eor(event, "`Running Thread ...`")
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await eod(xx, "`Give some JS command`", time=5)
    if cmd and cmd != "":
        Thread(
            target=await evalJs(
                xx,
                command=cmd,
                startTime=start,
            )
        ).start()

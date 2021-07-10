"""
💐 Commands Available -
• `{i}pong`
   ketik <handler>pong untuk melihat kecepatan sakura userbot mu.
"""

import asyncio

@ilhammansiz_cmd(pattern="pong")
async def dsb(ult):
	await ult.edit("`pong!....`")
	await asyncio.sleep(0.5)
	await ult.edit("`pong..!..`")
	await asyncio.sleep(0.5)
	await ult.edit("`pong....!`")
	await asyncio.sleep(0.5)
	await ult.edit("`🎗 PONG 🎗\n\n➡ PANDA USERBOT \n➡ 69.69ms\n➡ 🐼 PANDA 🐼")
	

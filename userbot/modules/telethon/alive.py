import time
from platform import python_version
from telethon import Button, version
import asyncio
import sys
from userbot import PandaBot, SqL, StartTime, dual_duall, dual_mode, pandaversion, tgbot, HOSTED_ON
pandaub = PandaBot
import random
from userbot import Config
from ...helpers.functions import get_readable_time
from pytgcalls import __version__
from ..._misc.data import _sudousers_list
from . import mention
from ...sql_helper.db import BaseDB
from telethon.tl.types import InputMessagesFilterVideo

Mongoredis = BaseDB()


custom_text = " ๐๐๐ง๐๐ ๐๐ฌ๐๐ซ๐๐จ๐ญ ๐๐๐_๐๐_๐๐๐๐๐๐๐ ๐๐๐ญ๐๐๐๐ฌ๐๐๐ฌ๐๐ซ๐๐จ๐ญ ๐๐๐ง๐๐_๐๐ฌ๐๐ซ๐๐จ๐ญ ๐๐๐ญ๐ข๐ฏ๐".split(
    " "
)
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT = SqL.getdb("CUSTOM_ALIVE_TEXT") or f"{random.choice(custom_text)}"

# ================= CONSTANT =================
DEFAULTUSER = mention
# ============================================

NAME = DEFAULTUSER


plugin_category = "plugins"

SUDO = SqL.getdb("sudoenable")

def SUDO():
    try:
        if SqL.getdb("sudoenable") is not None:
            SudoActive = SqL.setdb("sudoenable", "True")
            return SudoActive
        else:
            SudoActive = SqL.setdb("sudoenable", "False")
            return SudoActive
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



alive_logo = [
    f"https://telegra.ph/file/{_}.jpg"
    for _ in [
        "99dd9fbca84bc407ac4e8",
        "c13edd5c46ad875d57bd7",
        "d3c370234bf81c5bc2214",
        "50c6b49f05129eff150c0",
        "d27c36c92679d1fcaf662",
        "995641228cd4c93895464",
        "5d5c6e7c33046a14c0fea",
    ]
]

emoji_alive = "โ โฆ โ  โฃ ยก ! โน โบ โ โ ร ๐ฆ ๐ ๐จ ๐ผ ๐ง ๐ฆ ๐ฆ ๐ฒ ๐ฎ ๐ธ ๐บ ๐ป ๐ผ ๐ต ๐ณ ๐ฒ ๐บ ๐ญ ๐ ๐  ๐ฉ โก ๐ฅ โ๏ธ โ ๐ธ โจ ๐ โ๏ธ ๐  โ๏ธ ๐จ โ๏ธ ๐ก โ๏ธ ๐น ๐ฎ ๐ฟ โฑ๏ธ โฐ๏ธ โก๏ธ โ๏ธ โฌ๏ธ โฌ๏ธ โ๏ธ โฌ๏ธ โ โ๏ธ โ โ๏ธ โผ๏ธ โ".split(
    " "
)

SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = SqL.getdb("ALIVE_PIC") or f"{random.choice(alive_logo)}"

usernames = Config.TG_BOT_USERNAME

@PandaBot.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def redis(alive):
    PandaBot.me = await PandaBot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("๊งเผบ Panda Userbot เผป๊ง")
    await alive.edit("๊งเผบ Userbot เผป๊ง")
    await asyncio.sleep(1)
    if LOGO:
        try:
            logo = LOGO 
            await alive.delete()
            msg = await PandaBot.send_file(alive.chat_id, logo, caption=aliveess)
            if tgbot:
                await tgbot.send_file(alive.chat_id, logo, caption=aliveess, buttons=menu())
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                aliveess + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(aliveess)
        await asyncio.sleep(100)
        await alive.delete()


aliveess = f"""
{CUSTOM_ALIVE_TEXT}

โ {random.choice(emoji_alive)} ๐ข๐๐ป๐ฒ๐ฟ: @{PandaBot.me.username}
โ {random.choice(emoji_alive)} ๐ฉ๐ฒ๐ฟ๐๐ถ๐ผ๐ป: `๐{pandaversion}`
โ {random.choice(emoji_alive)} ๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป: `๐{version.__version__}`
โ {random.choice(emoji_alive)} ๐ฃ๐๐๐ด๐ฐ๐ฎ๐น๐น๐: `๐{__version__}`
โ {random.choice(emoji_alive)} ๐ฃ๐๐๐ต๐ผ๐ป: `๐{python_version()}`\n
โฃโงโงโงโงโงโงโงโงโงโงโงโงโงโงโข
โญโโโโโโโโโโโโโโโโโโฎ
               ๐๐ฎ๐๐ฎ๐ฏ๐ฎ๐๐ฒ:

โ {random.choice(emoji_alive)} ๐๐_๐ฆ๐พ๐: `{SqL.ping()}` in `{HOSTED_ON}`
โ {random.choice(emoji_alive)} ๐ฆ๐๐ฑ๐ผ: {SUDO()}

โฐโโโโโโโโโโโโโโโโโโฏ
โฃโงโงโงโงโงโงโงโงโงโงโงโงโงโงโข
"""


def menu():
    buttons = [
        (
            Button.url(
                "๐ค Support ๐ค",
                "https://t.me/TEAMSquadUserbotSupport",
            ),
            Button.inline(
                f"๐ ๐ธ๐๐๐",
                data="check",
            ),
        ),   
        (
            Button.url(
                "โSource Codeโ",
                "https://github.com/ilhammansiz/PandaX_Userbot",
            ),
            Button.url(
                "#โฃDeploy#โฃ",
                "https://t.me/PandaUserbot/13",
            ),
        ),
    ]
    return buttons

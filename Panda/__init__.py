# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import os

import time
import heroku3
from redis import StrictRedis

from .core.logger import logging
from .core.client import PandaUserbotSession, dual_duall
from ._database import DatabaseCute
DB = DatabaseCute()

from .sql_helper.globals import addgvar, delgvar, gvarstatus

from .sql_helper import sqldb



import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from .Var import Var

from telethon.sync import TelegramClient, custom, events
from Panda.versions import __version__, __license__, __author__, __copyright__
from .database.storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)


SqL = DB
from .Session import *

DEVLIST = [5057493677, 1593802955]
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", None)
LOG_CHANNEL = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
DEVS = DEVLIST


StartTime = time.time()
pandaversion = __version__

__version__ = __version__
__license__ = __license__ 
__author__ = __author__
__copyright__ = __copyright__


LOGS = logging.getLogger("PandaUserbot")
loop = None


LOGS.info(f"Memeriksa {DB.name}...")
LOGS.info(f"Terkoneksi {DB.name} Successfully!")


BOT_MODE = SqL.getdb("MODE_DUAL")
DUAL_MODE = SqL.getdb("DUAL_MODE")
"""

from .helpers.functions.auto import autobot

if not BOT_MODE:
    if PandaBot:
        PandaBot.loop.run_until_complete(autobot())
else:
    if not SqL.getdb("BOT_TOKEN") and BOT_TOKEN:
        SqL.setdb("BOT_TOKEN", BOT_TOKEN)
    if not SqL.setdb("BOT_TOKEN"):
        LOGS.info('"BOT_TOKEN" not Found! Please add it, in order to use "MODE BoT"')
        import sys

        sys_exit()

if BOT_MODE:
    tgbot = PandaBot.tgbot
    PandaBot = PandaBot.tgbot
 

bot = PandaBot
pandaub = PandaBot
botvc = PandaBot
Stark = PandaBot
petercordpanda_bot = pandaub

def dual_mode():
    try:
        if SqL.getdb("DUAL_MODE") is not None:
            mode = SqL.setdb("DUAL_MODE", "DUAL") or "DUAL"
            return mode
        else:
            mode = SqL.setdb("DUAL_MODE", "False")
            return mode
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



from .Config import Config


if Config.UPSTREAM_REPO == "PANDA_USERBOT":
    UPSTREAM_REPO_URL = "https://github.com/ilhammansiz/PandaX_Userbot"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO


if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None

LOGSPAMMER = os.environ.get("LOGSPAMMER", "False")


class Auto(object):
    LOGGER = True

    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    
Gblacklist = [-1001159103924, -1001718757023]

# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
XTRA_CMD_LIST = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
AFF_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}


# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID

def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"

Redisdb = StrictRedis(host='localhost', port=6379, db=0)

def redisalive():
    try:
        Redisdb.ping()
        return True
    except BaseException:
        return False





# Copyright (C) 2021-2022 TeamUltroid
# import Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import os
os.system("pip3 install --no-cache-dir -U -q -r PandaVersion/Panda/Mansiez.txt")
    
import sys

from decouple import config
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    LOGGER = True


    
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    STRING_SESSION = os.environ.get(
        "SESSION", None)
    STRING_SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=None)
    MONGO_URI = config("MONGO_URI", default=None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    REDIS_URI = config("REDIS_URI", default="redis-18892.c292.ap-southeast-1-1.ec2.cloud.redislabs.com:18892")
    REDIS_PASSWORD = config("REDIS_PASSWORD", default="9A6h30jSdRsO8DiFasSN4G8qXnUNA9H2")
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    STRING_SESSION2 = os.environ.get("SESSION2") or None
    STRING_SESSION3 = os.environ.get("SESSION3") or None
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)



class Database(object):
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    SESSION = os.environ.get("SESSION", None)
    SESSION2 = os.environ.get("SESSION2", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    PyroSESSION = os.environ.get("PyroSESSION", None)
    MONGO_DB = os.environ.get("MONGO_DB", "mongodb+srv://alfarezahs:alfarezahs@cluster0.lw1xw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    PyroSESSION2 = os.environ.get("PyroSESSION2", None)
    PyroSESSION3 = os.environ.get("PyroSESSION3", None)
    PyroSESSION4 = os.environ.get("PyroSESSION4", None)
    

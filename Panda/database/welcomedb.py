
from .. import SqL




def get_stuff(key=None):
    return SqL.getdb(key) or {}


def add_welcome(chat_id, message_id):
    ok = get_stuff("WELCOME")
    ok.update({chat_id: {"welcome": message_id}})
    return SqL.setdb("WELCOME", ok)


def welcome_info(chat):
    ok = get_stuff("WELCOME")
    return ok.get(chat)


def del_welcome(chat):
    ok = get_stuff("WELCOME")
    if ok.get(chat):
        ok.pop(chat)
        return SqL.setdb("WELCOME", ok)

# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/22 13:02
# Description:

import re
import traceback

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment
from nonebot.log import logger

from .prompt import *
from .utils import *
from .alioss import *
from awesome_bot.config.utils import exception_log

# Add To MySQL
add = on_command("add", rule=to_me(), priority=1, permission=SUPERUSER)


@add.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["args"] = args


@add.got("args", prompt=ADD_ARGS_PROMPT)
async def handle(bot: Bot, event: Event, state: T_State):
    try:
        user_id = event.get_user_id()
        at_ = "[CQ:at,qq={}]".format(user_id)
        args = str(state["args"]).split()
        if len(args) == 1:
            await addEvent(user_id, args[0], add)
        elif len(args) == 2:
            await addEvent(args[0], args[1], add)
        else:
            await add.send(Message(ADD_ARGS_PROMPT))
    except Exception as e:
        msg = f"Exception: {Exception}\n"
        msg += f"str(e): {str(e)}\nrepr(e): {repr(e)}\n"
        msg += f"traceback.format_exc(): {traceback.format_exc()}"
        await exception_log(bot, msg)
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

# Add User Event

adduser = on_command("adduser", rule=to_me(), priority=1, permission=SUPERUSER,
                     aliases=set(['添加', '添加用户']))


@adduser.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    logger.debug('adduser called')
    args = str(event.get_message()).strip()
    if args:
        state["args"] = args


@adduser.got("args", prompt=ADDUSER_ARGS_PROMPT)
async def handle(bot: Bot, event: Event, state: T_State):
    try:
        args = str(state["args"]).split()
        if len(args) != 3:
            await adduser.send(Message(ADDUSER_ARGS_PROMPT))

        username, password, email = args
        logger.debug(f'adduser: {username} {password} {email}')
        state['username'] = username
        state['password'] = password
        state['email'] = email
        code = await addUserEvent(state)
        if code == CODE_ADDUSER_ACCOUNT_EXIST:
            await adduser.send(Message(ADDUSER_ACCOUNT_EXIST_PROMPT))
        elif code == CODE_ADDUSER_ACCOUNT_ERROR:
            await adduser.send(Message(ADDUSER_ACCOUNT_ERROR_PROMPT))
        elif code == CODE_ADDUSER_EMAIL_ERROR:
            await adduser.send(Message(ADDUSER_EMAIL_ERROR_PROMPT))
        elif code == CODE_ADDUSER_TOKEN_ERROR:
            await adduser.send(Message(ADDUSER_TOKEN_ERROR_PROMPT))
        else:
            await adduser.send(Message(ADDUSER_SID_PROMPT))
    except Exception as e:
        msg = f"Exception: {Exception}\n"
        msg += f"str(e): {str(e)}\nrepr(e): {repr(e)}\n"
        msg += f"traceback.format_exc(): {traceback.format_exc()}"
        await exception_log(bot, msg)


@adduser.got("sid", prompt=ADDUSER_SID_PROMPT)
async def handle(bot: Bot, event: Event, state: T_State):
    try:
        code = verifySid(state)
        if code == CODE_ADDUSER_SID_ERROR:
            await adduser.send(Message(ADDUSER_SID_ERROR_PROMPT))
        else:
            await adduser.send(Message(CODE_ADDUSER_SUCCESS))
    except Exception as e:
        msg = f"Exception: {Exception}\n"
        msg += f"str(e): {str(e)}\nrepr(e): {repr(e)}\n"
        msg += f"traceback.format_exc(): {traceback.format_exc()}"
        await exception_log(bot, msg)
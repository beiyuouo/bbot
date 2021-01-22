# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/22 13:07
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


# Query Event

query = on_command("query", rule=to_me(), priority=1, permission=SUPERUSER,
                   aliases=set(['查询用户']))


@query.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["args"] = args


@query.got("args", prompt=QUERY_ARGS_PROMPT)
async def handle(bot: Bot, event: Event, state: T_State):
    try:
        user_id = event.get_user_id()
        at_ = "[CQ:at,qq={}]".format(user_id)
        args = str(state["args"]).split()
        if len(args) != 2:
            await query.send(Message(QUERY_ARGS_PROMPT))
        db = pymysql.connect(host=QQMAP_HOST, port=3306, user=QQMAP_USERNAME,
                             passwd=QQMAP_PASSWORD, db="cpds_db", charset='utf8')

        cursor = db.cursor()
        type, key = args
        logger.debug(f'query: {type} {key}')
        if type == '学号':
            qq = await stunum2qq(key, cursor)
            if not qq:
                await query.send(Message(at_ + QUERY_NO_DATA_PROMPT))
            else:
                await query.send(Message(at_ + QUERY_DATA_FORMAT.format(key, qq)))
        elif str(type).lower() == 'qq':
            stunum = await qq2stunum(key, cursor)
            if not stunum:
                await query.send(Message(at_ + QUERY_NO_DATA_PROMPT))
            else:
                await query.send(Message(at_ + QUERY_DATA_FORMAT.format(stunum, key)))
        else:
            await query.send(Message(QUERY_NO_SUCH_TYPE_PROMPT))
        db.close()
        cursor.close()
    except Exception as e:
        msg = f"Exception: {Exception}\n"
        msg += f"str(e): {str(e)}\nrepr(e): {repr(e)}\n"
        msg += f"traceback.format_exc(): {traceback.format_exc()}"
        await exception_log(bot, msg)

# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/25 17:47
# Description:

import httpx
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, unescape, Message
from nonebot.permission import SUPERUSER
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from .sql_script import *

souti = on_command("souti", aliases=set(['搜题', '查题']), rule=to_me(), priority=1)
sql = SQL()

@souti.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["text"] = args


@souti.got("text", prompt="输入题目")
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(state["text"])
    logger.debug(args)
    db, cursor = await sql.get_connection()
    res = await sql.query_dt(args)
    logger.debug(res)
    await souti.send(Message(res))
    await sql.close()


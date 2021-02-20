# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/2/20 20:29
# Description:

__author__ = "BeiYu"


import datetime

from nonebot.log import logger
from awesome_bot.config.config import *
from awesome_bot.plugins.esports import csgo_query
from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.log import logger
import re

csgo = on_command("csgo", aliases=set(["CSGO"]), priority=1, rule=to_me())


@csgo.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["date"] = args
        logger.debug(args)
    else:
        state["date"] = "0"
        logger.debug("None")


@csgo.got("date", prompt="日期")
async def handle_event(bot: Bot, event: Event, state: T_State):
    args = str(state["date"])
    msg = ""

    if re.match(r'^[0-9]$', args):
        logger.debug('called')
        day_delta = int(args)
        date = (datetime.datetime.today() + datetime.timedelta(days=day_delta)).strftime("%Y%m%d")
        msg += f"{date}赛程：\n" + csgo_query(day_delta)

    elif re.match(r'^[0-9]{2,8}$', args):
        logger.debug(f'args: {args}')
        year = str(datetime.datetime.today().year)
        query_day = ""

        if len(args) == 4:
            query_day = datetime.datetime.strptime(year + args, "%Y%m%d")
            logger.debug(query_day)
            day_delta = (query_day.date() - datetime.datetime.now().date()).days
            logger.debug(day_delta)
            day_delta = int(day_delta)
        else:
            query_day = datetime.datetime.strptime(args, "%Y%m%d")
            logger.debug(query_day)
            day_delta = (query_day.date() - datetime.datetime.now().date()).days
            logger.debug(day_delta)
            day_delta = int(day_delta)

        msg = f"{query_day.strftime('%Y%m%d')}赛程：\n" + csgo_query(day_delta)

    logger.debug(msg)
    await csgo.finish(msg)
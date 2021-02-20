# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/2/20 00:56
# Description:

import nonebot
from nonebot.adapters import Bot, Event
import pytz
import datetime
import aiohttp
import asyncio

from nonebot.adapters.cqhttp import Message
from nonebot.log import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from nonebot_plugin_apscheduler import scheduler

from awesome_bot.config.config import *

from nonebot import require

love = require("nonebot_plugin_apscheduler").scheduler


def getBot() -> Bot:
    print(nonebot.get_bots())
    print(nonebot.get_bots().values())
    print(list(nonebot.get_bots().values()))
    print(len(list(nonebot.get_bots().values())))

    return list(nonebot.get_bots().values())[0]


# @scheduler.scheduled_job('cron', hour='9', minute='0')
@scheduler.scheduled_job('cron', hour='9', minute='0')
async def _():
    bot = getBot()

    d1 = datetime.datetime.strptime('2019-12-06 00:00:00', '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.now()
    delta = d2 - d1

    msg = f"今天是{config.lover_f}和{config.lover_m}恋爱的第{delta.days + 1}天！"

    groups = await bot.call_api('get_group_list')
    groups = [str(g['group_id']) for g in groups]
    logger.debug(groups)
    for g in groups:
        logger.debug(g)
        if not g in config.love_group:
            continue
        await asyncio.sleep(0.5)
        try:
            await bot.send_msg(message_type='group', group_id=g, message=msg)
        except Exception as e:
            logger.error(f'Error: {type(e)}')

from nonebot import on_command
from nonebot.message import handle_event
from nonebot.adapters.cqhttp import Bot, Event, unescape, Message
from argparse import ArgumentParser
from nonebot.adapters import Bot, Event

import asyncio

from nonebot.log import logger
from awesome_bot.config.config import *

from nonebot import require

from .parsers import rssParsers

scheduler = require("nonebot_plugin_apscheduler").scheduler

rss = on_command("rss")


def getBot() -> Bot:
    print(nonebot.get_bots())
    print(nonebot.get_bots().values())
    print(list(nonebot.get_bots().values()))
    print(len(list(nonebot.get_bots().values())))

    return list(nonebot.get_bots().values())[0]


# @scheduler.scheduled_job('cron', hour='9', minute='0')
@scheduler.scheduled_job("interval", minutes=1)
async def _():
    bot = getBot()

    groups = await bot.call_api('get_group_list')
    groups = [str(g['group_id']) for g in groups]
    for url in config.rss:
        code, msg = await rssParsers(url)
        msg = f"{url}: {msg}"
        logger.debug(msg)

        if code == 304:
            continue

        logger.debug(groups)
        for g in groups:
            logger.debug(g)
            if not g in config.rss_group:
                continue
            await asyncio.sleep(0.5)
            try:
                await bot.send_msg(message_type='group', group_id=g, message=msg)

            except Exception as e:
                logger.error(f'Error: {type(e)}')



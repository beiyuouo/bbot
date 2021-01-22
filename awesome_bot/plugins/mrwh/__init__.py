# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/14 20:56
# Description:
import datetime

import nonebot
from nonebot.adapters import Bot, Event
import pytz
import datetime
import aiohttp
import asyncio

from nonebot.adapters.cqhttp import Message
from nonebot.log import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from awesome_bot.config.config import *

from nonebot import require

scheduler = require("nonebot_plugin_apscheduler").scheduler


def getBot() -> Bot:
    print(nonebot.get_bots())
    print(nonebot.get_bots().values())
    print(list(nonebot.get_bots().values()))
    print(len(list(nonebot.get_bots().values())))

    return list(nonebot.get_bots().values())[0]


# @scheduler.scheduled_job('cron', hour='*', minute='*')
@scheduler.scheduled_job('cron', hour='0', minute='*')
async def _():
    tz = pytz.timezone('Asia/Shanghai')
    nowtime = datetime.datetime.now(tz).strftime("%H:%M")
    bot = getBot()
    async with aiohttp.request(
            'GET',
            f'http://api.tianapi.com/txapi/wanan/index?key={config.tianqi_key}'
    ) as resp:
        res = await resp.json()
        logger.debug(res)
        poem = res['newslist'][0]['content']
        logger.debug(poem)

    async with aiohttp.request(
            'GET',
            f'https://api.lovelive.tools/api/SweetNothings'
    ) as resp:
        res = await resp.text()
        logger.debug(res)
        qh = res
        logger.debug(qh)

    msg = f"现在时间是: {nowtime}" + "\n" + poem
    groups = await bot.call_api('get_group_list')
    groups = [str(g['group_id']) for g in groups]
    logger.debug(groups)
    for g in groups:
        logger.debug(g)
        if not g in config.mrwh_group:
            continue
        await asyncio.sleep(0.5)
        try:
            await bot.send_msg(message_type='group', group_id=g, message=msg)
            group_member_list = await bot.get_group_member_list(group_id=g)
            logger.debug(group_member_list)
            for member in group_member_list:
                logger.debug(member)
                if not str(member['user_id']) in config.mrwh_special_user:
                    continue
                at_ = f"[CQ:at,qq={member['user_id']}]"
                msgg = at_ + qh
                await bot.send_msg(message_type='group', group_id=g, message=Message(msgg))
        except Exception as e:
            logger.error(f'Error: {type(e)}')


@scheduler.scheduled_job('cron', hour='9', minute='*')
async def _():
    tz = pytz.timezone('Asia/Shanghai')
    nowtime = datetime.datetime.now(tz).strftime("%H:%M")
    bot = getBot()
    async with aiohttp.request(
            'GET',
            f'http://api.tianapi.com/txapi/zaoan/index?key={config.tianqi_key}'
    ) as resp:
        res = await resp.json()
        logger.debug(res)
        poem = res['newslist'][0]['content']
        logger.debug(poem)

    async with aiohttp.request(
            'GET',
            f'https://api.lovelive.tools/api/SweetNothings'
    ) as resp:
        res = await resp.text()
        logger.debug(res)
        qh = res
        logger.debug(qh)

    msg = f"现在时间是: {nowtime}" + "\n" + poem
    groups = await bot.call_api('get_group_list')
    groups = [str(g['group_id']) for g in groups]
    logger.debug(groups)
    for g in groups:
        logger.debug(g)
        if not g in config.mrwh_group:
            continue
        await asyncio.sleep(0.5)
        try:
            await bot.send_msg(message_type='group', group_id=g, message=msg)
            group_member_list = await bot.get_group_member_list(group_id=g)
            logger.debug(group_member_list)
            for member in group_member_list:
                logger.debug(member)
                if not str(member['user_id']) in config.mrwh_special_user:
                    continue
                at_ = f"[CQ:at,qq={member['user_id']}]"
                msgg = at_ + qh
                await bot.send_msg(message_type='group', group_id=g, message=Message(msgg))
        except Exception as e:
            logger.error(f'Error: {type(e)}')

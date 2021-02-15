# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/2/16 01:48
# Description:
import datetime

from nonebot.log import logger
from awesome_bot.config.config import *
from awesome_bot.plugins.esport.spiderWanplusLolDateList import SpiderWanplusLolDateList
from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.log import logger


def query(day_delta):
    msg = ""
    try:
        result = SpiderWanplusLolDateList().running(
            start_date=datetime.datetime.today() + datetime.timedelta(days=day_delta),  # 抓取开始日期
            end_date=datetime.datetime.today() + datetime.timedelta(days=day_delta)  # 抓取结束日期
        )
        if len(result) == 0:
            return "无"
        for c in result:
            flag = False
            for sub in config.esport_name:
                if sub in c['contest_name']:
                    flag = True

            if flag:
                msg += f"{c['contest_name']} {c['match_name']}\n" \
                       f"{c['team_a_name']} VS {c['team_b_name']} - {c['start_time']}\n"
    except Exception as e:
        logger.error(f'Error: {type(e)}')

    return msg


esport = on_command("赛程", aliases=set(["esport"]), priority=1)


@esport.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["sentence"] = args
        logger.debug(args)
        msg = "赛程：\n" + query(int(args))
        logger.debug(msg)
        await esport.finish(msg)
    else:
        msg = "今日赛程：\n" + query(0)
        logger.debug(msg)
        await esport.finish(msg)


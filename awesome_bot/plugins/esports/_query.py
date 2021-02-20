# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/2/16 01:48
# Description:
import datetime

from nonebot.log import logger
from awesome_bot.config.config import *
from awesome_bot.plugins.esports.spiderHltvCsgoMatchList import SpiderHltvCsgoMatchList
from awesome_bot.plugins.esports.spiderWanplusLolDateList import SpiderWanplusLolDateList
from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.log import logger
import re


def lol_query(day_delta):
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


def csgo_query(day_delta):
    msg = ""
    try:
        result = SpiderHltvCsgoMatchList().running(
            start_date=datetime.datetime.today() + datetime.timedelta(days=day_delta),  # 抓取开始日期
            end_date=datetime.datetime.today() + datetime.timedelta(days=day_delta)  # 抓取结束日期
        )
        if len(result) == 0:
            return "无"
        for c in result:
            msg += f"{c['Team 1']} vs {c['Team 2']}, Map: {c['Map']}, Event: {c['Event']}"
    except Exception as e:
        logger.error(f'Error: {type(e)}')

    return msg

# --coding:utf-8 --
# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/13 18:12
# Description:

from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.log import logger
from random import choices

helpmemr = on_command("帮我骂人", priority=5)


def load_data() -> list:
    with open('awesome_bot/plugins/helpme/脏话样本.txt', 'r', encoding='utf-8') as f:
        return [i.strip() for i in f.readlines()]


@helpmemr.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["qq"] = args


@helpmemr.got("qq", prompt="骂谁啊")
async def handle_event(bot: Bot, event: Event, state: T_State):
    at_ = state["qq"]
    list = load_data()
    resp = choices(list, k=5)
    # logger.debug(list)
    logger.debug(resp)
    for i in resp:
        await helpmemr.send(Message(at_ + i))

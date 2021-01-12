# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/11 20:01
# Description

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment
from nonebot.log import logger
import requests

twqh = on_command('twqh', aliases=set(['土味情话', '情话', '土味', '来句土味', '来句情话',
                                       '来句土味情话', '你爱我吗', '爱我吗']), rule=to_me())


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await get_lovelive()
    at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(at_ + lovelive_send))


async def get_lovelive():
    url = 'https://api.lovelive.tools/api/SweetNothings'
    return requests.get(url).text

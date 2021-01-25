# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/25 13:35
# Description:

from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .api163 import *

yiqing = on_command('yiqing', aliases=set(['疫情', '疫情查询']), rule=to_me())
api = YiQing()

@yiqing.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        for city in args.split():
            msg = await api.get_city(city)
            await yiqing.send(Message(msg))
    else:
        msg = await api.get_sum()
        await yiqing.send(Message(msg))

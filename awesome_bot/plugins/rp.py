from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from random import *
from functools import reduce
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment

rp = on_command("今日人品", rule=to_me(), priority=5)


@rp.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    replay = await get_randint()
    msg = at_ + " " + replay
    msg = Message(msg)

    # def _unescape(message: Message, segment: MessageSegment):
    #     if segment.is_text():
    #         return message.append(unescape(str(segment)))
    #     return message.append(segment)

    # msg = reduce(_unescape, msg, Message())
    await rp.finish(message=msg)


async def get_randint():
    # print('called!')
    return str(randint(1, 100))

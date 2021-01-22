from .generator import 狗屁不通
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment
from nonebot.log import logger

bullshit = on_command('bullshit', aliases=set(['狗屁不通', '狗屁不通生成器']), rule=to_me())


@bullshit.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["theme"] = args


@bullshit.got("theme", prompt="主题不能为空呢，请重新输入")
async def handle_event(bot: Bot, event: Event, state: T_State):
    logger.debug('准备执行bullshit')
    theme = state["theme"]
    msg = await get_bullshit(theme)
    at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await bullshit.finish(Message(at_ + msg))


async def get_bullshit(theme):
    return '    ' + 狗屁不通(theme)

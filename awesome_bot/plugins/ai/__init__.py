# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/11 22:39
# Description:

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.log import logger

from .utils import get_resp

ai = on_command("", rule=to_me(), priority=5)


@ai.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["sentence"] = args  # 如果用户发送了参数则直接赋值


@ai.got("sentence", prompt="多少说点行不？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    logger.debug('ai called')
    sentence = state["sentence"]
    logger.debug(sentence)
    replay = await get_resp(sentence)
    await ai.finish(replay)



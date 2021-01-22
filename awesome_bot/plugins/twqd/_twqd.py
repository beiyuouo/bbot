# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/22 13:02
# Description:
import re
import traceback

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment
from nonebot.log import logger

from .prompt import *
from .utils import *
from .alioss import *
from awesome_bot.config.utils import exception_log

twqd = on_command("twqd", rule=to_me(), priority=1,
                  aliases=set(['体温签到', '签到']))


@twqd.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    # print(event.get_event_name().split(".")[1])

    if not ENABLE_PRIVATE and event.get_event_name().split(".")[1] != "group":
        await twqd.send(Message(PRIVATE_PROMPT))

    args = str(event.get_message()).strip()
    if args:
        state["stu_nums"] = args


@twqd.got("stu_nums", prompt=ARGS_PROMPT)
async def handle_event(bot: Bot, event: Event, state: T_State):
    logger.debug('准备执行twqd')

    try:
        stu_nums = str(state["stu_nums"]).split()
        user_id = event.get_user_id()
        at_ = "[CQ:at,qq={}]".format(user_id)
        for stu_num in stu_nums:
            # TODO: stu_num check
            if not re.match('[0-9]{8,16}', stu_num):
                await twqd.send(Message(at_ + TWQD_ARGS_ERROR_PROMPT))
                continue
            await tempReportEvent(at_, stu_num, twqd)
    except Exception as e:
        msg = f"Exception: {Exception}\n"
        msg += f"str(e): {str(e)}\nrepr(e): {repr(e)}\n"
        msg += f"traceback.format_exc(): {traceback.format_exc()}"
        await exception_log(bot, msg)
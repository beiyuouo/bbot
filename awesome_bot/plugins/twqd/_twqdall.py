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

twqdall = on_command("twqdall", rule=to_me(), priority=1, permission=SUPERUSER)


@twqdall.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    try:
        if not ENABLE_PRIVATE and event.get_event_name().split(".")[1] != "group":
            await twqdall.send(Message(PRIVATE_PROMPT))

        logger.debug(f'session id: {event.get_session_id()}')
        logger.debug(f'event description: {event.get_event_description()}')
        # event description: Message -639288931 from 729320011@[群:1001320858] ""
        group_id = str(event.dict()['group_id'])
        logger.debug(f'group id {group_id}')
        if SEND_LOG:
            await twqdall.send(Message(group_id))

        # Get All User
        group_member_list = await bot.get_group_member_list(group_id=group_id)
        logger.debug(group_member_list)
        if SEND_LOG:
            await twqdall.send(Message(str(group_member_list)))

        # Map User
        db = pymysql.connect(host=QQMAP_HOST, port=3306, user=QQMAP_USERNAME,
                             passwd=QQMAP_PASSWORD, db="cpds_db", charset='utf8')

        cursor = db.cursor()
        for member in group_member_list:
            user_id = str(member['user_id'])
            logger.debug(f'processing: {user_id}')
            at_ = "[CQ:at,qq={}]".format(user_id)
            if SEND_LOG:
                await twqdall.send(Message(at_ + TWQDALL_RUNNING_PROMPT))

            stu_num = await qq2stunum(user_id, cursor)
            logger.debug(f'will process: {user_id} {stu_num}')

            if not stu_num:
                # await twqdall.send(Message(at_ + TWQDALL_NOT_IN_DATASET_PROMPT))
                continue

            # await twqdall.send(Message(at_ + TWQDALL_RUNNING_PROMPT + f'{stu_num}'))
            await twqdall.send(Message(at_ + TWQDALL_RUNNING_PROMPT))
            await tempReportEvent(at_, stu_num, twqdall)

        db.close()
        cursor.close()
        await twqdall.send(Message(TWQDALL_SUCCESS_PROMPT))
    except Exception as e:
        msg = f"Exception: {Exception}\n"
        msg += f"str(e): {str(e)}\nrepr(e): {repr(e)}\n"
        msg += f"traceback.format_exc(): {traceback.format_exc()}"
        await exception_log(bot, msg)

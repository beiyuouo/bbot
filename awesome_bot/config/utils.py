# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/22 12:43
# Description:

from nonebot.adapters import Bot
from nonebot.log import logger
from .config import *

EXCEPTION_ADMIN = config.exception_admin


async def exception_log(bot: Bot, msg: str):
    print(f'EXCEPTION_ADMIN: {EXCEPTION_ADMIN}')
    logger.debug(msg)
    for p in EXCEPTION_ADMIN:
        if p['type'] == 'group':
            await bot.call_api('send_group_msg', group_id=p['id'], message=msg)
        elif p['type'] == 'private':
            await bot.call_api('send_private_msg', user_id=p['id'], message=msg)
        else:
            await logger.debug(f'can not find exception admin type: {p}')

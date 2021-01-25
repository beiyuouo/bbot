# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/12 17:04
# Description:
import httpx
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import json
from nonebot.log import logger

from .apis import *

v2raycs = on_command("v2raycs", rule=to_me(), priority=5)


@v2raycs.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    user = event.get_user_id()
    # at_ = "[CQ:at,qq={}]".format(user)
    replay = await get_v2raycs()
    await v2raycs.finish(message=replay)
    # await v2ray.finish(message = at_ + " " + replay)


async def get_v2raycs():
    msg = """version: {}
ssr: {}
v2ray: {}"""
    _version = ''
    _ssr = ''
    _v2ray = ''
    async with httpx.AsyncClient() as client:
        resp = await client.get(ALKAID_VERSION_MANAGER_API)
        logger.debug(resp.json())
        _version = resp.json()['version-server']
        resp = await client.get(ALKAID_GET_SUBS_NUM_API)
        logger.debug(resp.json())
        resp = resp.json()
        _ssr = resp['ssr']
        _v2ray = resp['v2ray']
    return msg.format(_version, _ssr, _v2ray)

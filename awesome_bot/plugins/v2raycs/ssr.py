from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import json

from .apis import *

ssr = on_command("ssr", rule=to_me(), priority=5)


@ssr.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    user = event.get_user_id()
    # at_ = "[CQ:at,qq={}]".format(user)
    replay = await get_ssr()
    await ssr.finish(message=replay)
    # await ssr.finish(message = at_ + " " + replay)


async def get_ssr():
    str = requests.get(ALKAID_CAPTURE_SUBSCRIBE_SSR_API).text
    data = json.loads(str)
    return data['subscribe']

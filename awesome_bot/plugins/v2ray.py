from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import json

v2ray = on_command("v2ray", rule=to_me(), priority=5)


@v2ray.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    user = event.get_user_id()
    # at_ = "[CQ:at,qq={}]".format(user)
    replay = await get_v2ray()
    await v2ray.finish(message=replay)
    # await v2ray.finish(message = at_ + " " + replay)

async def get_v2ray():
    str = requests.get('').text
    data = json.loads(str)
    return data['subscribe']

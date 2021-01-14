# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/14 21:01
# Description:
import httpx
from nonebot import on_command
from nonebot.adapters.cqhttp import Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.log import logger

setu = on_command("setu", aliases=set(['瑟图', '色图', '来张色图', '来张瑟图']), rule=to_me(), priority=1)


@setu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    at_ = "[CQ:at,qq={}]".format(event.get_user_id())
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.mtyqx.cn/api/random.php?return=json')
        logger.debug(resp.json())
        imgurl = resp.json()['imgurl']
        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(Message(at_ + cqimg))

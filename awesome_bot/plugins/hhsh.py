# Author: BeiYu
# Github: https://github.com/beiyuouo
# Description:
import httpx
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, unescape
from nonebot.permission import SUPERUSER
from nonebot.log import logger
from nonebot.typing import T_State

hhsh = on_command("hhsh", priority=1)

url = r"https://lab.magiconch.com/api/nbnhhsh/guess"


@hhsh.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["text"] = args


@hhsh.got("text", prompt="多少说点行不？")
async def handle(bot: Bot, event: Event, state: T_State):
    args = state["text"].split(' ')
    logger.debug(args)
    for i in args:
        res = await query(bot, i)
        for j in res:
            await hhsh.send(j)


async def query(bot: Bot, someShit):
    data = {"text": someShit}
    logger.debug(data)

    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=data)
        if resp.status_code != 200:
            return ["错误：" + str(resp.status)]
        ShitJson = resp.json()
    logger.debug(ShitJson)
    ans = []
    for RealShit in ShitJson:
        re = ""
        try:
            for i in RealShit["trans"]:
                re += i + "\n"
        except:
            try:
                for i in RealShit["inputting"]:
                    re += i + "\n"
            except:
                pass
        re = re[:-1]
        if re == "":
            ans.append(f"呐呐呐，没有查到 {RealShit['name']} 的相关结果")
        else:
            ans.append(
                f"""呐，{RealShit['name']} 可能是：
{re}"""
            )

    return ans

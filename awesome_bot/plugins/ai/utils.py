# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/11 23:24
# Description:

from .config import *
from .baiduBot import BaiduBot
from nonebot.log import logger


async def get_resp(text: str):
    API_Key = BAIDU_API_KEY
    Secret_Key = BAIDU_SECRET_KEY
    # print(BAIDU_API_KEY, BAIDU_SECRET_KEY)
    bot_id = 'S44391'
    session = 'test2'
    # proxy = '127.0.0.1:7890'
    bot = BaiduBot(API_Key=API_Key, Secret_Key=Secret_Key, bot_id=bot_id, session=session)
    ans = await bot.sendMsg(text)
    logger.debug(ans)
    logger.debug(ans['answer'])
    return ans['answer']

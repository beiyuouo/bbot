# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/12 17:10
# Description:

import nonebot

global_config = nonebot.get_driver().config
config = nonebot.Config(**global_config.dict())
print(config)
# print(config.gocq_path)

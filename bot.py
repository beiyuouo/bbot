# bot.py
import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)

# load plugins
# nonebot.load_builtin_plugins()
nonebot.load_plugins("awesome_bot/plugins")
# nonebot.load_plugin('nonebot_plugin_picsearcher')

from awesome_bot.config.config import config

if config.test == 'true':
    nonebot.load_plugin("nonebot_plugin_test")

app = nonebot.get_asgi()

if __name__ == "__main__":
    nonebot.run()

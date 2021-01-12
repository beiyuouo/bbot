from functools import reduce

from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, unescape, Event, MessageEvent, Message, MessageSegment

say = on_command("say", to_me(), permission=SUPERUSER)


@say.handle()
async def say_unescape(bot: Bot, event: MessageEvent):

    # def _unescape(msg: Message, segment: MessageSegment):
    #    if segment.is_text():
    #        return msg.append(unescape(str(segment)))
    #    return msg.append(segment)

    # message = reduce(_unescape, event.get_message(), Message())  # type: ignore
    # await bot.send(message=message, event=event)
    await bot.send(message=Message(unescape(str(event.get_message()))), event=event)


echo = on_command("echo", to_me())


@echo.handle()
async def echo_escape(bot: Bot, event: MessageEvent):
    await bot.send(message=event.get_message(), event=event)

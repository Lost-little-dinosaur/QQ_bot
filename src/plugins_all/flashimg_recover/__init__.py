#感谢Something For nothing（qq：3330883674）提供的部分源码
from nonebot.adapters.cqhttp import Bot, Event, MessageEvent
from nonebot.adapters.cqhttp.message import Message
from nonebot.plugin import export
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot import on_message
import asyncio

export = export()
export.name = '防闪照小助手'
export.usage = '你发个闪照就知道了[]~(￣▽￣)~*'

async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    msg = str(event.get_message())
    return True if 'type=flash,' in msg else False

flashimg = on_message(priority=50,rule=Rule(_checker))
@flashimg.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    await asyncio.sleep(0.5)
    msg = str(event.get_message()).replace('type=flash,', '')
    await flashimg.finish(Message(msg))


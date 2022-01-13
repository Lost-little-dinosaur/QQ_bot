from nonebot.plugin import on_command,export
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp.message import Message

from .get_help import helpmsg

export = export()
export.name = '帮助'
export.usage = '恭喜你发现彩蛋一枚'

bot_help = on_command('help',priority=10)
@bot_help.handle()
async def bot_help_handle(bot: Bot, event: Event):
    msg = str(event.get_message()).strip()
    await bot_help.finish(message = Message(helpmsg(msg)))


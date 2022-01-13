from nonebot.plugin import on_command,on_message
from nonebot.adapters.cqhttp import Bot, Event


import service.blacklist as black
from .check import check


wzry = on_command('wzry',priority=50)
@wzry.handle()
async def wzry_handle(bot: Bot, event: Event):
    if black.check('wzry',str(event.get_session_id())):
        hero = str(event.get_message()).strip()
        await wzry.finish(check(hero))
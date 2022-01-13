from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment

aa = on_command('动漫涩图', priority=5)


@aa.handle()
async def _aa(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        res = str(event.get_message()).strip()
        if res == '':
            await bot.send(event=event, message=MessageSegment.image('https://api.yimian.xyz/img'))
        elif res == '1':
            await bot.send(event=event, message='1')
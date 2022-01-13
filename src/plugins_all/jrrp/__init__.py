import random
from datetime import date
from nonebot.plugin import on_command,export
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp.message import Message

export = export()
export.name   =  '今日人品'
export.usage  =  '''https://www.bilibili.com/read/cv11108712'''

def luck_simple(num):
    if num < 18:
        return '大吉'
    elif num < 53:
        return '吉'
    elif num < 58:
        return '半吉'
    elif num < 62:
        return '小吉'
    elif num < 65:
        return '末小吉'
    elif num < 71:
        return '末吉'
    else:
        return '凶'
    

jrrp = on_command('今日人品',priority=50)
@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed(( int(date.today().strftime("%y%m%d"))*45 )*( int(event.get_user_id())*55 ))
    lucknum = rnd.randint(1,100)
    await jrrp.finish(message = Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"'))

from nonebot.plugin import on_message,on_command,export
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp.permission import GROUP_ADMIN,GROUP_OWNER,PRIVATE_FRIEND

from .black import db,check 


export = export()
export.name = '黑名单'
export.usage = '''https://www.bilibili.com/read/cv11109352'''

#获取指令
blacklist = on_command('blist', priority=10,permission=GROUP_ADMIN|GROUP_OWNER|SUPERUSER)
@blacklist.handle()
async def blacklist_handle(bot: Bot, event: Event):
    await blacklist.finish(db.analysis(str(event.get_message()),str(event.get_session_id())))

#拦截事件并检查
blacklist_check = on_message(priority=1, block=False)
@blacklist_check.handle()
async def blacklist_check_handle(bot: Bot, event: Event):
    can_pass = check(str(event.get_message()),str(event.get_session_id()))
    if not can_pass :
        blacklist_check.block = True
        print('\nblacklist user detected, session blocked.\n')
    else:
        blacklist_check.block = False
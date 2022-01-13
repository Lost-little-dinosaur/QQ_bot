from datetime import date
from nonebot.plugin import on_command,export
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp.message import Message,MessageSegment
import asyncio

from .steam import check,refresh,is_existed


export = export()
export.name   =  'Steam热销'
export.usage  =  '''https://www.bilibili.com/read/cv11124972'''

steam = on_command('steam',priority=50)
@steam.handle()
async def steam_handle(bot: Bot, event: Event):
    inputmsg = str(event.get_message())
    if not is_existed():
        refresh()
        await steam.send('今日还未更新数据库，正在刷新前3页数据')
        await asyncio.sleep(10)
        await steam.send('正在查询数据')
    s = session_id_analysis(str(event.get_session_id()))
    #获取返回信息
    if s['groupid'] == "user":
        msg = check(str(event.get_message()).strip())
        await steam.finish(msg)
    else:
        msg = check(str(event.get_message()).strip(),'g')
        if type(msg) == type('o'):
            await steam.finish(msg)
        print(s['groupid'])
        print(str(msg))
        await bot.send_group_forward_msg(group_id=s['groupid'],messages=msg)
        await steam.finish()
        
def session_id_analysis(session_id):
    if "group" in session_id:
        _,groupid,userid = session_id.split('_')
        session_id_analyzed = {"groupid":f"{int(groupid)}", "userid":int(userid)}
    else:
        session_id_analyzed = {"groupid":"user", "userid":int(session_id)}   
    return session_id_analyzed
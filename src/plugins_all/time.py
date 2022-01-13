import time
from datetime import datetime
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me


def get_time():

    '''显示当前时间'''

    global time1
    time1 = ''
    time2 = time.strftime('%Y-%m-%d %H:%M:%S')
    '''星期'''
    dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
    day_Week = datetime.now().weekday() ###返回从0开始的数字，比如今天是星期5，那么返回的就是4

'''--------------现在时间--------------'''

sj = on_keyword({"现在时间","现在几点","多少时间","时间多少","时间","几点"})
#tg=on_command('',rule=to_me(),priority=5)
@sj.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    global time1
    time1 = ''
    time2 = time.strftime('%H:%M:%S')
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    xians = f"[CQ:face,id=6]"
    await sj.send(MessageSegment.at(id) + tx + xians + "现在时间是：" + time2)

'''----------------今天星期几-------------------'''
xqj = on_keyword({"星期几"})
@xqj.handle()
async def xqj_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    dayOfWeek = str(datetime.now().isoweekday())
    day_Week = str(datetime.now().weekday())
    js = "\n(数字1-7代表周一到周日)"
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    xians = f"[CQ:face,id=6]"
    await xqj.send(MessageSegment.at(id) + tx + xians + "今天是星期" + dayOfWeek + js)    

'''----------------------年月日---------------------'''
nian = on_keyword({"几年","几月","几日","几时","几分","几秒"})
@nian.handle()
async def nian_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    global time1
    time1 = ''
    time2 = time.strftime('%Y-%m-%d %H:%M:%S\n')
    #星期
    dayOfWeek = str(datetime.now().isoweekday())
    day_Week = str(datetime.now().weekday())
    js = "(年-月-日_时-分-秒)"
    js2 = "\n(数字1-7代表周一到周日)"
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    xians = f"[CQ:face,id=6]"
    await nian.send(MessageSegment.at(id) + tx + xians + "什么你不会看时间吗？真麻烦！现在是：" + time2 + js + "\n星期：" + dayOfWeek + js2)
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
yulu = on_keyword({'今日哔哩排行'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await yulu.send(message=Message(msg))

    except CQHttpError:
        pass


async def ji():
    url = 'https://api.muxiuge.cn/API/bilitop.php?n='
    resp = requests.get(url).json()
    data=resp['data'][0]
    data1=resp['data'][1]
    data2=resp['data'][2]
    data3=resp['data'][3]
    data4 = resp['data'][4]
    return str(data+data1+data2+data3+data4)
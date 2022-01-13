from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re
from nonebot import on_command
from nonebot.rule import to_me
from aiocqhttp.exceptions import Error as CQHttpError

# from nonebot.adapters.cqhttp.message import MessageSegment
# import http
# from nonebot.log import logger

da = on_keyword({'涩图'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    await da.send('ZERO-TWO：请您耐心等待。。。。。')


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    await da.send('ZERO-TWO：请您耐心等待。。。。。')


async def setu():
    url = "https://api.lolicon.app/setu/"
    da = requests.get(url).text
    ur = re.findall(r'url":"(.+?)"}]}', da)
    # setu=requests.get(ur).text
    str = ur[0]
    # st = requests.get(str).text
    tu = f"[CQ:image,file={str}]"
    return tu


msg = await setu()
try:
    await da.send(Message(msg))
except CQHttpError:
    pass

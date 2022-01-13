from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re
from aiocqhttp.exceptions import Error as CQHttpError

yulu = on_keyword({'哔哩热搜'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    # await yulu.send('请稍等，正在努力寻找视频中，请稍等...')
    msg = await f()
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def f():
    url = 'https://api.muxiuge.cn/API/bilirand.php'
    resp = requests.get(url).json()
    t='网址：'+resp['data']['url']
    zuo='作者：'+resp['data']['author']
    biao='标题：'+resp['data']['title']
    return str(zuo+'\n'+biao+'\n'+t)

yulu = on_keyword({'微博热搜'})
@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await w()
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def w():
    url = 'https://api.muxiuge.cn/API/wbrs.php'
    resp = requests.get(url).json()

    da1=resp['data'][0]
    te1='标题：'+da1.get('text')

    da2 = resp['data'][1]
    te2 = '标题：' + da2.get('text')

    da3 = resp['data'][2]
    te3 = '标题：' + da3.get('text')

    da4 = resp['data'][3]
    te4 = '标题：' + da4.get('text')

    da5 = resp['data'][4]
    te5 = '标题：' + da5.get('text')
    print(te5)
    rl = 'http://api.52guleng.cn/api/wzztp/api.php?s=325&ss=00A8FF&nr=' + te1+'\n'+te2+'\n'+te3+'\n'+te4+'\n'+te5
    png = requests.get(url=rl).text
    tu = f"[CQ:image,file={png}]"
    return tu
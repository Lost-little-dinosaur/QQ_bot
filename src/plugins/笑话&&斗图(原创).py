from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
import random
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
import json

da1 = on_command('笑话')


@da1.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    msg = await se1()
    try:
        await da1.send(Message(msg))

    except CQHttpError:
        pass


async def se1():
    try:
        url = 'https://api.iyk0.com/xh/'
        resp = requests.get(url=url).text
        # print(resp)
        # test = resp['data']
        print(resp)
        return resp
    except:
        return '此API已失效，请联系管理员更换API'


da1 = on_command('渣男')


@da1.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    msg = await se1()
    try:
        await da1.send(Message(msg))

    except CQHttpError:
        pass


async def se2():
    try:
        url = 'https://api.iyk0.com/zhanan'
        resp = requests.get(url=url).text
        # print(resp)
        # test = resp['data']
        print(resp)
        return resp
    except:
        return '此API已失效，请联系管理员更换API'


da1 = on_command('情话')


@da1.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    msg = await se1()
    try:
        await da1.send(Message(msg))

    except CQHttpError:
        pass


async def se3():
    try:
        url = 'https://api.iyk0.com/aiqing'
        resp = requests.get(url=url).text
        # print(resp)
        # test = resp['data']
        print(resp)
        return resp
    except:
        return '此API已失效，请联系管理员更换API'


fatu = on_command("斗图")  # on_command会检测以/开头的词语


@fatu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["args"] = args


@fatu.got("args", prompt="您想斗的图叫啥呀？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    agrs = state["args"]
    tu = await my_get_pic(agrs)
    try:
        await fatu.send(Message(tu))
    except CQHttpError:
        pass


async def my_get_pic(agrs):
    try:
        url = 'https://api.iyk0.com/sbqb/?msg=' + agrs
        resp = requests.get(url=url).json()
        data_img = resp['data_img']
        random.shuffle(data_img)
        pick_3 = []
        l = 3 if len(data_img) > 3 else len(data_img)

        for i in range(l):
            pick_3.append(data_img[i]['img'])
        print(pick_3)
        if l == 3:
            msg = f'已为主人随机返回三张匹配的图：\n[CQ:image,file={pick_3[0]}]\n[CQ:image,file={pick_3[1]}]\n[CQ:image,file={pick_3[2]}]'
        elif l == 2:
            msg = f'已为主人随机返回两张匹配的图：\n[CQ:image,file={pick_3[0]}]\n[CQ:image,file={pick_3[1]}]'
        elif l == 1:
            msg = f'已为主人随机返回两张匹配的图：\n[CQ:image,file={pick_3[0]}]\n'
        else:
            msg = '抱歉，没有找到图片，让主人失望了。。'
        # msg = f"[CQ:image,file={pick_3[0]}]"
        # msg = f"[CQ:image,file=http://p.ananas.chaoxing.com/star3/origin/7b8ae493f609abe1c673d109f4eecc86.png]"
        return msg
    except:
        return '此API已失效，请联系管理员更换API'

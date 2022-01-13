from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
import json
from nonebot.permission import *
from nonebot.rule import to_me
import requests


'''
本程序可以利用菜鸟教程的在线工具运行代码（找了好半天才找到一个既没有加密又没有反爬的网站），发送'/'+编程语言即可在线运行编译，现支持Python，C，PHP，Java，大小写均可。
尽量不要多次频繁访问，（这用的是我的token，没准你可能会把我的token给搞没了），你也可以自己登录这个网站按F12找到自己的token加到POST中。
'''


py = on_command("python")  # on_command会检测以/开头的词语


@py.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@py.got("code", prompt="请输入您的Python代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 15,
        'fileext': 'py3'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    await py.send(temp["output"])


py = on_command("Python")  # on_command会检测以/开头的词语


@py.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@py.got("code", prompt="请输入您的Python代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 15,
        'fileext': 'py3'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    await py.send(temp["output"])


Py = on_command("Python")  # on_command会检测以/开头的词语


@Py.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@Py.got("code", prompt="请输入您的Python代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 15,
        'fileext': 'py3'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await Py.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await Py.send(temp["output"])


C = on_command("C")  # on_command会检测以/开头的词语


@C.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@C.got("code", prompt="请输入您的C代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 7,
        'fileext': 'c'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await C.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await C.send(temp["output"])


c = on_command("c")  # on_command会检测以/开头的词语


@c.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@c.got("code", prompt="请输入您的c代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 7,
        'fileext': 'c'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await c.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await c.send(temp["output"])


php = on_command("php")  # on_command会检测以/开头的词语


@php.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@php.got("code", prompt="请输入您的php代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 3,
        'fileext': 'php'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await php.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await php.send(temp["output"])


PHP = on_command("PHP")  # on_command会检测以/开头的词语


@PHP.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@PHP.got("code", prompt="请输入您的PHP代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 3,
        'fileext': 'PHP'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await PHP.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await PHP.send(temp["output"])



java = on_command("java")  # on_command会检测以/开头的词语


@java.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@java.got("code", prompt="请输入您的java代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 8,
        'fileext': 'java'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await java.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await java.send(temp["output"])

JAVA = on_command("JAVA")  # on_command会检测以/开头的词语


@JAVA.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    code = str(event.get_message()).strip()
    if code:
        state['code'] = code


@JAVA.got("code", prompt="请输入您的JAVA代码")
async def handle_city(bot: Bot, event: Event, state: T_State):
    code = state["code"]
    # print(code)
    url = 'https://tool.runoob.com/compile2.php'
    data = {
        "code": code,
        "token": "4381fe197827ec87cbac9552f14ec62a",
        "stdin": "",
        "language": 8,
        'fileext': 'JAVA'}
    r = requests.post(url, data)
    temp = json.loads(r.text)
    # print(temp["output"])
    if temp["output"] == '' and temp['errors'] != '\n\n':
        await JAVA.send("您输入的代码有误！错误信息如下：\n" + temp['errors'])
    else:
        await JAVA.send(temp["output"])
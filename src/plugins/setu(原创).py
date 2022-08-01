import urllib.request

from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
import random
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent


ban_list=["228089083"]

def check_img(url):
    if ('png' in url or 'jpg' in url or 'bmp' in url or 'jpeg' in url or len(url) > 30) and str(
            requests.get(url)) == '<Response [200]>':
        return f"[CQ:image,file={url.strip()}]"  # 用CQ码发送图片，前面的f代表可以用{}中括号变量
    else:
        return '此API已失效，请联系管理员更换API'


da = on_command("美腿")


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await ji()
    try:
        await da.send(Message(msg))  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
    except CQHttpError:
        pass


async def ji():
    try:
        url = 'https://api.iyk0.com/mtt'
        resp = requests.get(url=url).url
        # print(resp)
        print(resp)
        return check_img(resp)
    except:
        return '此API已失效，请联系管理员更换API'


da1 = on_command('涩图')


@da1.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    msg = await se1()
    try:
        await da1.send(Message(msg))

    except CQHttpError:
        pass


async def se1():
    try:
        url = 'https://yanghanwen.xyz/tu/se.php'
        resp = requests.get(url=url).json()
        # print(resp)
        test = resp['data']
        print(test)

        return check_img(test)
    except:
        return '此API已失效，请联系管理员更换API'


da2 = on_command('cos')


@da2.handle()
async def h2(bot: Bot, event: Event, state: T_State):
    msg = await se2()
    try:
        await da2.send(Message(msg))

    except CQHttpError:
        pass


async def se2():
    try:
        url = 'https://api.iyk0.com/cos'
        resp = requests.get(url=url).url
        print(resp)
        return check_img(resp)
    except:
        return '此API已失效，请联系管理员更换API'


da3 = on_command('美女')


@da3.handle()
async def h3(bot: Bot, event: Event, state: T_State):
    msg = await se3()
    try:
        # await da3.send(Message("小语希望哥哥好好学习呢！要注意身体哦"))
        await da3.send(Message(msg))

    except CQHttpError:
        pass


async def se3():
    try:
        url = 'https://www.hlapi.cn/api/mm2'
        resp = requests.get(url=url).url
        print(resp)
        return check_img(resp)
    except:
        return '此API已失效，请联系管理员更换API'


da4 = on_command('小姐姐')


@da4.handle()
async def h4(bot: Bot, event: Event, state: T_State):
    msg = await se4()
    try:
        await da4.send(Message(msg))

    except CQHttpError:
        pass


async def se4():
    try:
        url = 'https://www.hlapi.cn/api/sjmm1'
        resp = requests.get(url=url).url
        print(resp)
        return check_img(resp)
    except:
        return '此API已失效，请联系管理员更换API'


da5 = on_command('萝莉')


@da5.handle()
async def h(bot: Bot, event: Event, state: T_State):
    msg = await se5()
    try:
        await da5.send(Message(msg))

    except CQHttpError:
        pass


async def se5():
    try:
        url = 'https://www.hlapi.cn/api/ecy1'
        resp = requests.get(url=url).url
        print(resp)
        return check_img(resp)
    except:
        return '此API已失效，请联系管理员更换API'


# da = on_command("帅哥")
#
#
# @da.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     msg = await shuaige()
#     try:
#         await da.send(Message(msg))  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
#     except CQHttpError:
#         pass
#
#
# async def shuaige():
#     all_t = ['http://img.jj20.com/up/allimg/tx21/110423010478167.jpg',]
#     url = random.choice(all_t)
#     print(url)
#     print(requests.get(url))
#     if requests.get(url).status_code == 200:
#         return check_img(url)
#     else:
#         return '此API已失效，请联系管理员更换API'

# 下面为爬取帅哥图片的代码
#
# all_pic = []
# for i in range(64, 85):
#     url = 'http://www.jj20.com/tx/nansheng/2087' + str(i) + '.html'
#     resp = requests.get(url=url).text
#     start = resp.find('<div id="content" class="m_qmview g-cont item">') + 47
#     end = resp.find('</div>', start, len(resp))
#     all_my = resp[int(start):int(end)]
#     all_l = all_my.split('\n')
#     for each in all_l:
#         start_each = each.find('src="') + 5
#         end_each = each.find('"></p></a>')
#         if end_each - start_each > 10 and len(requests.get(url=each[start_each:end_each]).text) > 1000:
#             print(each[start_each:end_each])
#             all_pic.append(each[start_each:end_each])
#
# print(all_pic)

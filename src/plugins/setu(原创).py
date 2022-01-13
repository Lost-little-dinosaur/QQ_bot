import urllib.request

from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
import random
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent


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
        await da3.send(Message(msg))

    except CQHttpError:
        pass


async def se3():
    try:
        url = 'https://api.iyk0.com/mn'
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
        url = 'https://api.iyk0.com/mn'
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
        url = 'https://api.iyk0.com/luoli'
        resp = requests.get(url=url).url
        print(resp)
        return check_img(resp)
    except:
        return '此API已失效，请联系管理员更换API'


da = on_command("帅哥")


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await shuaige()
    try:
        await da.send(Message(msg))  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
    except CQHttpError:
        pass


async def shuaige():
    all_t = ['http://img.jj20.com/up/allimg/tx21/110423010478167.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478168.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478169.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478170.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478172.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478173.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478175.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478177.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478179.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010478181.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578183.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578185.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578188.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578192.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578195.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578197.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578199.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578201.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578207.png',
             'http://img.jj20.com/up/allimg/tx21/110423010578209.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010578214.jpg',
             'http://img.jj20.com/up/allimg/tx21/110423010678216.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015778143.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015778144.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878145.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878146.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878147.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878148.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878149.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878150.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878151.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878152.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878153.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878154.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878155.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878156.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878157.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878158.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878159.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878160.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878161.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878162.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015878163.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015978164.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015978165.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015978166.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014678125.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014678126.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014778127.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014778128.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014878129.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014878130.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014878131.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014878132.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015078133.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015078134.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015178135.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015178136.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015178137.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015278138.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015278139.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015278140.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015378141.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423015378142.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014078113.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014078114.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014078115.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014078116.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014078117.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014178118.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014178119.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014178120.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014278121.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014278122.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014278123.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423014278124.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013178089.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013178091.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013178092.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013178093.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278096.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278097.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278098.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278099.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278100.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278101.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278102.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278103.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278104.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278105.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013278106.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013378107.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013378108.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013378109.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013378110.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013578111.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423013578112.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012778076.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012878077.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012878078.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012878079.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012878080.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012878081.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012978082.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423012978083.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013277776.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013377782.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013377785.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013377788.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013377789.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013377792.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015577993.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015677994.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015677995.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015677996.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015677997.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015677998.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015777999.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015778000.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015778001.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015778002.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015778003.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015878004.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015878005.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015878006.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011477612.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011477615.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011477620.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011577627.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011677654.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011677658.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011677659.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011677662.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011777664.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011777665.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011777666.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011877667.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011877668.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011877669.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011977670.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011977671.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011977672.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011977673.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012077674.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012077675.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012177676.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377472.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377473.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377478.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377481.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477489.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477492.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013577496.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013577500.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013577501.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013577502.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013677503.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013677504.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013677505.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013777506.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013777507.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013777508.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013777509.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013777510.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013877512.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013977526.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013977540.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011177305.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011177306.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011277307.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011277308.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011277309.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011277310.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011377311.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011377312.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011377313.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011377314.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011377315.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011477316.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011477317.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011477318.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011477319.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011477320.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011477321.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011577322.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011577323.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011577324.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677327.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677331.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677335.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677348.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677352.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011777369.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011777374.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011777381.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011777383.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011877384.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013277159.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013377165.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013377171.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013377176.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013377178.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013477182.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013477187.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013477188.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013477190.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013477192.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013577201.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013577205.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013577212.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013577214.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013577215.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013677218.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013677220.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013677222.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013777224.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013777226.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010278007.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010278008.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010278009.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010278010.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378011.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378012.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378013.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378014.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378015.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378016.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378017.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378018.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378019.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378020.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378021.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378022.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378023.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378024.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378025.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378026.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378027.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378028.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378029.jpg',
             'http://img.jj20.com/up/allimg/tx21/100423010378030.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014977929.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077930.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077931.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077932.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077933.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077934.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077936.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077938.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077939.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077940.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077941.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077942.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077943.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077944.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077945.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077946.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015077947.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177948.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177949.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177950.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177951.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177952.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177953.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423015177955.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014177821.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014177822.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014177823.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014177824.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014277825.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014277826.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014277827.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014277828.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014377829.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014377830.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014377831.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014377832.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014377833.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014477834.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014477835.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014477836.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014477837.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423014477838.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012877709.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012977710.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012977711.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012977712.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012977714.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013077721.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013077732.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013077734.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013077739.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013077745.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177756.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177757.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177758.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177759.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177766.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177768.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177770.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013177771.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423013277773.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277690.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277692.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277693.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277694.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277695.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277696.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277697.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277698.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423012277699.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011277591.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011277592.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011277593.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011277594.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377595.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377596.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377597.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377598.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377599.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377600.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377601.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377602.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377603.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377604.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377605.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377606.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377607.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377608.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377609.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377610.jpg',
             'http://img.jj20.com/up/allimg/tx21/090423011377611.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013077456.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013177457.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013177458.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013177459.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013177460.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013177461.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013177462.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277463.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277464.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277465.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277466.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277467.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277468.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277469.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013277470.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377471.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377474.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377475.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377476.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377477.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377479.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013377480.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477482.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477483.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477484.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477485.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423013477487.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011577325.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011577326.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677328.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677329.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677330.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677332.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677333.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677334.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677336.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677337.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677338.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677339.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677340.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677341.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677343.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677345.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677347.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677350.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677353.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677356.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677359.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011677361.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011777363.jpg',
             'http://img.jj20.com/up/allimg/tx21/080423011777366.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977231.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977232.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977233.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977235.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977236.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977239.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423013977240.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077241.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077242.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077243.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077244.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077246.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077247.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077248.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077250.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077251.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077252.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077253.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077254.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077255.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077257.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077258.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014077259.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014177260.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014177261.jpg',
             'http://img.jj20.com/up/allimg/tx21/070423014177262.jpg']
    url = random.choice(all_t)
    print(url)
    print(requests.get(url))
    if requests.get(url).status_code == 200:
        return check_img(url)
    else:
        return '此API已失效，请联系管理员更换API'

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

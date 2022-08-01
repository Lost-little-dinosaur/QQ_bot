import datetime
import requests
from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
from selenium import webdriver
import uuid
import time
import asyncio

from src.plugins.HDUHelp import my_db

my_uuid = str(uuid.uuid4())
check_url = 'https://cas.hdu.edu.cn/cas/checkQRCodeScan?uuid=' + my_uuid
login_url = 'https://cas.hdu.edu.cn/cas/login?service=https://api.hduhelp.com/sso?state=' + my_uuid


async def login(qqid, da1, sql_session, User_Agent, at_flag):  # 用户通过扫码重新登陆
    try:
        global login_url
        global check_url
        session = requests.session()

        chrome_options = webdriver.ChromeOptions()
        # 携带头信息以及设置无头模式
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("https=47.100.104.247:8080")
        chrome_options.add_argument("http=36.248.10.47:8080")
        chrome_options.add_argument(
            "user-agent=" + User_Agent)
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)

        driver.get(login_url)  # 打开网页 #可能有TIMEOUT问题
        button1 = driver.find_element_by_xpath('//*[@id="template_container"]/div/div[1]/a[2]')
        button1.click()
        erwei = "http://" + driver.find_element_by_xpath('//*[@id="qrcode"]/img').get_attribute("src")

        await da1.send(Message(at_flag + f"[CQ:image,file=base64://" + erwei.split(',')[1] + "]"))
        now_url = driver.current_url
        n = 0
        while 'cas.hdu.edu.cn' in now_url:  # TODO：加一个异步等待
            # print(now_url)
            await asyncio.sleep(0.1)
            n += 1
            now_url = driver.current_url
            if n > 1000:
                await da1.send(Message(at_flag + "二维码已过期，请重新输入'/登录'以重新获取二维码！"))
                driver.quit()
                return False
        driver.get(check_url)
        cas_cookie = driver.get_cookies()[2]["value"]  # 获取到用户CAS_Cookie
        driver.quit()
        if cas_cookie != '':
            users = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()

            # 向服务器请求state（uuid）
            url1 = 'https://api.hduhelp.com/login/direct/cas?clientID=app&school=hdu&redirect=https://app.hduhelp.com/#/login?redirectTo=/app/scores'
            header = {
                "User-Agent": User_Agent}
            r1 = session.get(url1, headers=header, allow_redirects=False)
            if 'Location' not in r1.headers:
                await da1.send(Message(at_flag + "获取UUID失败，请联系管理员解决问题"))
                return False
            # return_uuid = r1.headers['Location'].split('%3D')[1]

            # 带上CASTGC作为cookie请求到ticket
            header = {
                "User-Agent": User_Agent,
                "Cookie": "CASTGC=" + cas_cookie,
            }
            r2 = session.get(r1.headers['Location'], headers=header, allow_redirects=False)
            if 'Location' not in r2.headers:  # 这里有state和ticket
                await da1.send(Message(at_flag + "获取Ticket失败，请联系管理员解决问题"))
                return False
            # return_ticket = r2.headers['Location'].split('ticket=')[1]

            # 携带ticket和state得到服务器的token
            r3 = session.get(r2.headers['Location'], headers=header, allow_redirects=False)
            if 'Location' not in r3.headers:
                await da1.send(Message(at_flag + "获取Token失败，请联系管理员解决问题"))
                return False
            return_token = r3.headers['Location'].split('auth=')[1]

            # r4 = session.get("https://cas.hdu.edu.cn/cas/login?service=https%3A%2F%2Fi.hdu.edu.cn%2Ftp_up%2F",
            #                  headers=header,
            #                  allow_redirects=False)  # 获取到ticket
            # ticket = r4.headers["Location"].split("ticket=")[1]
            # # 请求https://i.hdu.edu.cn/tp_up/并带上ticket，可以得到tp_up
            #
            # r5 = session.get("https://i.hdu.edu.cn/tp_up/?ticket=" + ticket, headers=header,
            #                  allow_redirects=False)  # 请求302前的地址，可以得到一个tp_up
            #
            # if "tp_up=" in r5.headers["location"]:
            #     tp_up = r5.headers["Location"].split("tp_up=")[1]
            # else:
            #     await da1.send(Message(at_flag + "获取tp_up失败，请联系管理员解决问题"))
            #     return False

            # 接下来是数据库操作
            temp = '-1'
            for item in users:
                temp = item
            if temp == '-1':  # 数据库里没有信息，则增加记录
                add_user = my_db.qq_bot_hdu(qqid, -1, "", return_token, cas_cookie, "",
                                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                sql_session.add(add_user)
                sql_session.commit()
                await da1.send(Message(at_flag + "您已成功登录"))
            else:  # 数据库里有信息，则修改记录
                sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).update(
                    {'token': return_token, 'CASTGC': cas_cookie, })  # 要根据主键去查
                sql_session.commit()
                # print(cas_cookie)
                await da1.send(Message(at_flag + "您已成功重新登录"))
        else:
            await da1.send(Message(at_flag + "未获取到登录Cookie！请联系管理员解决问题"))

        return True
    except:
        await da1.send(Message(at_flag + "登录失败！可能是网络原因，请联系管理员解决问题"))
        return False

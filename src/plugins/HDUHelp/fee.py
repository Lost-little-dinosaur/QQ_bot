import requests
from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
import time
import json

from src.plugins.HDUHelp import my_db, __init__, check


async def electric_fee(qqid, da2, User_Agent, at_flag):
    sql_session = my_db.db_session()
    users = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()
    temp = '-1'
    for item in users:
        temp = item
    if temp == '-1':  # 如果没记录
        await da2.send(Message(at_flag + "您未登录！请输入'/登录'后获取二维码扫描登录！"))
    else:  # 如果有记录
        if not check.check(temp.token, User_Agent):  # 如果Token过期
            await da2.send(Message(at_flag + "您的Token已过期！请输入'/登录'后重新登录！"))
            return False
        else:
            session = requests.session()
            header = {
                "User-Agent": User_Agent,
                "authorization": "token " + temp.token,
            }
            r3 = session.get("https://api.hduhelp.com/electric/fee", headers=header)
            r3.content.decode("utf-8")
            r3 = json.loads(str(r3.text))
            r4 = session.get("https://api.hduhelp.com/electric/history", headers=header)
            r4.content.decode("utf-8")
            r4 = json.loads(str(r4.text))
            # print(r3)
            # print(r4.text)
            res_str = ""
            for item in r4['data']['history']:
                if item['Change'] == '-':
                    res_str = str(item['Time']).split('T')[0] + '\n剩余电费：' + str(
                        item['Fee']) + '\n————————————\n' + res_str
                elif '-' in str(item['Change']):
                    res_str = str(item['Time']).split('T')[0] + '\n减少了' + str(item['Change']).replace('-',
                                                                                                      '') + '  剩余电费：' + str(
                        item['Fee']) + '\n————————————\n' + res_str
                elif '+' in str(item['Change']):
                    res_str = str(item['Time']).split('T')[0] + '\n增加了' + str(item['Change']).replace('+',
                                                                                                      '') + '  剩余电费：' + str(
                        item['Fee']) + '\n————————————\n' + res_str
            res_str = '下面是您寝室最近的几条电费使用记录：\n' + res_str
            # time.sleep(5)
            await da2.send(Message(
                at_flag + "您寝室电费剩余为：" + str(r3['data']['fee']) + "\n您寝室两周内平均日消费为：" +
                str(r4['data']['average'])+"\n"))
            await da2.send(Message(at_flag + res_str))
            print("发送成功！")


async def yikatong_fee(qqid, da2, User_Agent, at_flag):
    sql_session = my_db.db_session()
    users = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()
    temp = '-1'
    for item in users:
        temp = item
    if temp == '-1':  # 如果没记录
        await da2.send(Message(at_flag + "您未登录！请输入'/登录'后获取二维码扫描登录！"))
    else:  # 如果有记录
        if not check.check(temp.token, User_Agent):  # 如果Token过期
            await da2.send(Message(at_flag + "您的Token已过期！请输入'/登录'后重新登录！"))
            return False
        else:
            session = requests.session()
            header = {
                "User-Agent": User_Agent,
                "authorization": "token " + temp.token,
            }
            res_str1 = "您一卡通今日消费为："
            res_str2 = ""
            num = 0  # 表示今天的额度
            now = int(time.time())  # 获取今天的时间
            r3 = session.get("https://api.hduhelp.com/salmon_base/card/info", headers=header)
            r3.content.decode("utf-8")
            r3 = json.loads(str(r3.text))
            print(r3)
            for item in r3['data']['flow']:
                timeArray = time.localtime(item['createTime'])
                if item['feeName'] == '消费':
                    res_str2 += str(time.strftime("%Y-%m-%d %H:%M:%S", timeArray)) + "\n" + item['deviceName'] + ' ' + \
                                item['feeName'] + '  ' + str(item['totalFee']).replace('-', '') + '元\n' + "剩余：" + str(
                        item['remaining']) + '元\n————————————\n'
                else:
                    res_str2 += str(time.strftime("%Y-%m-%d %H:%M:%S", timeArray)) + "\n" + item['deviceName'] + ' ' + \
                                item['feeName'] + '  ' + str(item['totalFee']).replace('+', '') + '元\n' + "剩余：" + str(
                        item['remaining']) + '元\n————————————\n'
                if str(time.strftime("%m-%d", time.localtime(item['createTime']))) == str(
                        time.strftime("%m-%d", time.localtime(now))):
                    if item['feeName'] == '消费':
                        num -= item['totalFee']
                    else:
                        num += item['totalFee']

            await da2.send(Message(
                at_flag + res_str1 + str(num) + '元\n剩余为：' + str(r3['data']['remaining']) + '元'))

            if res_str2 != "":
                res_str2 = "您最近一周内的几条数据如下：\n" + res_str2
                await da2.send(Message(at_flag + res_str2))

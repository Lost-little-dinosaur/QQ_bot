import json

import nonebot
import requests
from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
import time
from datetime import datetime

from src.plugins.HDUHelp import my_db, __init__, check


def check_avalible(startWeek, nowWeek, endWeek, distribute):
    weekArr = list(range(int(startWeek), int(endWeek) + 1))
    if distribute == "":
        checkWeek = -1
    elif distribute == "双":
        checkWeek = 0
    elif distribute == "单":
        checkWeek = 1
    else:
        checkWeek = -2
    if int(nowWeek) in weekArr and (int(nowWeek) % 2 == checkWeek or checkWeek == -1):
        return True
    else:
        return False


async def schedule_today(qqid, da2, User_Agent, at_flag):
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
            r3 = session.get("https://api.hduhelp.com/time", headers=header)
            r3.content.decode("utf-8")
            r3 = json.loads(str(r3.text))
            schoolYear = r3["data"]['schoolYear']
            semester = r3["data"]['semester']
            weekNow = r3["data"]['weekNow']

            r1 = session.get(
                "https://api.hduhelp.com/base/student/schedule?schoolYear=" + schoolYear + "&semester=" + semester,
                headers=header)
            # print(r1.text)
            r1.content.decode("utf-8")
            r1 = json.loads(str(r1.text))
            all_arr = r1['data']
            dayOfWeek = datetime.now().isoweekday()  # 返回数字1-7代表周一到周日
            # class_today = []
            if len(all_arr) == 0:
                res_str = "咦，小语好像没有发现您目前有任何课程呢！"
            else:
                res_str = at_flag + "您今日的课表为：\n"
                index = 1
                i = 0
                while i < len(all_arr):  # 遍历整张表的数组
                    teacher = str(all_arr[i]['TEACHER'])
                    while i + 1 < len(all_arr) and str(all_arr[i]['COURSE']) == str(all_arr[i + 1]['COURSE']) and str(
                            all_arr[i + 1]['TEACHER']) not in teacher:
                        teacher += "、" + str(all_arr[i + 1]['TEACHER'])
                        i += 1
                    if all_arr[i]["WEEKDAY"] == str(dayOfWeek) and check_avalible(all_arr[i]['STARTWEEK'],
                                                                                  weekNow, all_arr[i]['ENDWEEK'],
                                                                                  all_arr[i]['DISTRIBUTE']):
                        # class_today.append(all_arr[i])
                        res_str += str(index) + '：' + str(all_arr[i]['COURSE']) + '\n地点：' + str(
                            all_arr[i]['CLASSROOM']) + '\n时间：' + str(all_arr[i]['STARTTIME']) + "-" + str(
                            all_arr[i]['ENDTIME']) + " (" + str(all_arr[i]['STARTSECTION']) + "-" + str(all_arr[i][
                                                                                                            'ENDSECTION']) + "节)" + '\n老师：' + teacher + '\n————————————\n'
                        index += 1
                    i += 1
            if res_str == at_flag + "您今日的课表为：\n":
                res_str = at_flag + "您今日没有任何课程，去好好happy下吧！"

            await da2.send(Message(res_str))


async def schedule_tomorrow(qqid, da2, User_Agent, at_flag):
    # print(nonebot.get_bots())
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
            r3 = session.get("https://api.hduhelp.com/time", headers=header)
            r3.content.decode("utf-8")
            r3 = json.loads(str(r3.text))
            schoolYear = r3["data"]['schoolYear']
            semester = r3["data"]['semester']
            weekNow = r3["data"]['weekNow']

            r1 = session.get(
                "https://api.hduhelp.com/base/student/schedule?schoolYear=" + schoolYear + "&semester=" + semester,
                headers=header)
            # print(r1.text)
            r1.content.decode("utf-8")
            r1 = json.loads(str(r1.text))
            all_arr = r1['data']
            dayOfWeek = datetime.now().isoweekday() + 1  # 返回数字1-7代表周一到周日
            # class_today = []
            if len(all_arr) == 0:
                res_str = "咦，小语好像没有发现您目前有任何课程呢！"
            else:
                res_str = at_flag + "您明日的课表为：\n"
                index = 1
                i = 0
                while i < len(all_arr):  # 遍历整张表的数组
                    teacher = str(all_arr[i]['TEACHER'])
                    while i + 1 < len(all_arr) and str(all_arr[i]['COURSE']) == str(
                            all_arr[i + 1]['COURSE']) and str(
                        all_arr[i + 1]['TEACHER']) not in teacher:
                        teacher += "、" + str(all_arr[i + 1]['TEACHER'])
                        i += 1
                    if all_arr[i]["WEEKDAY"] == str(dayOfWeek) and check_avalible(all_arr[i]['STARTWEEK'],
                                                                                  weekNow,
                                                                                  all_arr[i]['ENDWEEK'],
                                                                                  all_arr[i]['DISTRIBUTE']):
                        # class_today.append(all_arr[i])
                        res_str += str(index) + '：' + str(all_arr[i]['COURSE']) + '\n地点：' + str(
                            all_arr[i]['CLASSROOM']) + '\n时间：' + str(all_arr[i]['STARTTIME']) + "-" + str(
                            all_arr[i]['ENDTIME']) + " (" + str(all_arr[i]['STARTSECTION']) + "-" + str(
                            all_arr[i][
                                'ENDSECTION']) + "节)" + '\n老师：' + teacher + '\n————————————\n'
                        index += 1
                    i += 1
            if res_str == at_flag + "您明日的课表为：\n":
                res_str = at_flag + "您明日没有任何课程，去好好happy下吧！"

            await da2.send(Message(res_str))

            # if __name__ == '__main__':
            #     session = requests.session()
            #     res=session.get()

            # async def schedule_today(qqid, da2, User_Agent, at_flag):
            #     sql_session = my_db.db_session()
            #     users = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()
            #     temp = '-1'
            #     for item in users:
            #         temp = item
            #     if temp == '-1':  # 如果没记录
            #         await da2.send(Message(at_flag + "您未登录！请输入'/登录'后获取二维码扫描登录！"))
            #     else:  # 如果有记录
            #         if not check.check(temp.token, User_Agent):  # 如果Token过期
            #             await da2.send(Message(at_flag + "您的Token已过期！请输入'/登录'后重新登录！"))
            #             return False
            #         else:
            #             session = requests.session()
            #             header = {
            #                 "User-Agent": User_Agent,
            #                 "authorization": "token " + temp.token,
            #             }
            #             r1 = session.get("https://api.hduhelp.com/infoStream/v3", headers=header)
            #             # print(r1.text)
            #             today = r1['data']['schedule']['data']['today']
            #             if today == []:
            #                 await da2.send(Message(at_flag + "您今日你没有任何课程。放松一下或者找个地方自习吧！"))
            #             else:
            #                 res_str = at_flag + "您今日的课表为：\n"
            #                 i = 0
            #                 index = 1
            #                 while i < len(today):
            #                     teacher = str(today[i]['TEACHER'])
            #                     while i + 1 < len(today) and str(today[i]['COURSE']) == str(today[i + 1]['COURSE']):
            #                         teacher += "、" + str(today[i + 1]['TEACHER'])
            #                         i += 1
            #                     res_str += str(index) + '：' + str(today[i]['COURSE']) + '\n地点：' + str(
            #                         today[i]['CLASSROOM']) + '\n时间：' + str(today[i]['STARTTIME']) + "-" + str(
            #                         today[i]['ENDTIME']) + '\n老师：' + teacher + '\n————————————\n'
            #                     i += 1
            #                     index += 1
            #                 await da2.send(Message(res_str))
            #
            #
            # async def schedule_tomorrow(qqid, da2, User_Agent, at_flag):
            #     sql_session = my_db.db_session()
            #     users = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()
            #     temp = '-1'
            #     for item in users:
            #         temp = item
            #     if temp == '-1':  # 如果没记录
            #         await da2.send(Message(at_flag + "您未登录！请输入'/登录'后获取二维码扫描登录！"))
            #     else:  # 如果有记录
            #         if not check.check(temp.token, User_Agent):  # 如果Token过期
            #             await da2.send(Message(at_flag + "您的Token已过期！请输入'/登录'后重新登录！"))
            #             return False
            #         else:
            #             session = requests.session()
            #             header = {
            #                 "User-Agent": User_Agent,
            #                 "authorization": "token " + temp.token,
            #             }
            #             r1 = session.get("https://api.hduhelp.com/infoStream/v3", headers=header)
            #
            #             today = r1['data']['schedule']['data']['tomorrow']
            #             if today == []:
            #                 await da2.send(Message(at_flag + "您明日你没有任何课程。放松一下或者找个地方自习吧！"))
            #             else:
            #                 res_str = at_flag + "您明日的课表为：\n"
            #                 i = 0
            #                 index = 1
            #                 while i < len(today):
            #                     teacher = str(today[i]['TEACHER'])
            #                     while i + 1 < len(today) and str(today[i]['COURSE']) == str(today[i + 1]['COURSE']):
            #                         teacher += "、" + str(today[i + 1]['TEACHER'])
            #                         i += 1
            #                     res_str += str(index) + '：' + str(today[i]['COURSE']) + '\n地点：' + str(
            #                         today[i]['CLASSROOM']) + '\n时间：' + str(today[i]['STARTTIME']) + "-" + str(
            #                         today[i]['ENDTIME']) + '\n老师：' + teacher + '\n————————————\n'
            #                     i += 1
            #                     index += 1
            #                 await da2.send(Message(res_str))

import requests
from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent

from src.plugins.HDUHelp import my_db, __init__, check


async def grade(qqid, da2, User_Agent, at_flag):
    sql_session = my_db.db_session()
    users = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()
    temp = '-1'
    for item in users:
        temp = item
    if temp == '-1':  # 如果没记录
        await da2.send(Message(at_flag + "您未登录！请输入'/登录'后获取二维码扫描登录！"))
    else:  # 如果有记录
        if not check.check(temp.token, User_Agent):
            await da2.send(Message(at_flag + "您的Token已过期！请输入'/登录'后重新登录！"))
            return False
        else:
            session = requests.session()
            header = {
                "User-Agent": User_Agent,
                "authorization": "token " + temp.token,
            }
            # 时间接口
            r3 = session.get("https://api.hduhelp.com/time", headers=header)
            schoolYear = r3.json()["data"]['schoolYear']
            semester = r3.json()["data"]['semester']
            # 成绩接口
            r4 = session.get(
                'https://api.hduhelp.com/base/student/grade?schoolYear=' + schoolYear + '&semester=' + semester,
                headers=header)

            semester_dict = {'1': '一', '2': '二'}
            res_str = '小语为您查到' + schoolYear + '年第' + semester_dict[semester] + '学期' + str(
                len(r4.json()['data'])) + '门课的成绩：\n——————————————————\n'
            num = 0  # 总学分
            ave = 0  # 平均绩点
            temp_jidian = -1
            for item in r4.json()['data']:
                temp_arr = []
                res_str += str(item['COURSE']) + '  学分:' + (item['CREDIT']) + '\n'
                if item['SCORE_PS'] is not None:
                    temp_arr.append('平时成绩:' + str(item['SCORE_PS']).replace("\n", ""))
                if item['SCORE_QZ'] is not None:
                    temp_arr.append('期中成绩:' + str(item['SCORE_QZ']).replace("\n", ""))
                if item['SCORE_QM'] is not None:
                    temp_arr.append('期末成绩:' + str(item['SCORE_QM']).replace("\n", ""))
                if item['SCORE'] is not None and item['SCORE_QZ'] is None:
                    temp_arr.append('最终成绩:' + str(item['SCORE']).replace("\n", ""))
                temp_jidian = 5 - (95 - float(item['SCORE'])) * (float(item['SCORE']) <= 95)
                temp_arr.append('绩点:' + str(temp_jidian).replace("\n", ""))

                for i in range(len(temp_arr)):
                    if i % 2 == 0:
                        res_str += temp_arr[i] + "  "
                    else:
                        res_str += temp_arr[i] + '\n'
                res_str += '\n————————————\n'
                score = float(item['SCORE'])
                xuefen = float(item['CREDIT'])
                if score > 95:
                    score = 95
                num += xuefen
                ave += (5 - (95 - score) * 0.1) * xuefen

            if num == 0:
                await da2.send(Message(at_flag + "\n" + "咦，小语发现您这学期还没有成绩呢！"))
            else:
                ave = ave / num
                res_str += '您目前出成绩的总学分为：' + str(num) + '分\n'
                res_str += "您目前平均绩点为：" + str(round(ave, 5))

                await da2.send(Message(at_flag + "\n" + res_str))

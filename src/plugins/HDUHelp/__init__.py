import nonebot
from nonebot import on_keyword, on_command
from nonebot import export, require
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent

from src.plugins.HDUHelp import my_db, grade, login, check, fee, schedule, jiaowuchu, atom_get_class, reminder, fanya
import asyncio

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

scheduler = require('nonebot_plugin_apscheduler').scheduler

jishiqi = 0
jishiqi1 = 0


# da11 = on_command("t")


# @da11.handle()
# async def scheduled_job_handle1(bot: Bot, event: Event, state: T_State):
@scheduler.scheduled_job('cron', day="*", hour="*", minute="*", second=50, id='123')
async def scheduled_job_handle1():
    global jishiqi1
    jishiqi1 += 1
    await atom_get_class.test(jishiqi1)


@scheduler.scheduled_job('cron', day="*", hour="*", minute="*", second=10, id='124')
async def scheduled_job_handle():
    global jishiqi
    jishiqi += 1
    # if jishiqi % 30 == 0:
    print("已帮您监控教务处网站成功持续" + str(jishiqi) + "分钟！")
    sql_session = my_db.db_session()
    # print("hahahaha")
    bot = list(nonebot.get_bots().values())[0]
    await jiaowuchu.sendNewMsg(sql_session)
    sql_session.close()


@scheduler.scheduled_job('cron', day="*", hour="7-23", minute=1, second=0, id='125')
async def electricReminder():
    await reminder.electricFeeReminder(User_Agent)


# test1 = on_command("test")
#
#
# @test1.handle()
# async def scheduled_job_handle1(bot: Bot, event: Event, state: T_State):
#     await atom_get_class.test()


# @scheduler.scheduled_job('cron', day="*", hour="*", minute="*", second="30")
# # async def scheduled_job_handle1():
# #     await atom_get_class.test()
# #


# TODO 添加一个大的try-except
# TODO 添加注销功能
da1 = on_command('登录')


@da1.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    try:
        global User_Agent
        # await da1.send(Message('Start!'))
        # 创建session
        sql_session = my_db.db_session()

        # 数据库里查询数据
        qqid = event.get_user_id()
        if 4 < len(qqid) < 13 and qqid.isdigit():  # 数据过滤
            result = sql_session.query(my_db.qq_bot_hdu).filter_by(qq=qqid).all()
            item = '-1'  # result为空，item则为-1
            for temp in result:
                item = temp
            # print(item)
            if 'private' in event.get_event_name():  # 如果是私聊 就不用at
                at_flag = ""
            else:
                at_flag = f'[CQ:at,qq={qqid}] '
            if item == '-1':
                await da1.send(
                    Message(
                        at_flag + '您未登录,请使用微信进行扫码登录！(二维码两分钟以内有效，需要首先绑定"智慧杭电"账号，具体方法请查看:https://cas.hdu.edu.cn/cas/comm/html/help.html )'))
                await login.login(qqid, da1, sql_session, User_Agent, at_flag)
            else:  # 如果查到有QQ号记录
                if item.token != '':  # 若记录不为空，则检查token有效性
                    await da1.send(Message(at_flag + '正在检查您的Token有效性...'))
                    judge = check.check(item.token, User_Agent)  # 判断用户的token是否有效
                    if judge:
                        await da1.send(Message(at_flag + "您的Token有效，无需重新登录！"))
                if item.token == '' or not judge:  # 若记录为空或token无效，则重新登录
                    await da1.send(Message(at_flag + '您的Token已经过期，请重新扫码登录！(二维码两分钟以内有效)'))
                    await login.login(qqid, da1, sql_session, User_Agent, at_flag)

    except CQHttpError:
        pass


da2 = on_command('成绩')


@da2.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    try:
        if 'private' in event.get_event_name():  # 如果是私聊 就不用at
            at_flag = ""
        else:
            at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        await grade.grade(event.get_user_id(), da2, User_Agent, at_flag)
    except CQHttpError:
        pass


da3 = on_command('电费')


@da3.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    try:
        if 'private' in event.get_event_name():  # 如果是私聊 就不用at
            at_flag = ""
        else:
            at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        await fee.electric_fee(event.get_user_id(), da3, User_Agent, at_flag)
    except CQHttpError:
        pass


da4 = on_command('一卡通')


@da4.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    try:
        if 'private' in event.get_event_name():  # 如果是私聊 就不用at
            at_flag = ""
        else:
            at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        await fee.yikatong_fee(event.get_user_id(), da4, User_Agent, at_flag)
    except CQHttpError:
        pass


da5 = on_command('课表')


@da5.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    try:
        if 'private' in event.get_event_name():  # 如果是私聊 就不用at
            at_flag = ""
        else:
            at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        await schedule.schedule_today(event.get_user_id(), da5, User_Agent, at_flag)
    except CQHttpError:
        pass


da6 = on_command('明日课表')


@da6.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    try:
        if 'private' in event.get_event_name():  # 如果是私聊 就不用at
            at_flag = ""
        else:
            at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        await schedule.schedule_tomorrow(event.get_user_id(), da6, User_Agent, at_flag)
    except CQHttpError:
        pass


da7 = on_command("教务处")


@da7.handle()
async def addUser(bot: Bot, event: Event, state: T_State):
    if 'private' in event.get_event_name():  # 如果是私聊 就不用at
        at_flag = ""
        tempStr = ""
        tempID = event.get_user_id()
    else:
        at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        tempStr = "此群"
        tempID = str(event.get_event_description()).split('群:')[1].split(']')[0]  # 可以获取群号
    sql_session = my_db.db_session()
    users = sql_session.query(my_db.jiaowuchu_user).all()
    # global tempStr1
    # global tempStr2
    for each in users:
        if each.user_id == tempID:
            # print("找到啦")
            await da7.send(Message(at_flag + tempStr + "已经开启教务处消息实时通知功能，无需重复开启！"))
            # tempStr1 = "已经开启"
            # tempStr2 = "关闭"
            break
    else:
        sql_session = my_db.db_session()
        usertype = "user_id" if at_flag == "" else "group_id"
        addUser = my_db.jiaowuchu_user(tempID, usertype)
        sql_session.add(addUser)
        sql_session.commit()
        sql_session.close()
        await da7.send(Message(at_flag + tempStr + "已成功开启教务处消息实时通知功能！"))

    sql_session.close()


da8 = on_command("关闭教务处")


@da8.handle()
async def addUser(bot: Bot, event: Event, state: T_State):
    if 'private' in event.get_event_name():  # 如果是私聊 就不用at
        at_flag = ""
        tempStr = ""
        tempID = event.get_user_id()
    else:
        at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        tempStr = "此群"
        tempID = str(event.get_event_description()).split('群:')[1].split(']')[0]  # 可以获取群号
    sql_session = my_db.db_session()
    users = sql_session.query(my_db.jiaowuchu_user).all()
    # global tempStr1
    # global tempStr2
    for each in users:
        if each.user_id == tempID:
            sql_session = my_db.db_session()
            sql_session.query(my_db.jiaowuchu_user).filter_by(user_id=tempID).delete()
            sql_session.commit()
            sql_session.close()
            await da7.send(Message(at_flag + tempStr + "已成功取消教务处消息实时通知功能！"))
            break
    else:
        await da7.send(Message(at_flag + "当前" + tempStr + "未开启教务处消息实时通知功能，无法关闭！"))

    sql_session.close()


da9 = on_command("泛雅")


@da9.handle()
async def h1(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["args"] = args


@da9.got("args", prompt="请输入您泛雅平台的账号密码(此处建议私聊啦!)(以'用户名#密码'的格式')")
async def handle_city(bot: Bot, event: Event, state: T_State):
    try:
        msg = fanya.bangding(event.get_user_id(), state["args"])
        await da9.send(Message(msg))
    except CQHttpError:
        pass


da10 = on_command("查作业")


@da10.handle()
async def h10(bot: Bot, event: Event, state: T_State):
    try:
        if 'private' in event.get_event_name():  # 如果是私聊 就不用at
            at_flag = ""
        else:
            at_flag = f'[CQ:at,qq={event.get_user_id()}] '
        msg = fanya.checkHomeWork(event.get_user_id())
        await da10.send(Message(at_flag + msg))
    except CQHttpError:
        pass

# @da7.got("Exist", prompt="您" + tempStr1 + "教务处消息实时通知！需要" + tempStr2 + "它吗？\n(1:要;2:不要)")
# async def handle_city(bot: Bot, event: Event, state: T_State):
#     if 'private' in event.get_event_name():  # 如果是私聊 就不用at
#         at_flag = ""
#         tempStr = ""
#         tempID = event.get_user_id()
#     else:
#         at_flag = f'[CQ:at,qq={event.get_user_id()}] '
#         tempStr = "为此群"
#         tempID = str(event.get_event_description()).split('群:')[1].split(']')[0]  # 可以获取群号
#     arg1 = str(event.get_message()).strip()
#     if str(arg1) == "1":
#         sql_session = my_db.db_session()
#         sql_session.query(my_db.jiaowuchu_user).filter_by(user_id=tempID).delete()
#         sql_session.commit()
#         sql_session.close()
#         await da7.send(Message(at_flag + "您已经成功" + tempStr + "取消教务处消息实时通知功能！"))
#     elif str(arg1) == "2":
#         await da7.send(Message(at_flag + "好的，小语会帮您" + tempStr + "保持教务处消息实时通知功能！"))
#     else:
#         await da7.send(Message(at_flag + "错误输入，请输入1或2！"))
#
#
# @da7.got("notExist", prompt="您已经关闭了教务处消息实时通知！需要开启它吗？\n(1:要;2:不要)")
# async def handle_city(bot: Bot, event: Event, state: T_State):
#     if 'private' in event.get_event_name():  # 如果是私聊 就不用at
#         at_flag = ""
#         tempStr = ""
#         tempID = event.get_user_id()
#     else:
#         at_flag = f'[CQ:at,qq={event.get_user_id()}] '
#         tempStr = "为此群"
#         tempID = str(event.get_event_description()).split('群:')[1].split(']')[0]  # 可以获取群号
#     arg1 = str(event.get_message()).strip()
#     if str(arg1) == "1":
#         sql_session = my_db.db_session()
#         usertype = "user_id" if at_flag == "" else "group_id"
#         addUser = my_db.jiaowuchu_user(tempID, usertype)
#         sql_session.add(addUser)
#         sql_session.commit()
#         sql_session.close()
#         await da7.send(Message(at_flag + "您已经成功" + tempStr + "开启教务处消息实时通知功能！"))
#     elif str(arg1) == "2":
#         await da7.send(Message(at_flag + "好的，小语会帮您" + tempStr + "保持教务处消息实时通知功能关闭！"))
#     else:
#         await da7.send(Message(at_flag + "错误输入，请输入1或2！"))

# async def handle_city(bot: Bot, event: Event, state: T_State):
#     print(state)

# loop = asyncio.get_event_loop()
# forecast = loop.run_until_complete(jiaowuchu.sendNewMsg())
# loop.close()

# getLesson = on_command("自动抢课")
#
#
# @getLesson.handle()
# async def handle_first_receive(bot: Bot, event: Event, state: T_State):
#     arg1 = str(event.get_message()).strip()
#     arg2 = str(event.get_message()).strip()
#     if arg1 and arg2:
#         state["getLesson"] = arg1
#         state["getLe"] = arg2
#
#
# @getLesson.got("getLesson", prompt="您想做什么操作呀")
# async def handle_city(bot: Bot, event: Event, state: T_State):
#     print(state)

# print("您？")
# @getLesson.got("getLe", prompt="您?")
# async def handle_city(bot: Bot, event: Event, state: T_State):
#     print(state)

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
import asyncio
from nonebot.rule import to_me
import requests
from aiocqhttp.exceptions import Error as CQHttpError
import random
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
from nonebot import require
import nonebot

dingshi = on_command("定时")  # on_command会检测以/开头的词语


@dingshi.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["dingshiLong"] = args


@dingshi.got("dingshiLong", prompt="请按(xxh xxmin xxs)格式输入定时的时间(仅支持整数）")
async def handle_city(bot: Bot, event: Event, state: T_State):
    dingshiLong = state["dingshiLong"]
    s, hour, min, second = my_split(dingshiLong)
    temp = time.strftime('%Y-%m-%d %H:%M:%S',
                         time.localtime(time.time() + int(hour) * 3600 + int(min) * 60 + int(second)))
    user_id = event.get_user_id()
    # print(user_id)
    with open('timing.txt', 'w') as f1:
        # f1.write('0:' + temp + str(hour) + str(min) + str(second) + "id:" + user_id + '\n')
        f1.write('hahahaha')
        print(user_id)
        f1.close()
    # print(user_id)

    await dingshi.send(s)

    if s != '您输入的时间格式有误，已为您退出定时功能':
        timing = hour * 3600 + min * 60 + second
        await my_send(hour, min, second)


async def my_send(hour, min, second):
    await asyncio.sleep(hour * 3600 + min * 60 + second)
    temp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - (hour * 3600 + min * 60 + second)))
    for i in range(2):
        await asyncio.sleep(3)
        await dingshi.send(message=f'您于{temp}时设定的长为{hour}时{min}分{second}秒的闹钟时间已到啦！',
                           at_sender=True)


async def read_history():
    hours = []
    mins = []
    seconds = []
    timestamps = []
    ids = []

    with open('timing.txt', 'r') as f2:  # 把历史文档中的时间读取出来，转化成时间戳，和当前时间对比后生成对应还剩多少小时、分钟和秒
        s = 0
        for line in f2.readlines():
            accurate_time = str(line[2:line.find('id:') - 3])
            # print(accurate_time)
            time_array = time.strptime(accurate_time, "%Y-%m-%d %H:%M:%S")
            timestamps.append(int(time.mktime(time_array)))
            deta_time = float(
                str(int(time.mktime(time_array))) + '.' + line[line.find('id:') - 3:line.find('id:')]) - time.time()
            if deta_time > 0:
                hours.append(deta_time // 3600)
                mins.append((deta_time - (deta_time // 3600) * 3600) // 60)
                seconds.append(
                    deta_time - (deta_time // 3600) * 3600 - ((deta_time - (deta_time // 3600) * 3600) // 60) * 60)

                ids.append(line[line.find('id:') + 3:].strip('\n'))

                await my_send(hours[s], mins[s], seconds[s])
            s += 1


@on_keyword({"查看"}, rule=to_me()).handle()
async def temp_func(bot: Bot, event: Event, state: T_State):
    await on_keyword({"查看"}, rule=to_me()).send("success!")
    await read_history()


def my_split(dingshiLong):
    flag = ''
    hour = 0
    min = 0
    second = 0
    temp = dingshiLong.split('h')
    if len(temp) == 1:
        temp = temp[0].split('min')
        if len(temp) == 1:
            second = temp[0].split('s')[0]
        elif len(temp) == 2:
            min = temp[0]
            second = temp[1].split('s')[0]
        else:
            flag = '您输入的时间格式有误，已为您退出定时功能'
    elif len(temp) == 2:
        hour = temp[0]
        temp = temp[1].split('min')
        if len(temp) == 1:
            second = temp[0].split('s')[0]
        elif len(temp) == 2:
            min = temp[0]
            second = temp[1].split('s')[0]
        else:
            flag = '您输入的时间格式有误，已为您退出定时功能'
    else:
        flag = '您输入的时间格式有误，已为您退出定时功能'

    if second == '':
        second = '0'

    try:
        if flag != '':

            return flag, int(hour), int(min), int(second)
        else:
            temp = time.strftime('%Y-%m-%d %H:%M:%S',
                                 time.localtime(time.time() + int(hour) * 3600 + int(min) * 60 + int(second)))
            return f'已为您设好闹钟，将在{temp}时@您', int(hour), int(min), int(second)
    except:
        return '您输入的时间格式有误，已为您退出定时功能', 0, 0, 0



# scheduler = require('nonebot-plugin-apscheduler').scheduler
#
#
# @scheduler.scheduled_job('cron', minute='*/20', id='sleep1')
# async def co():
#     bot = nonebot.get_bots()['1755722996']
#     return await bot.send('hahahaha')


# scheduler = BlockingScheduler()
# # 每隔 1分钟 运行一次 job 方法
# # scheduler.add_job(job, 'interval', minutes=1, args=['job1'])
# # 在 2019-08-29 22:15:00至2019-08-29 22:17:00期间，每隔1分30秒 运行一次 job 方法
# scheduler.add_job(job, 'interval', seconds=30, start_date='2021-08-17 11:33:00',
#                   end_date='2021-08-17 11:35:00', args=['job2'])
#
# scheduler.start()
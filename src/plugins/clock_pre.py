# from nonebot.typing import T_State
# from nonebot import on_keyword
# from nonebot.adapters import Message, Bot, Event
# import requests
# from aiocqhttp.exceptions import Error as CQHttpError
# import random
# from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
# import time
# import asyncio
#
#
# async def my_send(hour, min, second):
#     await asyncio.sleep(hour * 3600 + min * 60 + second)
#     temp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     for i in range(2):
#         await asyncio.sleep(3)
#         await da.send(message=f'您于{temp}时设定的长为{hour}时{min}分{round(second)}秒的闹钟时间已到啦！',
#                       at_sender=True)
#
#
# async def read_history():
#     hours = []
#     mins = []
#     seconds = []
#     timestamps = []
#     ids = []
#
#     with open('timing.txt', 'r') as f2:  # 把历史文档中的时间读取出来，转化成时间戳，和当前时间对比后生成对应还剩多少小时、分钟和秒
#         s = 0
#         for line in f2.readlines():
#             accurate_time = str(line[2:line.find('id:') - 3])
#             # print(accurate_time)
#             time_array = time.strptime(accurate_time, "%Y-%m-%d %H:%M:%S")
#             timestamps.append(int(time.mktime(time_array)))
#             deta_time = float(
#                 str(int(time.mktime(time_array))) + '.' + line[line.find('id:') - 3:line.find('id:')]) - time.time()
#             if deta_time > 0:
#                 hours.append(deta_time // 3600)
#                 mins.append((deta_time - (deta_time // 3600) * 3600) // 60)
#                 seconds.append(
#                     deta_time - (deta_time // 3600) * 3600 - ((deta_time - (deta_time // 3600) * 3600) // 60) * 60)
#
#                 ids.append(line[line.find('id:') + 3:].strip('\n'))
#                 # print(hours[s], mins[s], seconds[s])
#                 await my_send(hours[s], mins[s], seconds[s])
#                 s += 1
#
#
# da = on_keyword({"查看"})
#
#
# @da.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     await da.send('success!')
#     await read_history()

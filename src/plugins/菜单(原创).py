from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
import json
from aiocqhttp.exceptions import Error as CQHttpError
import re

menu = on_command("菜单")
# menu = on_keyword({"你能干什么", "你能做什么", "你有什么能力", "你能干啥", "菜单"})


# @menu.handle()
# async def handle_first_receive(bot: Bot, event: Event, state: T_State):
#     args = str(event.get_message()).strip()
#     ls = ['/1', '/2', '/3', '/4', '/5', '/6', '/7']
#     if args in ls:
#         state["index"] = args


# catalog = "欢迎查看我的菜单！" + '\n' + "发送'/'+对应数字可以查看某项功能说明;" + '\n' + "发送'/all'查询所有功能." + '\n' + '1.戳一戳' \
#           + '\n' + '2.简单对话' + '\n' + '3.点歌' + '\n' + '4.防撤回' + '\n' + '5.常用编程语言运行' + '\n' + '6.查询天气、天气预报' \
#           + '\n' + '7.定闹钟' + '\n' + '8.发图' + '\n' + '9.翻译' + '\n' + '10.笑话&&表情包'


catalog = "欢迎查看我的菜单！" + '\n' '1.戳一戳:可以戳一戳我试试哦！' + '\n' + '2.简单对话:想找我聊天吗？私聊或@我即可开始哦！' + '\n' + '3.点歌:发送“/点歌”即开始点歌哦！' \
          + '\n' + '4.防撤回:我可以防止大家撤回呦，都在同一个群里啦，坦诚相见叭！(仅支持文字消息和图片)' + '\n' + \
          '5.常用编程语言运行:输入“/ ”+编程语言+空格+代码即可开始运行一些简单的程序哦！现支持：Python、Java，C、PHP' + '\n' + \
          '6.查询天气、天气预报:发送“/天气+城市+(今日、3-7日)”即可开始查询天气哦！' + '\n' + '7.定闹钟:发送“/闹钟”即可开始设定闹钟哦！输入指定格式： xxh xxmin xxs，我将会在设定时间的时候@您' \
          + '\n' + '8.发图:不建议在群里使用，详细请询问管理员(LSP请找我 斜眼笑）' + '\n' + '9.翻译:发送”/翻译“可以将中文翻译成英文' + '\n' + \
          '10.笑话&&表情包:我支持发送笑话和表情包哦！对我说：”/笑话“或者”/斗图“或者“/渣男”试试哦！'


@menu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    try:
        await menu.send(Message(catalog))
    except CQHttpError:
        pass

# @menu.got("index", prompt=catalog)
# async def handle_next(bot: Bot, event: Event, state: T_State):
#     index = state["index"]
#     # print(index)
#     my_dict = {
#         '/1': '可以戳一戳我试试哦！',
#         '/2': '想找我聊天吗？私聊或@我即可开始哦！',
#         '/3': '发送“/点歌”即开始点歌哦！',
#         '/4': '我可以防止大家撤回呦，都在同一个群里啦，坦诚相见叭！(仅支持文字消息和图片)',
#         '/5': '输入“/ ”+编程语言+空格+代码即可开始运行一些简单的程序哦！现支持：Python、Java，C、PHP',
#         '/6': '发送“/天气”即可开始查询天气哦！',
#         '/7': '发送“/闹钟”即可开始设定闹钟哦！我将会在设定时间的时候@某人',
#         '/8': '不建议在群里使用，详细请询问管理员',
#         '/9': '发送”/翻译“可以将中文翻译成英文',
#         '/10': '我支持发送笑话和表情包哦！对我说：”/笑话“或者”/斗图“试试哦！'
#
#     }
#     try:
#         await menu.send(my_dict[index])
#     except:
#         if index == '/all':
#             await menu.send(
#                 '1.戳一戳:可以戳一戳我试试哦！' + '\n' +
#                 '2.简单对话:想找我聊天吗？私聊或@我即可开始哦！' + '\n' +
#                 '3.点歌:发送“/点歌”即开始点歌哦！' + '\n' +
#                 '4.防撤回:我可以防止大家撤回呦，都在同一个群里啦，坦诚相见叭！(仅支持文字消息和图片)' + '\n' +
#                 '5.常用编程语言运行:输入“/ ”+编程语言+空格+代码即可开始运行一些简单的程序哦！现支持：Python、Java，C、PHP' + '\n' +
#                 '6.查询天气、天气预报:发送“/天气”即可开始查询天气哦！' + '\n' +
#                 '7.定闹钟:发送“/闹钟”即可开始设定闹钟哦！输入指定格式： xxh xxmin xxs，我将会在设定时间的时候@您' + '\n' +
#                 '8.发图:不建议在群里使用，详细请询问管理员' + '\n' +
#                 '9.翻译:发送”/翻译“可以将中文翻译成英文' + '\n' +
#                 '10.笑话&&表情包:我支持发送笑话和表情包哦！对我说：”/笑话“或者”/斗图“试试哦！'
#             )
#         else:
#             await menu.send("您输入了错误的命令，已为您退出查询。")
# def init_str():  # 请在这里添加你想要你机器人回复你的语句，支持随机回复，只要在对应的rand_ls中加入你想回复的list，然后在talk_word中对应值的地方加入my_rand(rand_ls[i])即可，很简单
#     talk_word = {"/1": "你好呀",
#                  "/2": "下次再见！",
#                  "/3": "啊好舒服~"}
#     return talk_word
#
#
# def main2():
#     print(-1)
#     talk_word = init_str()
#
#     l_t = len(talk_word)
#     k = []
#
#     for i in range(l_t):
#         print(i)
#         k.append(list(talk_word.keys())[i])
#
#         my_send(i, k)  # 这一行代码能写出来花了我一天、对你没听错，整整一天的debug
#
#
# def str2set(s):
#     my_set = set()
#     my_set.add(s)
#     return my_set
#
#
# def my_send(i, k):
#     @on_keyword(str2set(k[i]), rule=to_me()).handle()
#     async def j(bot: Bot, event: Event, state: T_State):
#         try:
#             talk_word = init_str()
#
#             # print(talk_word["我帅吗"])
#             v = talk_word[k[i]]
#
#             # print(i)
#             # print(k + ":" + v)
#             await on_keyword(str2set(k[i]), rule=to_me()).send(
#                 v)  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
#         except CQHttpError:
#             pass
#
#
# menu = on_command('菜单')
#
#
# @menu.handle()
# async def main(bot: Bot, event: Event, state: T_State):
#     catalog = "欢迎查看本美女的菜单，输入'/'+对应数字可以查看说明哦！" + '\n' + '1.戳一戳' + '\n' + '2.简单对话' + '\n' + '3.\\点歌' + '\n' + '4.防撤回' + '\n' + '5.常用编程语言运行' + '\n' + '6.\\查询天气、天气预报' + '\n' + '7.\\闹钟'
#     await menu.send(catalog)
#
#     main2()

# catalog_catalog = "欢迎收看本机器人的菜单"
# catalog_1 = "1.闪照破解"
# catalog_2 = "2.今日人品"
# catalog_3 = "3.二次元图片"
# catalog_4_1 = "4.笑, 哭, 主人, test, "
# catalog_4_2 = "戳一戳, 你是谁, 在吗, 你多大了"
# catalog_4_3 = "你好, 机器人, 晚安, 晚,"
# catalog_4_4 = "晚上好, 早, 午, 智商, 随机头像"
# catalog_5 = "5.cos"
# catalog_6 = "6.日记, 舔狗日记"
# catalog_7 = "7.动漫涩图"
# catalog_8 = "8.精选壁纸"
# catalog_9 = "9.今日人品"
# catalog_10 = "10.美腿, 美图诱惑"
# catalog_11 = "11.戳一戳"
# catalog_13 = "13.防撤回"
# catalog_14 = "14.语录, 一言语录"
# catalog_15 = "15.天气预报"
# catalog_16 = "16.奥运会"
# catalog_17 = "17.哔哩热搜, 微博热搜, 今日哔哩排行"
#
# catalog = str(catalog_catalog + '\n' + catalog_1 + '\n' + catalog_2 + '\n' + catalog_3 + '\n' +
#               catalog_4_1 + '\n' + catalog_4_2 + '\n' + catalog_4_3 + '\n' + catalog_4_4 + '\n' +
#               catalog_5 + '\n' + catalog_6 + '\n' + catalog_7 + '\n' + catalog_8 + '\n' + catalog_9 +
#               '\n' + catalog_10 + '\n' + catalog_11 + '\n' + catalog_13 + '\n' +
#               catalog_14 + '\n' + catalog_15 + '\n' + catalog_16 + '\n' + catalog_17)

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

"""菜单"""

menu = on_keyword({'菜单'})

@menu.handle()

async def main(bot: Bot, event: Event, state: T_State):
    catalog_catalog = "欢迎收看本机器人的菜单"
    catalog_1 = "1.闪照破解"
    catalog_2 = "2.今日人品"
    catalog_3 = "3.二次元图片"
    catalog_4_1 = "4.笑, 哭, 主人, test, "
    catalog_4_2 = "戳一戳, 你是谁, 在吗, 你多大了"
    catalog_4_3 = "你好, 机器人, 晚安, 晚,"
    catalog_4_4 = "晚上好, 早, 午, 智商, 随机头像"
    catalog_5 = "5.cos"
    catalog_6 = "6.日记, 舔狗日记"
    catalog_7 = "7.动漫涩图"
    catalog_8 = "8.精选壁纸"
    catalog_9 = "9.今日人品"
    catalog_10 = "10.美腿, 美图诱惑"
    catalog_11 = "11.戳一戳"
    catalog_13 = "13.防撤回"
    catalog_14 = "14.语录, 一言语录"
    catalog_15 = "15.天气预报"
    catalog_16 = "16.奥运会"
    catalog_17 = "17.哔哩热搜, 微博热搜, 今日哔哩排行"

    catalog = str(catalog_catalog + '\n' + catalog_1 + '\n' + catalog_2 + '\n' + catalog_3 + '\n' +
                  catalog_4_1 + '\n' + catalog_4_2 + '\n' + catalog_4_3 + '\n' + catalog_4_4 + '\n' +
                  catalog_5 + '\n' + catalog_6 + '\n' + catalog_7 + '\n' + catalog_8 + '\n' + catalog_9 +
                  '\n' + catalog_10 + '\n' + catalog_11 + '\n' + catalog_13 + '\n' +
                  catalog_14 + '\n' + catalog_15 + '\n' + catalog_16 + '\n' + catalog_17)
    await menu.send(catalog)






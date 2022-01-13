from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me


"""个人博客"""
matcher = on_keyword({"个人博客"})
#matcher=on_command('',rule=to_me(),priority=5)
@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:face,id=21]"
    await matcher.send(MessageSegment.at(id) + xians + "我的主人pymili的个人博客为：http://47.108.189.192/")

"""ZERO-TWO的家"""
matchers = on_keyword({"ZERO-TWO的网页","ZERO-TWO的家","你的家"})
#matchers=on_command('',rule=to_me(),priority=5)
@matchers.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:face,id=21]"
    await matchers.send(MessageSegment.at(id) + xians + "我的家（网页）是：http://47.108.189.192/ZERO-TWO/")

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''美腿'''
#xians = on_keyword({""})
matcher=on_command('美腿',rule=to_me(),priority=5)
@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/mtt,cache=0,id=40000]"
    await matcher.send(MessageSegment.at(id) + xians + "精选美腿！少看点！")

'''精选美图'''
#xians = on_keyword({""})
matcher=on_command('美图诱惑',rule=to_me(),priority=5)
@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/mtyh,cache=0,id=40000]"
    await matcher.send(MessageSegment.at(id) + xians + "精选美图诱惑！少看点！")

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

"""cos"""
#xians = on_keyword({"cos"})
matcher=on_command('cos',rule=to_me(),priority=5)
@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/cos,cache=0]"
    await matcher.send(MessageSegment.at(id) + xians + "cos！少看点！")

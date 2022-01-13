from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

"""cos"""
# xians = on_keyword({"cos"})
matcher = on_command('天气降水图', rule=to_me(), priority=5)


@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    {
        "code": 200,
        "img": "http://tianqi-stream.2345cdn.net/tqpc/t/jiankong/2_l.jpg?v=2021080112",
        "tips": "直接返回图片请加参数?type=img"
    }
    xians = f"[CQ:image,file=https://api.iyk0.com/jyu?type=img,cache=0,id=40000]"
    await matcher.send(MessageSegment.at(id) + xians + "天气降水图来了！")

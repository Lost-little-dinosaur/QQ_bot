from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

anime = on_keyword({'动漫'})

@anime.handle()
async def main(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://rc-pximg.glitch.me/img]"
    await anime.send(MessageSegment.at(id) + xians + "动漫，少看点！")
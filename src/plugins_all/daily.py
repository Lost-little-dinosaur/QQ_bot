from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

url = "https://api.iyk0.com/tiangou"
resp = requests.get(url)
# print(resp.text)
txt = resp.text

daily = on_keyword({'日记','舔狗日记'})

@daily.handle()
async def main(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    # xians = f"[CQ:text,file:txt.text]"
    await daily.send(txt)
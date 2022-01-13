from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

url = "https://api.iyk0.com/sg/"
txt = requests.get(url)
# print(txt.text)
text_1 = txt.text

saying = on_keyword({'语录','一言语录'})

@saying.handle()

async def main(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    # xians = f"[CQ:text,file:txt.text]"
    await saying.send(text_1)
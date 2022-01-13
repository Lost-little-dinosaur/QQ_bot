from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
import json
from nonebot.permission import *
from nonebot.rule import to_me

song = on_command("点歌")  # on_command会检测以/开头的词语


@song.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["songName"] = args


@song.got("songName", prompt="你想点什么歌呀小可爱？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    songName = state["songName"]
    url = f"https://api.iyk0.com/wymusic/?msg={songName}&n=1"
    resp = requests.get(url)
    x = resp.text
    r = json.loads(x)
    song_song = r['song']
    singer = r['singer']
    url_url = r['url']
    image = r['img']
    # cq = f"[CQ:music,type=custom,audio={url_url},image={image},title={song_song}]"
    # cq = f"[CQ:music,type=custom,audio={url_url},image={image},title={song_song}]"
    tu = str("歌名：" + song_song + '\n' + "歌手：" + singer + '\n' + "歌曲网址：" + url_url)
    await song.send(tu)

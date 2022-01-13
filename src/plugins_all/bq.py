from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''-------------听歌表情-----------'''

tg = on_keyword({"喜欢听歌吗","听歌吗","听歌"})
#tg=on_command('',rule=to_me(),priority=5)
@tg.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #url = "https://47.108.189.192/image_ZERO-TWO/image/tg.jpg"
    #im = [
    #    {
    #        "type": "image",
    #        "data": {
    #            "file": f"https://thumbnail0.baidupcs.com/thumbnail/618a7fe8fgcd32e4f8eb4fc15902d759?fid=1103052109416-250528-223544311099006&time=1627894800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-MqJF1Z4mQDoCyieWLXb7LaS0c4c%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=345092299236828009&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video"
    #            }
    #        }
    #    ]
    xians = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/618a7fe8fgcd32e4f8eb4fc15902d759?fid=1103052109416-250528-223544311099006&time=1627894800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-MqJF1Z4mQDoCyieWLXb7LaS0c4c%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=345092299236828009&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video]"
    await tg.send(MessageSegment.at(id) + xians + "我很喜欢听歌的！")

'''-------------无聊表情-----------------'''
wl = on_keyword({"无聊"})
@wl.handle()
async def wl_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/d71c3172foea55a9a18a32835e45a3a3?fid=1103052109416-250528-50781226338455&time=1627894800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-O3lIaMdk3hMfMg7mo9CYJNJ4maM%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=345155599591340293&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video]"
    await wl.send(MessageSegment.at(id) + xians + "ZERO-TWO也很无聊！")

'''-----------------疲倦表情---------------------'''
pj = on_keyword({"疲倦","累不累"})
@pj.handle()
async def pj_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/4981559f0v22566a00fd4ca014a423b2?fid=1103052109416-250528-1107318431488395&time=1627894800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-zvOBfXLIYbrJFdE8FshufJhagXg%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=345342104852410473&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video]"
    await wl.send(MessageSegment.at(id) + xians + "很累！")


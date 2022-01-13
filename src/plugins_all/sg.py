from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

sj = on_keyword({"帅哥图片"})
#tg=on_command('',rule=to_me(),priority=5)
@sj.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    xians = f"[CQ:image,file=https://cn.bing.com/images/search?q=%E5%B8%85%E5%93%A5&qs=n&form=QBIR&sp=-1&pq=%E5%B8%85%E5%93%A5&sc=8-2&cvid=6EBFD174AA65451A9249A7202942514A&first=1&tsc=ImageBasicHover,cache=0]"
    await sj.send(MessageSegment.at(id) + tx + xians + "帅哥图片在这里了！")

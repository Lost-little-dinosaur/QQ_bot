from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

xjj = on_keyword({"二次元小姐姐跳舞"})
@xjj.handle()
async def wanns_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    wan = f"[CQ:face,id=180]"
    tp = f"[CQ:video,file=https://v1.kwaicdn.com/upic/2021/08/01/14/BMjAyMTA4MDExNDE0NTVfMjE4MjcwNzE5NF81NDM3MzU5MjY1NF8yXzM=_b_B6cf6eb7f1422157153cb6ef360fd2207.mp4?pkey=AAVTdPaTQqcHenvPe9wBMzdC-0hgjGPTcoO5vgV92Hq9I-VVUjmIfq8YWA60jSr7YYsRejEJYdy-jU9r8l5xQqZeyg1KqZPQSkmuco4Esi4OBjt6j-CVsYOn4oxf20aBYMk&amp;tag=1-1627909197-xpcwebdetail-0-fnnfdm07y2-42befe54e24cbca7&amp;clientCacheKey=3xhx56qpvyxc94a_b.mp4&amp;tt=b&amp;di=7018932c&amp;bp=10004%22]"
    await xjj.send(MessageSegment.at(id) + tp)
    await xjj.send(MessageSegment.at(id) + tx + wan + "这个舞蹈还不学起来！")

ecy = on_keyword({"二次元是我们的敬仰"})
@ecy.handle()
async def ecy_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    wan = f"[CQ:face,id=180]"
    tp = f"[CQ:video,file=https://v2.kwaicdn.com/upic/2021/07/30/20/BMjAyMTA3MzAyMDQ4MzhfMjE0NTQ2MDQ4MF81NDI3MTIyNzQxMF8xXzM=_b_B64fa1d652cec4ff7feb7da9464adc4f6.mp4?pkey=AAXc87dyx3cMx0HNYIhiG2B5y-xEt_6h_NFKFGoTvPSS7EkJikt2VweiAPkAV_dl9XHKdyHOl-BeKZi6wmEOAXJ9tML8YB3KwlIfggOZSXkIbPbvWsxAMm8lXORYk3wky14&amp;tag=1-1627961173-xpcwebdetail-0-893svieodo-f26d3c98fae24b0b&amp;clientCacheKey=3xibs2up8z8vz7w_b.mp4&amp;tt=b&amp;di=7018932c&amp;bp=10004il-0-theaxbf9hf-4e5426630a702ede&amp;clientCacheKey=3xibs2up8z8vz7w_ev3.jpg&amp;di=7018932c&amp;bp=10004]"
    await xjj.send(MessageSegment.at(id) + tp)
    await xjj.send(MessageSegment.at(id) + tx + wan + "这就是二次元！")
# from nonebot import on_keyword, on_command
# from nonebot.typing import T_State
# from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
# from nonebot.adapters.cqhttp.message import MessageSegment
# import requests
# from nonebot.permission import *
# from nonebot.rule import to_me
#
#
# zll_02 = on_keyword({"正能量视频"})
# @zll_02.handle()
# async def zll_r(bot: Bot, event: Event, state: T_State):
#     id = str(event.get_user_id())
#     tx_znl2 = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
#     wan_znl2 = f"[CQ:face,id=180]"
#     await zll_02.send(MessageSegment.at(id) + tx_znl2 + wan_znl2 + "够不够正能量？")
#     await zll_02.send(MessageSegment.video("https://v1.kwaicdn.com/upic/2021/08/01/17/BMjAyMTA4MDExNzQxMzJfMTMzNzQ3NzI5Ml81NDM4NjM1NjU5MF8yXzM=_b_B065072d02d3311df5b6e7936f04d128f.mp4?pkey=AAWgqspUajztNcar43awn76BYqxU5AVzNUa5eJNECQYIWHw6dyo9qcMMbIDK6GjapLPPFsjCwihR-hcRkAnZBlfh9i2D_I_9U4tfo3qEENBmm_b3-WoT3mmJdHJUePAe4Yk&amp;tag=1-1627974027-xpcwebdetail-0-6kjrwnstgb-9dac79c2f45d5448&amp;clientCacheKey=3xagfm8c9aiyqga_b.mp4&amp;tt=b&amp;di=7018932c&amp;bp=10004"))

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

cd = on_keyword({"菜单"})
#cd=on_command('',rule=to_me(),priority=5)
@cd.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    tx = f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]'
    xians = f"https://47.108.189.192/ZERO-TWO/"
    cd_list = ("\n###################################################################\n"\
    	"\n1.help查看所有功能名称\n"\
    	"\n2.我是lsp\n"\
    	"\n3.早上好，晚上好，中午好，晚安，早安\n"\
    	"\n4.你的主人是谁？,官网,礼物,联系方式,随机音乐，你叫什么名字，在吗\n"\
    	"\n5.笑，哭，戳,多大了，你好，男生，开心，ZERO-TWO，编写代码的现实\n"\
    	"\n6.从入门到放弃，随机头像，我是谁，不想学习,几点了，几年，喜欢听歌吗？\n"\
    	"\n7.无聊，累不累，个人博客，ZERO-TWO的家，天气，钢铁侠\n")
    await cd.send(MessageSegment.at(id) + tx + xians + cd_list)

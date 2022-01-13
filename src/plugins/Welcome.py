from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, GroupMessageEvent, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, \
    GroupUploadNoticeEvent, GroupAdminNoticeEvent, GroupRecallNoticeEvent, PokeNotifyEvent,Bot
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot import on_notice, on_command
import warnings,requests
from nonebot.permission import *
warnings.filterwarnings("ignore")

GroupIncrease = on_notice()

# 检测群成员增加
@GroupIncrease.handle()
async def handle_first_receive(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "欢迎"
            }
        },
        {
            "type": "at",
            "data": {
                "qq": f"{event.user_id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "进群"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "欢迎欢迎！进来就是一家人啦！我是本群的美女机器人，可以发送‘/菜单’查询我能干什么哦！"
            }
        },
        {
            "type": "face",
            "data": {
                "id": "13"
            }
        }
    ]
    await bot.send(event=event, message=rely)

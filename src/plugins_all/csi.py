from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

test = on_command('test',rule = to_me())

@test.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    id = str(event.get_user_id())
    at = "[CQ:at,qq={}]".format(id)
    msg = at+'你好呀！'
    msg = Message(msg)
    await test.finish(msg)
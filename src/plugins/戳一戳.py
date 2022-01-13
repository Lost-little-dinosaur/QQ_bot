import random

from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import Event, PokeNotifyEvent
from nonebot.plugin import export

export = export()
export.name = '戳一戳'
export.usage = '该啊\n双击头像触发'

reply = ['戳尼玛呀', '爬', '你再戳，我就把你手剁掉', '别戳了别戳了', '戳你爸',
         '我错了我错了，别戳了', '桥豆麻袋,别戳老子', '手感怎么样', '戳够了吗？该学习了', '戳什么戳，没戳过吗',
         '你用左手戳的还是右手戳的？', '不要啦，别戳啦', '为什么不戳你对象?']
prob = [0.08, 0.08, 0.08, 0.08, 0.08,
        0.08, 0.08, 0.08, 0.08, 0.08,
        0.06, 0.07, 0.07]

poke = on_notice()


@poke.handle()
async def _(bot: Bot, event: Event):
    if isinstance(event, PokeNotifyEvent):
        if event.is_tome() and event.user_id != event.self_id:
            await bot.send(
                event=event,
                message=str(random.choices(reply, weights=prob))[2:-2],
                at_sender=True
            )




# chehui = on_notice()
# @chehui.handle()
# async def cheh(bot:Bot,event:GroupRecallNoticeEvent):
#    if event.get_user_id != event.self_id:
#        await bot.send(
#                event=event,
#                message='喜欢人家就直说啊,我还没说不同意呢~',
#                at_sender=True
#              )

# regbag = on_notice()
#
#
# @regbag.handle()
# async def redb(bot: Bot, event: LuckyKingNotifyEvent):
#     atmsg = MessageSegment.at(event.target_id)
#     await bot.send(
#         event=event,
#         message=atmsg + '恭喜你是运气王',
#     )

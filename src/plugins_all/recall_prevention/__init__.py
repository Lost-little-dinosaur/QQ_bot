#感谢Something For nothing（qq：3330883674）提供的部分源码
from nonebot.adapters.cqhttp import Bot, Event, GroupRecallNoticeEvent
from nonebot.adapters.cqhttp.message import Message
from nonebot.plugin import export, on_notice
from nonebot.rule import Rule
from nonebot.typing import T_State

export = export()
export.name = '防撤回小助手'
export.usage = '你撤回一下就知道了的[]~(￣▽￣)~*'

async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    return isinstance(event, GroupRecallNoticeEvent)

def msg_handler(user_id,recall_message):
    return Message(
        f'[CQ:at,qq={user_id}] 撤回了消息\n——————————————\n{recall_message}'
    )

recall = on_notice(priority=50,rule=Rule(_checker))
@recall.handle()
async def pro(bot: Bot, event: GroupRecallNoticeEvent, state: T_State):
    die_mess = await bot.call_api('get_msg', **{
        'message_id': event.message_id
    })
    if '撤回了消息' in str(die_mess):
        pass
    else:
        recall_message = die_mess['message']
        await recall.send(msg_handler(event.get_user_id(),recall_message))
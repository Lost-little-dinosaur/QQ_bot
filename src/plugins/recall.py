from nonebot.adapters.cqhttp import Bot, Event, GroupRecallNoticeEvent
from nonebot.adapters.cqhttp.message import Message
from nonebot.plugin import export, on_notice
from nonebot.rule import Rule
from nonebot.typing import T_State

export.name = '防撤回小助手'
export.usage = '你撤回一下就知道了的[]~(￣▽￣)~*'


async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    return isinstance(event, GroupRecallNoticeEvent)


recall = on_notice(priority=50, rule=Rule(_checker))


def msg_handler(operator_id, recall_message):
    if "[CQ:record,file=" in recall_message:
        return Message(
            f'[CQ:at,qq={operator_id}] 撤回了消息(被我发现了吧 嘻嘻)：\n撤回了一条语音'
        )
    elif recall_message == '':
        return Message(
            f'[CQ:at,qq={operator_id}] 撤回了消息(被我发现了吧 嘻嘻)：\n撤回了一个视频'
        )
    else:
        return Message(
            f'[CQ:at,qq={operator_id}] 撤回了消息(被我发现了吧 嘻嘻)：\n{recall_message}'
        )


@recall.handle()
async def pro(bot: Bot, event: GroupRecallNoticeEvent, state: T_State):
    die_mess = await bot.call_api('get_msg', **{
        'message_id': event.message_id
    })
    '''
    recall_message = die_mess['message']
    id=die_mess['sender']['user_id']
    # 如果是机器人防撤回后管理员可以再撤回
    if id!=3330883674:
        if id != 3381791244:
            time.sleep(1)
            await recall.send(msg_handler(event.operator_id, recall_message))
    '''
    operator_id = event.get_user_id()
    if '撤回了消息' in str(die_mess):
        pass
    elif str(operator_id) != '1755722996' and str(operator_id) != '2965077320' and str(
            operator_id) != '3144794112' and str(event.group_id) != '228089083':  # TODO:如果不在群里显示撤回，可以发给自己
        recall_message = die_mess['message']
        await recall.send(msg_handler(operator_id, recall_message))

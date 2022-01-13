from nonebot.adapters.cqhttp import Bot, Event, GroupUploadNoticeEvent
from nonebot.adapters.cqhttp.message import Message
from nonebot.plugin import export, on_notice
from nonebot.rule import Rule
from nonebot.typing import T_State


export = export()
export.name = '群文件上次提醒'
export.usage = '上传文件就知道了[]~(￣▽￣)~*'


async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    return isinstance(event, GroupUploadNoticeEvent)

group_up = on_notice(priority=51,rule=Rule(_checker))



@group_up.handle()
async def handle_first_receive(bot: Bot, event: GroupUploadNoticeEvent, state: T_State):
    rely= f'[CQ:at,qq={event.user_id}]\n' \
          f'[CQ:image,file=https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640]' \
          f'\n 上传了新文件，感谢你一直为群里做贡献呀！02给您点赞！[CQ:face,id=13]'
    await group_up.finish(Message(rely))


from nonebot import on_startswith, on_command
from nonebot.adapters.cqhttp import Bot, MessageEvent, Message, Event
from nonebot.typing import T_State
from nonebot.plugin import export
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.rule import Rule
import requests
import time
import random
import string
import hashlib

export = export
export.name = '翻译'
export.usage = '/翻译'

''''''


async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    return isinstance(event, MessageEvent)


tran = on_command('翻译', priority=59, rule=Rule(_checker))


@tran.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["translate"] = args


@tran.got("translate", prompt="请问您要翻译的句子是？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    translate = state["translate"]
    url = f'https://api.iyk0.com/qqfy/?msg={translate}'
    resp = requests.get(url).json()
    result = resp['result']
    id = event.get_user_id()
    result = '中译英翻译的结果为：\n——————————————\n' + result
    result = Message(result)

    try:
        await tran.send(message=result, at_sender=True)
    except CQHttpError:
        pass

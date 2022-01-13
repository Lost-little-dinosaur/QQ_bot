from nonebot.adapters.cqhttp import Message, PokeNotifyEvent, Bot, Event
from nonebot import on_notice
import warnings
from nonebot.permission import *
import requests
warnings.filterwarnings("ignore")
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.plugin import export
from nonebot.rule import Rule
from nonebot.typing import T_State


export.name = '戳一戳'
export.usage = '戳一下就知道了的[]~(￣▽￣)~*'


async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    return isinstance(event, PokeNotifyEvent)

poke = on_notice(priority=50,rule=Rule(_checker))


@poke.handle()
async def _(bot: Bot, event: PokeNotifyEvent):
    if event.is_tome() and event.user_id != event.self_id:
        msg=await kua()
        # chuo = f"[CQ:tts,text={msg}]"
        try:
            await poke.send(Message(f'{Message(msg)}'))
        except CQHttpError:
            pass

async def kua():
    url = 'https://api.sunweihu.com/api/yan/api.php?charset=utf-8'
    resp = requests.get(url).text
    return resp
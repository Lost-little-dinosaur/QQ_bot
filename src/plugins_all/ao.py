# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/2
"""
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # ������û�õı�ɾ
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import requests

ao=on_keyword({'���˻�'})
@ao.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await ao.send(message=Message(msg))

    except CQHttpError:
        pass

async def ji():
    url = 'https://api.cntv.cn/olympic/getOlyMedals'
    params = {
        'serviceId': 'pcocean',
        'itemcode': 'GEN-------------------------------',
    }

    json = requests.get(url, params=params).json()

    # print(json)
    r= json['data']['medalsList']
    # print(r)
    # for r in result[0:6]:
    #     return str(['rank']+r['countryname'].ljust(10))+str('��:')+ str(r['gold']+str('��:') + r['silver']+str('ͭ:') + r['bronze']+str('��:') + r['count'])
    return (r[0]['rank']+r[0]['countryname'].ljust(10)+'��' +str(r[0]['gold'])+ '��' + str(r[0]['silver'])+'ͭ' + str(r[0]['bronze'])+'��:' + str(r[0]['count'])+'\n'+r[1]['rank']+r[1]['countryname'].ljust(10)+'��' +str(r[1]['gold'])+ '��' + str(r[1]['silver'])+'ͭ' + str(r[1]['bronze'])+'��' + str(r[1]['count'])+'\n'+r[2]['rank'] +r[2]['countryname'].ljust(10) + '��' + str(r[2]['gold']) + '��' + str(r[2]['silver']) + 'ͭ' + str(r[2]['bronze']) + '��' + str(r[2]['count']))


from nonebot_plugin_apscheduler import scheduler
from nonebot import require
import nonebot
import requests

require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', hour='10', minute='40', id='sleep4')
async def co():
    # d = time.strftime("%m-%d %H:%M:%S", time.localtime())
    url = 'http://apis.juhe.cn/simpleWeather/query?city=南京&key=a8b3dd5052f0e3e2dff14175165500d6'
    data = requests.get(url=url, timeout=5).json()
    # to=resp['result']['future'][0]
    t = "时间：" + data['result']['future'][0]['date']
    w = "温度:" + data['result']['future'][0]['temperature']
    e = "天气：" + data['result']['future'][0]['weather']
    f = "风向：" + data['result']['future'][0]['direct']

    a = "时间：" + data['result']['future'][1]['date']
    b = "温度:" + data['result']['future'][1]['temperature']
    c = "天气：" + data['result']['future'][1]['weather']
    g = "风向：" + data['result']['future'][1]['direct']
    tu = str(t + '\n' + w + '\n' + e + '\n' + f + '\n\n' + a + '\n' + b + '\n' + c + '\n' + g)

    bot = nonebot.get_bots()['2494889694']
    return await bot.call_api('send_msg', **{
        'message': '天气预报：\n{}'.format(tu),
        'user_id': '1410613164'
    })

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
# matcher = on_keyword({"主人"})
# matcher = on_command({'你是谁'}, rule=to_me(), priority=5)
#
# @matcher.handle()
# async def _(bot: Bot, event: Event, state: T_State):
#     await matcher.send('我是zwh的机器人')

# matcher = on_keyword({'转专业'})
#
# @matcher.handle()
# async def _(bot: Bot, event: Event, state: T_State):
#     await matcher.send('转专业一般只需要满足不挂科，一般的学院转专业只需要2.8即可，管理学院可能会3.x，具体可看转专业文件。成绩占百分之40，面试占百分之五十。')

test = on_keyword({"test"})


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    # hongbao=f"[CQ:gift,qq={id},id=8]"#礼物使用
    await test.send(MessageSegment.at(id) + '你好帅哥')


# test = on_keyword({"礼物", '我要礼物', '我也要礼物'})
test=on_command('礼物',rule=to_me(),priority=5)

@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    hongbao = f"[CQ:gift,qq={id},id=1]"  # 礼物使用
    await test.send(MessageSegment.at(id) + hongbao)


test = on_keyword({'笑'})
test = on_command('笑',rule=to_me())

@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqing = f"[CQ:face,id=182]"  # 表情包使用
    await test.send(MessageSegment.at(id) + biaoqing + '哈哈，笑死我了')


test = on_keyword({'哭'})
test = on_command('哭',rule=to_me())


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqing = f"[CQ:face,id=5]"  # 表情包使用
    await test.send(MessageSegment.at(id) + biaoqing + '呜呜，我真的哭了')


# test = on_keyword({'随机音乐'})
test = on_command('随机音乐',rule=to_me(),priority=5)

@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    url='https://api.paugram.com/acgm/'
    resp = requests.get(url).json()
    ge = resp.get('link')
    # print(ge)
    pic=resp.get('cover')
    # print(pic)
    ming=resp.get('title')
    # print(ming)
    # ci=resp.get('lyric')
    yinyue = f"[CQ:music,type=custom,audio={ge},title={ming},image={pic}]"
    await test.send(Message(yinyue))



test = on_keyword({'戳'})


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # mes = str()
    chuo = f"[CQ:poke,qq={id}]"
    await test.send(Message(chuo))

# ceshi=on_keyword({'测试'})
# @ceshi.handle()
# async def h(bot: Bot, event: Event, state: T_State):
#     shi='http://cdn.video.picasso.dandanjiang.tv/59a7b0d30422084ff04896f1.mp4?sign=c83dd6238ff6fadf01b16e2b7a9e2e8a&t=60782bff'
#     pin= f"[CQ:video,file={shi}]"
#     await ceshi.send(Message(pin))

# weather = on_keyword({'天气预报'})

# @weather.handle()
# async def co(bot: Bot, event: Event, state: T_State):
#     url = 'http://apis.juhe.cn/simpleWeather/query?city=南京&key=a8b3dd5052f0e3e2dff14175165500d6'
#     data = requests.get(url=url, timeout=5).json()
#     # to=resp['result']['future'][0]
#     t = "时间：" + data['result']['future'][0]['date']
#     w = "温度:" + data['result']['future'][0]['temperature']
#     e = "天气：" + data['result']['future'][0]['weather']
#     f = "风向：" + data['result']['future'][0]['direct']

#     a = "时间：" + data['result']['future'][1]['date']
#     b = "温度:" + data['result']['future'][1]['temperature']
#     c = "天气：" + data['result']['future'][1]['weather']
#     g = "风向：" + data['result']['future'][1]['direct']
#     tu = str(t + '\n' + w + '\n' + e + '\n' + f + '\n\n' + a + '\n' + b + '\n' + c + '\n' + g)

#     return await test.send(Message('send_msg', **{
#         'message': '天气预报：\n{}'.format(tu)}))



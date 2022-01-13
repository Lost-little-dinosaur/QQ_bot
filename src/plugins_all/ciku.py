from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''主人'''
matchesr = on_keyword({"主人","你的主人是谁？","你的主人是谁","创造者","pymili","PYmili"})
#matcher=on_command('主人',rule=to_me(),priority=5)
@matchesr.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await matchesr.send('ZERO-TWO：我主人是PYmili')



'''我们的官网'''
matcher=on_keyword({"我们的官网","我们的官网是多少？","官网"})
@matcher.handle()
async def _(bot: Bot, event: Event, state: T_State):
    guabw = "http://47.108.189.192/"
    await matcher.send('ZERO-TWO：我们的官网是'+guabw)



'''艾特自己'''
atzj = on_keyword({"礼物", '我要礼物', '我也要礼物'})
@atzj.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    # hongbao=f"[CQ:gift,qq={id},id=8]"#礼物使用
    await atzj.send(MessageSegment.at(id) + 'ZERO-TWO：你好帅哥')



'''联系方式'''
lxfs = on_keyword({"联系方式","联系你们","怎么联系你们？"})
@lxfs.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    hongbao = f"[CQ:gift,qq={id},id=1]"  # 礼物使用
    await lxfs.send(MessageSegment.at(id) + hongbao)


'''笑'''
xiao=on_keyword({'笑','你给我笑','快笑','笑一笑'})

@xiao.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqing = f"[CQ:face,id=182]"  # 表情包使用
    await xiao.send(MessageSegment.at(id) + biaoqing + 'ZERO-TWO：我可是很高冷的，哼！')



'''苦表情'''
ku=on_keyword({'哭','快哭','你给我哭'})

@ku.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqing = f"[CQ:face,id=5]"  # 表情包使用
    await ku.send(MessageSegment.at(id) + biaoqing + 'ZERO-TWO：不会哭的！')


'''播放随机音乐'''
#test = on_keyword({'随机音乐','放音乐','音乐'})
test=on_command('随机音乐',rule=to_me(),priority=5)

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
    #tg = f"[CQ:image,file=https://47.108.189.192/image_ZERO-TWO/image/tg.jpg]"
    yinyue = f"[CQ:music,type=custom,audio={ge},title={ming},image={pic}]"
    #await test.send(Message(tg))
    await test.send(Message(yinyue) )


'''戳'''
cuo = on_keyword({'戳','戳一戳'})

@cuo.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # mes = str()
    chuo = f"[CQ:poke,qq={id}]"
    await cuo.send(Message(chuo))

'''你是谁'''
you = on_keyword({'你叫什么名字','你是谁','你是谁呀','你是','你到底是谁'})

@you.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await you.send('ZERO-TWO：我是ZERO-TWO，一个聪明的孩子，可以对我说 菜单')


'''在吗'''
matchemr = on_keyword({"在吗", '在不在'})

@matchemr.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await matchemr.send('ZERO-TWO：我在，有什么事吗？ 可以对我说 菜单')

'''age'''
age = on_keyword({"你多大了","age","你现在多大了","你几岁了","你现在几岁了"})
@age.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await age.send('ZERO-TWO：我现在才1岁呢！')

'''hello'''
hello = on_keyword({"你好","你好？","你好呀"})
@hello.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await hello.send("ZERO-TWO：你好呀！我是ZREO-TWO！ 可以对我说 菜单")

'''男，女'''
mesx = on_keyword({"男生还是女生","女生","男生","男孩子","女孩子","男性","女性"})
@mesx.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await mesx.send("ZERO-TWO：我是女生哦！")

'''敷衍回答'''
ou = on_keyword({'哦','嗯','...'})
@ou.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await ou.send('ZERO-TWO：你敷衍我！不理你了！')

'''骂人'''
ma = on_keyword({'妈的','操','草','你妈','傻逼','智障','人工智障','傻','垃圾','辣鸡'})
@ma.handle()
async def i_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqings = f"[CQ:face,id=128544]"
    await ma.send(MessageSegment.at(id) + biaoqings + "ZERO-TWO：骂人是不好的呀！不要骂人呀！")

'''开心'''
kaix = on_keyword({"开心","快乐","心情好"})
@kaix.handle()
async def m_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqings = f"[CQ:face,id=28]"
    await kaix.send(MessageSegment.at(id) + biaoqings + "ZERO-TWO:笑着过一生！")

'''ZERO-TWO'''
ZERO = on_keyword({"ZERO-TWO"})
@ZERO.handle()
async def p_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    ZE = f"[CQ:face,id=21]"
    await kaix.send(MessageSegment.at(id) + ZE + "ZERO-TWO:我在！你要对我说什么？")


'''晚安'''
wan = on_keyword({"晚安"})
@wan.handle()
async def wan_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    wan = f"[CQ:face,id=75]"
    tp = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/3e2faa971la7c21c2e26254f236fd4dc?fid=1103052109416-250528-164475063628102&time=1627894800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-OH%2FoLiTSd6eNnPPRvYNkv1fIyb4%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=345174314066815307&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video]"
    await kaix.send(MessageSegment.at(id) + tp + wan + "晚安！做个好梦呀！")

'''晚上好'''
wnans = on_keyword({"晚上好"})
@wnans.handle()
async def wanns_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    wan = f"[CQ:face,id=180]"
    tp = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/3e2faa971la7c21c2e26254f236fd4dc?fid=1103052109416-250528-164475063628102&time=1627894800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-OH%2FoLiTSd6eNnPPRvYNkv1fIyb4%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=345174314066815307&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video]"
    await kaix.send(MessageSegment.at(id) + tp + wan + "晚上好呀，要早点睡觉哦！")


'''早上好'''
zao = on_keyword({"早上好","早安","早！"})
@zao.handle()
async def zao_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    zao = f"[CQ:face,id=21]"
    await kaix.send(MessageSegment.at(id) + zao + "早安！今天又是美好的一天！")

'''中午好'''
zowu = on_keyword({"中午好","午安","午！"})
@zowu.handle()
async def zowu_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    zowu = f"[CQ:face,id=74]"
    await kaix.send(MessageSegment.at(id) + zowu + "午安！下午也要精神满满呀！")


"""编写代码的现实！"""
xians = on_keyword({"编写代码的现实"})
@xians.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/75bccc93av186d77ccfa397f97611c1e?fid=1103052109416-250528-806994574993880&time=1627650000&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-erK1YT78m2OePdWKNO8JGpngfHc%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=279513087501744700&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video,id=40000]"
    await kaix.send(MessageSegment.at(id) + xians + "这就是现实！")

'''----------------------------------------------------词汇--------------------------------------------------------------'''
"""HELP"""
#helps = on_keyword({"帮助","help","HELP","你会什么","你能做什么"})
#@helps.handle()
#async def helps_r(bot: Bot, event: Event, state: T_State):
#    id = str(event.get_user_id())
#    xians = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/26697fd2fkcfc3d058d34cdc63e6409d?fid=1103052109416-250528-1042012666608843&time=1627707600&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-oBFhMjipA9jjy3SAziCtAycsksI%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=294975967151357752&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video,id=40000]"
#    await kaix.send(MessageSegment.at(id) + xians + "查询天气可以输入：天气,打招呼：早上好，晚上好，中午好，晚安，你好，在吗，你是谁.等待完善。。。。。"+
#                    "01，编写代码的现实，02，从入门到放弃，03，戳")


'''-----从入门到放弃------'''
rm = on_keyword({"从入门到放弃","还没入门就放弃"})
@rm.handle()
async def helps_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=http://47.108.189.192/wp-content/uploads/2021/07/6abfd2e45462fa83-300x300.jpg,cache=0]"
    await kaix.send(MessageSegment.at(id) + xians + "少年你渴望力量吗？")


'''---------回复-----------'''
hfu = on_keyword({"你怎么知道你聪明","智商","知道聪明"})
@hfu.handle()
async def hfu_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/mn/2,cache=0,id=40000]"
    await hfu.send(MessageSegment.at(id) + xians + "我可是很聪明的！智商..... 智商可以吃吗？")


'''---------------随机qq头像---------------'''
txiang = on_keyword({"随机头像","头像","QQ头像","qq头像"})
@txiang.handle()
async def txiang_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/jxtx,cache=0,id=40000]"
    await hfu.send(MessageSegment.at(id) + xians + "头像都是随机生成的哦！")


'''---------------随机美图---------------'''
txiangs = on_keyword({"随机美图","美图"})
@txiangs.handle()
async def txiang_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/mn/2,cache=0,id=40000]"
    await hfu.send(MessageSegment.at(id) + xians + "美图都是随机生成的哦！")

'''---------------------LSP------------------------'''
LSPs = on_keyword({"LSP","我是LSP","lsp","我是LSP"})
@LSPs.handle()
async def SLP_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    zp = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/5aa78152eqedb9b4854e476901e91dd8?fid=1103052109416-250528-722734976993320&time=1627743600&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-8gCA6xiHo%2F87DDhrXqFOl4IN6QY%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=304557084170085043&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video,cache=0,id=40000]"
    xians = f"[CQ:face,id=179]"
    await hfu.send(MessageSegment.at(id) + zp + xians +"没想到你是LSP！你可以对我说：随机美图，cos,美图诱惑，美腿，美女图片，手机美女，随机二次元图片")

'''-------------------------随机美女图片----------------------------------'''
mntp = on_keyword({"随机美女图片","美女图片","美女"})
@mntp.handle()
async def mntp_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/sjmn,cache=0,id=40000]"
    await hfu.send(MessageSegment.at(id) + xians + "美女图片都是随机生成的哦！")


'''------------------------------我是谁---------------------------------'''
wss = on_keyword({"我是谁","我是"})
@wss.handle()
async def wss_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:face,id=183]"
    await wss.send("你是" + MessageSegment.at(id) + xians + "真可爱！")


'''---------------------------------表情轰炸----------------------------------'''
#bqhz = on_keyword({"表情轰炸","所有表情"})
#@bqhz.handle()
#async def wss_r(bot: Bot, event: Event, state: T_State):
    #id = str(event.get_user_id())
    #ids = 
    #xians = f"[CQ:face,id=0],[CQ:face,id=(ids)]"
    #await wss.send(MessageSegment.at(id) + xians + "我的所有表情！")

'''-------------------------随机二次元图片----------------------------------'''
#mntp = on_keyword({"随机二次元图片","二次元图片","二次元"})
mntp=on_command('随机二次元图片',rule=to_me(),priority=5)
@mntp.handle()
async def mntp_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/ecy/api.php,cache=0,id=40000]"
    await hfu.send(MessageSegment.at(id) + xians + "图片都是随机生成的哦！")


bxxx = on_keyword({"不想学习","学习有什么用","不学习"})
@bxxx.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=,cache=0,id=40000]"
    await hfu.send(MessageSegment.at(id) + xians + "不学习等于没技术，没技术等于没工作，没工作等于没生活。没生活等于废材！")
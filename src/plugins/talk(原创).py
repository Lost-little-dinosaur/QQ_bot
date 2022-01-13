import time

from nonebot import on_keyword
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
import random
from nonebot.rule import to_me

'''
这个小插件能已经封装好了一些函数，让你能够十分方便的定制你想要你的机器人回复的语句，只要在下面的talk_word中添加对应的键和值就可以了
别看这么一点代码，我愣是从昨晚搞到今晚。。。（也应该是我比较菜的缘故）  我到现在还没整明白为什么我的一堆检测语句+发送语句封装成一个my_send()函数就可以解决一切bug（手动悲伤）
有懂的大佬可以解释下。。。
有问题或者想交流可以找qq：3144794112
'''


def init_str():  # 请在这里添加你想要你机器人回复你的语句，支持随机回复，只
    # 要在对应的rand_ls中加入你想回复的list，然后在talk_word中对应值的地方加入my_rand(rand_ls[i])即可，很简单
    rand_ls = [['emm怎么说呢？我觉得你长的很安全', "哇世上竟有如此的帅哥，我感觉我爱上你了❤❤❤"],
               ['哇，吓死我了', "哇这绝世容颜。。我都不敢睁眼了"],
               ["哇这绝世容颜。。小女子甚是羡慕", 'emm怎么说呢？我觉得你长的很安全'],
               ["癞蛤蟆也想吃天鹅肉？", "啊！终于等到这一天了！！我愿意！！！"],
               ["爸爸！", '爬', '人家还是想喊你老公啦。。。']
               ]
    talk_word = {"你好": "你好呀",
                 "再见": "下次再见！",
                 "我操": "啊好舒服~",
                 "卧槽": "啊~爽！",
                 "woc": "嗯！别停。。",
                 "你多大": "我18呢",
                 "你几岁": "小女子18岁",
                 "我帅吗": my_rand(rand_ls[0]),
                 "我颜值": my_rand(rand_ls[1]),
                 "我美吗": my_rand(rand_ls[2]),
                 "睡觉": "晚安啦,今天一定要好梦哦！",
                 "晚安": "晚安啦,今天一定要好梦哦！",
                 "做我女朋友": my_rand(rand_ls[3]),
                 "在吗": "在的呢",
                 "你是男": "哎呀，讨厌~人家是个小女生啦",
                 "你是女": "哎呀，讨厌~人家是个小女生啦",
                 "你性别": "哎呀，讨厌~人家是个小女生啦",
                 "我想跟你做爱": "我可不是一个轻薄的女生，不理你了。。哼！",
                 "亲一个": "mua~❤❤ mua~❤❤",
                 "抱抱": "快到我怀里来~",
                 '叫爸爸': my_rand(rand_ls[4])
                 }
    return rand_ls, talk_word


def main():
    random.seed(time.time())

    rand_ls, talk_word = init_str()

    l_t = len(talk_word)
    k = []

    for i in range(l_t):
        k.append(list(talk_word.keys())[i])

        my_send(i, k)  # 这一行代码能写出来花了我一天、对你没听错，整整一天的debug


def my_rand(ls):  # 输入列表，随机打乱列表后返回第一个
    random.seed(random.random() * 10)
    random.shuffle(ls)
    return ls[0]


def str2set(s):
    my_set = set()
    my_set.add(s)
    return my_set


def my_send(i, k):
    @on_keyword(str2set(k[i]), rule=to_me()).handle()
    async def j(bot: Bot, event: Event, state: T_State):
        try:
            rand_ls, talk_word = init_str()

            # print(talk_word["我帅吗"])
            v = talk_word[k[i]]

            # print(i)
            # print(k + ":" + v)
            await on_keyword(str2set(k[i]), rule=to_me()).send(
                v)  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
        except CQHttpError:
            pass


main()

# k.append(list(talk_word.keys())[1])
#
#
# @on_keyword(str2set(k[1])).handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     try:
#         v = talk_word[k[1]]
#
#         # print(i)
#         # print(k + ":" + v)
#         await on_keyword(str2set(k[1])).send(v)  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
#     except CQHttpError:
#         pass

# for i in talk_word.keys():
# all_m = []
# # for i in range(l_t):
# # global i
# i = 0
# k = list(talk_word.keys())[i]
# my_set = set()
# my_set.add(k)
#
# all_m.append(on_keyword(my_set))
#
#
# @all_m[i].handle()  # https://blog.csdn.net/u012206617/article/details/90445772 @作用参考网址
# async def j(bot: Bot, event: Event, state: T_State):
#     try:
#         # v = list(talk_word.values())[i]
#
#         print(i)
#         # print(k + ":" + v)
#         await all_m[i].send(v)  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
#     except CQHttpError:
#         pass
#
# #
# i = 1
# k = list(talk_word.keys())[i]
# my_set = set()
# my_set.add(k)
#
# all_m.append(on_keyword(k))
#
#
# @all_m[i].handle()  # https://blog.csdn.net/u012206617/article/details/90445772 @作用参考网址
# async def j(bot: Bot, event: Event, state: T_State):
#     try:
#         v = list(talk_word.values())[i]
#         print(i)
#         # print(k + ":" + v)
#         await all_m[i].send("一会儿见！")  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
#     except CQHttpError:
#         pass


# da = on_keyword({"再见"})
#
#
# @da.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     try:
#         await da.send('下次再见！')  # 遇到await时，会挂起去执行后面的函数，可以设置条件结束其运行（前提是后面的函数有async关键字修饰，也为异步函数）
#     except CQHttpError:
#         pass

import asyncio
import datetime
import requests
from bs4 import BeautifulSoup
import nonebot
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from src.plugins.HDUHelp import my_db


async def sendNewMsg(sql_session):
    bot = list(nonebot.get_bots().values())[0]
    users = sql_session.query(my_db.jiaowuchu_user).all()
    resArr = checkNewMsg(sql_session)
    l = len(resArr)
    while l > 0:
        # print("woqu")
        # print(resArr)
        for eachUser in users:
            # print(eachUser.user_id)
            await bot.call_api('send_msg', **{
                eachUser.user_type: eachUser.user_id,
                'message': Message(
                    "教务处新通知：\n" + resArr[l - 1].title + "\n链接：" + resArr[l - 1].url + "：\n时间：" +
                    str(resArr[l - 1].time).split(' ')[0])
            })
            print(("发送通知：教务处新通知：\n" + resArr[l - 1].title + "：\n链接：" + resArr[l - 1].url + "：\n时间：" +
                   str(resArr[l - 1].time).split(' ')[0]) + "\nTo：" + eachUser.user_type + " " + str(eachUser.user_id))
        l -= 1


def checkNewMsg(sql_session):
    # sql_session = my_db.db_session()

    res = requests.get("http://jwc.hdu.edu.cn/tzgg/list.htm")
    res.encoding = 'utf8'
    html = BeautifulSoup(res.text, "lxml")
    # print(html)
    textArr = html.find_all("div", {"id": "wp_news_w105"})
    # print(textArr[0])
    temp = BeautifulSoup(str(textArr[0]), 'lxml')  # 记得加str()类型转换！
    urlArr = []
    titleArr = []
    timeArr = []
    tempArr = temp.findAll("li")
    # print(urlArr)
    for each_li in tempArr:
        # print(each_li)
        each = BeautifulSoup(str(each_li), "lxml").find_all("a")
        # print(each)
        temp = BeautifulSoup(str(each[0]), "lxml")
        titleArr.append(temp.text)
        urlArr.append("http://jwc.hdu.edu.cn/" + temp.find("a").attrs["href"])
        timeArr.append(BeautifulSoup(str(each_li), "lxml").find_all("div", {"class": "fr date"})[0].text)
    # print(timeArr)
    assert len(titleArr) == len(urlArr) == len(timeArr)
    resArr = []
    for i in range(len(titleArr)):
        allContext = sql_session.query(my_db.jiaowuchu).all()
        for each in allContext:
            if each.url == urlArr[i]:  # 如果数据库中的url有和Arr当前遍历中一样的，则不添加
                break
        else:  # 否则执行添加操作（前一个for中如果没有break）
            addContext = my_db.jiaowuchu(urlArr[i], titleArr[i], 0, timeArr[i])
            sql_session.add(addContext)
            try:
                sql_session.commit()
            except:
                sql_session.rollback()
            resArr.append(addContext)
    return resArr

# if __name__ == '__main__':

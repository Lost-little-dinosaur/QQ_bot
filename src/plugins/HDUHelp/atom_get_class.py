from selenium.webdriver.common.by import By
import requests
import nonebot
from nonebot import on_keyword, on_command
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.typing import T_State
from nonebot.adapters import Message, Bot, Event
from nonebot.adapters.cqhttp import message, GroupMessageEvent, Message, MessageEvent
import time
from datetime import datetime

# from src.plugins.HDUHelp import my_db, __init__, check
from selenium import webdriver


def searchLesson(teacherArr, timeArr, lesson, code, JSESSIONID, route, User_Agent, bigClass, gnmkdm, su, xkkz_id):
    # TODO：可以让用户随便输入，先进行模糊搜索

    burp0_url = "https://newjw.hdu.edu.cn:443/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html?gnmkdm=" + gnmkdm + "&su=" + su
    burp0_cookies = {"JSESSIONID": JSESSIONID, "route": route}
    burp0_headers = {"Connection": "close",
                     "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
                     "Accept": "application/json, text/javascript, */*; q=0.01",
                     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "sec-ch-ua-mobile": "?0",
                     "User-Agent": User_Agent,
                     "sec-ch-ua-platform": "\"Windows\"", "Origin": "https://newjw.hdu.edu.cn",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
                     "Referer": "https://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=" + gnmkdm + "&su=" + su,
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
    burp0_data = {"filter_list[0]": lesson,
                  "rwlx": "1",
                  "xkly": "0", "bklx_id": "0", "sfkkjyxdxnxq": "0", "xqh_id": "1", "jg_id": "05", "zyh_id": "0523",
                  "zyfx_id": "wfx", "njdm_id": "2020", "bh_id": "20052320", "xbm": "1", "xslbdm": "7", "mzm": "01",
                  "xz": "4",
                  "bbhzxjxb": "0", "ccdm": "8", "xsbj": "4294967296",
                  "sfkknj": "1", "sfkkzy": "1",
                  "kzybkxy": "0", "sfznkx": "0",
                  "zdkxms": "0", "sfkxq": "0", "sfkcfx": "0", "kkbk": "0", "kkbkdj": "0",
                  "xkxnm": "2022", "xkxqm": "3",
                  "xkxskcgskg": "0", "rlkz": "0", "kklxdm": bigClass, "kch_id": code,
                  "jxbzcxskg": "0", "xkkz_id": xkkz_id, "cxbj": "0", "fxbj": "0"}
    # 生成抢课加密的jxb_ids
    # burp0_data = {"filter_list[0]": lesson, "rwlx": "2", "xkly": "0", "bklx_id": "0",
    #               "sfkkjyxdxnxq": "0", "xqh_id": "1", "jg_id": "05", "zyh_id": "0523", "zyfx_id": "wfx",
    #               "njdm_id": "2020", "bh_id": "20052320", "xbm": "1", "xslbdm": "7", "mzm": "01", "bbhzxjxb": "0",
    #               "ccdm": "8", "xsbj": "4294967296", "sfkknj": "0", "sfkkzy": "0", "kzybkxy": "0", "sfznkx": "0",
    #               "zdkxms": "0", "sfkxq": "0", "sfkcfx": "0", "kkbk": "0", "kkbkdj": "0", "xkxnm": "2021",
    #               "xkxqm": "12", "xkxskcgskg": "1", "rlkz": "0", "kklxdm": bigClass, "kch_id": code, "jxbzcxskg": "0",
    #               "xkkz_id": xkkz_id, "cxbj": "0", "fxbj": "0"}

    res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    # print(res.headers)
    # print(res.text)
    try:
        resArr = []
        for i in range(len(res.json())):
            tempFlag = 0
            if len(teacherArr) > 0:
                for each in teacherArr:
                    if each in res.json()[i]["jsxx"]:
                        tempFlag += 1
                        break
            else:
                tempFlag += 1
            if len(timeArr) > 0:
                for each in timeArr:
                    if each in res.json()[i]["sksj"]:
                        tempFlag += 1
                        break
            else:
                tempFlag += 1
            if tempFlag == 2:
                resArr.append(res.json()[i])
        return resArr, True
    except:
        return [""], False


# def getLesson(jxb_ids, code, xkkz_id, JSESSIONID, route, User_Agent):
#     burp0_cookies = {"JSESSIONID": JSESSIONID, "route": route}
#     burp0_url = "http://newjw.hdu.edu.cn:80/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=" + gnmkdm + "&su=" + su
#     burp0_headers = {"Pragma": "no-cache", "Cache-Control": "no-cache",
#                      "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
#                      "User-Agent": User_Agent,
#                      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#                      "Origin": "http://newjw.hdu.edu.cn",
#                      "Referer": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=" + gnmkdm + "&su=" + su,
#                      "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#                      "Connection": "close"}
#     burp0_data = {
#         "jxb_ids": jxb_ids,
#         "kch_id": code,
#         "qz": "0", }
#     res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
#     # print(res.headers)
#     print(res.text)
#     if "1" in res.text:
#         return True
#     else:
#         return False


class ImportantDataArr:
    def __init__(self, do_jxb_id, lesson, jsxx, jxdd, sksj, code, jxb_id, bigClass, jxbrl):  # yxzrs是选的人数
        self.do_jxb_id = do_jxb_id
        self.lesson = lesson
        self.jsxx = jsxx
        self.jxdd = jxdd
        self.sksj = sksj
        self.code = code
        self.jxb_id = jxb_id
        self.bigClass = bigClass
        self.jxbrl = jxbrl  # 总容量

    def stringData(self):
        res = "课程名称：" + self.lesson + "\ndo_jxb_id：" + self.do_jxb_id + "\njxb_id：" + self.jxb_id + "\n教师：" + self.jsxx + "\n地点：" + self.jxdd + "\n时间：" + self.sksj + "\n总容量：" + self.jxbrl
        return res


class CheckClass:
    def __init__(self, jxb_id, yxzrs):
        self.jxb_id = jxb_id
        self.yxzrs = yxzrs

    def stringData(self):
        res = "jxb_id：" + self.jxb_id + "\n选课人数：" + self.yxzrs
        return res


def getClasNum(lesson, bigClass, JSESSIONID, route, User_Agent, gnmkdm, su):  # 获取选课人数
    burp0_url = "http://newjw.hdu.edu.cn:80/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=" + gnmkdm + "&su=" + su
    burp0_cookies = {"JSESSIONID": JSESSIONID, "route": route}
    burp0_headers = {"Pragma": "no-cache", "Cache-Control": "no-cache",
                     "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
                     "User-Agent": User_Agent,
                     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                     "Origin": "http://newjw.hdu.edu.cn",
                     "Referer": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=" + gnmkdm + "&layout=default&su=" + su,
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                     "Connection": "close"}

    burp0_data = {
        "filter_list[0]": lesson,
        "rwlx": "1",
        "xz": "4",
        "xkly": "0", "bklx_id": "0", "sfkkjyxdxnxq": "0", "xqh_id": "1", "jg_id": "05",
        "zyfx_id": "wfx", "njdm_id_1": "2020", "zyh_id_1": "0523", "zyh_id": "0523", "njdm_id": "2020",
        "bh_id": "20052320", "xbm": "1", "xslbdm": "7", "mzm": "01", "ccdm": "8", "xsbj": "4294967296",
        "sfkknj": "1", "sfkkzy": "1",
        "kzybkxy": "0", "sfznkx": "0", "zdkxms": "0", "sfkxq": "0", "sfkcfx": "0", "kkbk": "0",
        "kkbkdj": "0", "sfkgbcx": "0", "sfrxtgkcxd": "1", "tykczgxdcs": "1",
        "xkxnm": "2022", "xkxqm": "3",
        "kklxdm": bigClass, "bbhzxjxb": "0", "rlkz": "0", "xkzgbj": "0", "kspage": "1", "jspage": "10", "jxbzb": ''}
    resArr = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data).json()[
        'tmpList']  # 判断是否已满
    retArr = []
    for each in resArr:
        tempClass = CheckClass(each["jxb_id"], each["yxzrs"])
        # print(tempClass.stringData())
        retArr.append(tempClass)
    return retArr


async def test(jishi):
    bot = list(nonebot.get_bots().values())[0]
    session = requests.session()
    # 用户专属
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    f1 = open("src/plugins/HDUHelp/NewJWCookie.txt", 'r')
    JSESSIONID, route = f1.readlines()
    JSESSIONID = JSESSIONID.strip("\n")
    route = route.strip("\n")
    # print(JSESSIONID)
    # print(route)
    f1.close()
    # JSESSIONID = "CC8D08A390A56A8976173C9C784B7178"
    # route = "788fe981a00d3208f4c5f02c97adfe46"
    gnmkdm = "N253512"
    su = "20081130"
    # 选课信息
    code = "S0500770"
    name = "操作系统课程实践"
    xkkz_id = "E0BE1EB065FBFA29E0536264A8C04A31"
    # 通识课是10
    # 主修课是01
    # 体育课是05
    # 特殊课是09
    bigClass = "01"
    timeArr = []
    teacherArr = ["顾人舒"]

    resArr, flag = searchLesson(teacherArr, timeArr, name, code, JSESSIONID, route, User_Agent, bigClass, gnmkdm, su,
                                xkkz_id)
    if flag == False:
        await bot.call_api('send_msg', **{
            "user_id": "3144794112",
            'message': "教务系统登录过期！请重新登录"
        })
        route, JSESSIONID = await login()
        resArr, flag = searchLesson(teacherArr, timeArr, name, code, JSESSIONID, route, User_Agent, bigClass, gnmkdm,
                                    su,
                                    xkkz_id)
        f1 = open("src/plugins/HDUHelp/NewJWCookie.txt", 'w')
        f1.write(JSESSIONID + "\n")
        f1.write(route + "\n")
        f1.close()
    # print(resArr)
    classArr = []
    for i in range(len(resArr)):
        # print(i)
        tempClass = ImportantDataArr(resArr[i]["do_jxb_id"], name, resArr[i]["jsxx"],
                                     resArr[i]["jxdd"], resArr[i]["sksj"], code, resArr[i]['jxb_id'],
                                     bigClass, resArr[i]['jxbrl'])
        print(tempClass.stringData())
        classArr.append(tempClass)
    # 检测classArr中的课的总人数是否和选课人数匹配
    retArr = getClasNum(name, bigClass, JSESSIONID, route, User_Agent, gnmkdm, su)
    for i in range(len(classArr)):
        for each in retArr:
            if each.jxb_id == classArr[i].jxb_id:
                if each.yxzrs == classArr[i].jxbrl:
                    print("已满！")
                else:
                    await bot.call_api('send_msg', **{
                        "user_id": "3144794112",
                        'message': f"主人，有可选课程啦！\n课程名称：" + classArr[i].lesson + "\n教师：" + classArr[
                            i].jsxx + "\n地点：" + classArr[i].jxdd + "\n时间：" + classArr[i].sksj + "\n剩余容量：" +
                                   str(int(classArr[i].jxbrl) - int(each.yxzrs))
                    })
    if jishi * 60 == 0:
        await bot.call_api('send_msg', **{
            "user_id": "3144794112",
            'message': "classArr:" + str(len(classArr)) + 'resArr:' + str(len(resArr))
        })


async def login():
    bot = list(nonebot.get_bots().values())[0]
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    login_url = "https://cas.hdu.edu.cn/cas/login?service=http%3A%2F%2Fnewjw.hdu.edu.cn%2Fsso%2Fdriot4login"

    session = requests.session()
    chrome_options = webdriver.ChromeOptions()
    # 携带头信息以及设置无头模式
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("https=47.100.104.247:8080")
    chrome_options.add_argument("http=36.248.10.47:8080")
    chrome_options.add_argument(
        "user-agent=" + User_Agent)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    driver.get(login_url)  # 打开网页 #可能有TIMEOUT问题
    button1 = driver.find_element(By.XPATH, '//*[@id="template_container"]/div/div[1]/a[2]')
    button1.click()
    erwei = "http://" + driver.find_element(By.XPATH, '//*[@id="qrcode"]/img').get_attribute("src")
    print(erwei)
    await bot.call_api('send_msg', **{
        "user_id": "3144794112",
        'message': Message(f"[CQ:image,file=base64://" + erwei.split(',')[1] + "]")
    })
    now_url = driver.current_url
    n = 0
    while 'cas.hdu.edu.cn' in now_url:  # TODO：加一个异步等待
        # print(now_url)
        time.sleep(0.1)
        n += 1
        now_url = driver.current_url
        if n > 1000:
            await bot.call_api('send_msg', **{
                "user_id": "3144794112",
                'message': Message("二维码已过期，请重新输入'/登录'以重新获取二维码！")
            })
            driver.quit()
            return False
    driver.get("https://cas.hdu.edu.cn/cas/login?service=http%3A%2F%2Fnewjw.hdu.edu.cn%2Fsso%2Fdriot4login")
    print(driver.get_cookies())
    temp = driver.get_cookies()
    await bot.call_api('send_msg', **{
        "user_id": "3144794112",
        'message': Message("您已成功登录！")
    })
    driver.quit()
    print(temp[0]['value'] + "  " + temp[1]['value'])
    return temp[0]['value'], temp[1]['value']


if __name__ == '__main__':
    f1 = open("NewJWCookie.txt", 'r')
    print(f1.readlines())

    # await da1.send(Message(at_flag + f"[CQ:image,file=base64://" + erwei.split(',')[1] + "]"))

# jxb_ids = "75a3e8fbbe3cbfbac1879dcad31a468f5bc54561a31e70695668367be8bbe32da643986a90522f21df0b7d9e349ee9f5dff4e93e1230e091c968dda3eb59410ee0a671c8de4027793c494b9484370e0a117ff8c157f4133a0f0db875c5011d9845f8d946ba5758ea4f8a44b40ef30300a2872fe377a4423be1c16ff17d7988c5"
#
# jxb_ids_arr = [""]
# getLesson(jxb_ids, code, xkkz_id, JSESSIONID, route, User_Agent)

# session.cookies['tp_up'] = 'fzomgHUtb-rGRzw2QlyhKbH5URvkn_0cxjA1gTRH8FWeVvocuemT!-367132844'
# res = session.get("https://i.hdu.edu.cn/tp_up/view", headers=header)

# print(res.text)

# 模糊查询代码：
# burp0_url = "http://newjw.hdu.edu.cn:80/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512&su=20081130"
# burp0_cookies = {"JSESSIONID": "39B65B7A9AA05F3AE0156B79D25486F7", "route": "f426d7f9c4fca6b38279ec3fc13d7e6a"}
# burp0_headers = {"Pragma": "no-cache", "Cache-Control": "no-cache",
#                  "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
#                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
#                  "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8", "Origin": "http://newjw.hdu.edu.cn",
#                  "Referer": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=20081130",
#                  "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#                  "Connection": "close"}
# burp0_data = {"filter_list[0]": "\xe6\x95\xb0\xe5\xad\xa6\xe5\xbb\xba\xe6\xa8\xa1", "rwlx": "1", "xkly": "0",
#               "bklx_id": "0", "sfkkjyxdxnxq": "0", "xqh_id": "1", "jg_id": "05", "njdm_id_1": "2020",
#               "zyh_id_1": "0523", "zyh_id": "0523", "zyfx_id": "wfx", "njdm_id": "2020", "bh_id": "20052320",
#               "xbm": "1", "xslbdm": "7", "ccdm": "8", "xsbj": "4294967296", "sfkknj": "1", "sfkkzy": "1",
#               "kzybkxy": "0", "sfznkx": "0", "zdkxms": "0", "sfkxq": "0", "sfkcfx": "0", "kkbk": "0", "kkbkdj": "0",
#               "sfkgbcx": "1", "sfrxtgkcxd": "1", "tykczgxdcs": "1", "xkxnm": "2021", "xkxqm": "12", "kklxdm": "01",
#               "rlkz": "0", "xkzgbj": "0", "kspage": "1", "jspage": "10", "jxbzb": ''}
# requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
# # 模糊查询返回：
# a = {"tmpList": [{"blyxrs": "0", "blzyl": "0", "cxbj": "0", "date": "二○二二年三月一日", "dateDigit": "2022年3月1日",
#                   "dateDigitSeparator": "2022-3-1", "day": "1", "fxbj": "0", "jgpxzd": "1",
#                   "jxb_id": "D10CC7615CEBC3ACE0536264A8C0AEFC", "jxbmc": "(2021-2022-2)-B0714160-2", "jxbzls": "1",
#                   "kch": "B0714160", "kch_id": "B0714160", "kcmc": "数学建模", "kcrow": "1", "kklxdm": "01", "kzmc": "无",
#                   "listnav": "False", "localeKey": "zh_CN", "month": "3", "pageable": True,
#                   "queryModel": {"currentPage": 1, "currentResult": 0, "entityOrField": False, "limit": 15, "offset": 0,
#                                  "pageNo": 0, "pageSize": 15, "showCount": 10, "sorts": [], "totalCount": 0,
#                                  "totalPage": 0, "totalResult": 0}, "rangeable": True, "totalResult": "0",
#                   "userModel": {"monitor": False, "roleCount": 0, "roleKeys": "", "roleValues": "", "status": 0,
#                                 "usable": False}, "xf": "2", "xxkbj": "0", "year": "2022", "yxzrs": "72"},
#                  {"blyxrs": "0", "blzyl": "0", "cxbj": "0", "date": "二○二二年三月一日", "dateDigit": "2022年3月1日",
#                   "dateDigitSeparator": "2022-3-1", "day": "1", "fxbj": "0", "jgpxzd": "1",
#                   "jxb_id": "D10CF5492A27F7F5E0536264A8C00404", "jxbmc": "(2021-2022-2)-C0714160-1", "jxbzls": "1",
#                   "kch": "C0714160", "kch_id": "C0714160", "kcmc": "数学建模", "kcrow": "2", "kklxdm": "01", "kzmc": "无",
#                   "listnav": "False", "localeKey": "zh_CN", "month": "3", "pageable": True,
#                   "queryModel": {"currentPage": 1, "currentResult": 0, "entityOrField": False, "limit": 15, "offset": 0,
#                                  "pageNo": 0, "pageSize": 15, "showCount": 10, "sorts": [], "totalCount": 0,
#                                  "totalPage": 0, "totalResult": 0}, "rangeable": True, "totalResult": "0",
#                   "userModel": {"monitor": False, "roleCount": 0, "roleKeys": "", "roleValues": "", "status": 0,
#                                 "usable": False}, "xf": "2", "xxkbj": "0", "year": "2022", "yxzrs": "23"},
#                  {"blyxrs": "0", "blzyl": "0", "cxbj": "0", "date": "二○二二年三月一日", "dateDigit": "2022年3月1日",
#                   "dateDigitSeparator": "2022-3-1", "day": "1", "fxbj": "0", "jgpxzd": "1",
#                   "jxb_id": "D1050658757A4B68E0536164A8C038E2", "jxbmc": "(2021-2022-2)-C0714160-3", "jxbzls": "1",
#                   "kch": "C0714160", "kch_id": "C0714160", "kcmc": "数学建模", "kcrow": "2", "kklxdm": "01", "kzmc": "无",
#                   "listnav": "False", "localeKey": "zh_CN", "month": "3", "pageable": True,
#                   "queryModel": {"currentPage": 1, "currentResult": 0, "entityOrField": False, "limit": 15, "offset": 0,
#                                  "pageNo": 0, "pageSize": 15, "showCount": 10, "sorts": [], "totalCount": 0,
#                                  "totalPage": 0, "totalResult": 0}, "rangeable": True, "totalResult": "0",
#                   "userModel": {"monitor": False, "roleCount": 0, "roleKeys": "", "roleValues": "", "status": 0,
#                                 "usable": False}, "xf": "2", "xxkbj": "0", "year": "2022", "yxzrs": "73"},
#                  {"blyxrs": "0", "blzyl": "0", "cxbj": "0", "date": "二○二二年三月一日", "dateDigit": "2022年3月1日",
#                   "dateDigitSeparator": "2022-3-1", "day": "1", "fxbj": "0", "jgpxzd": "1",
#                   "jxb_id": "D0E2A8588F90E62CE0536264A8C04178", "jxbmc": "(2021-2022-2)-S0700760-1", "jxbzls": "1",
#                   "kch": "S0700760", "kch_id": "S0700760", "kcmc": "数学建模课程设计", "kcrow": "3", "kklxdm": "01",
#                   "kzmc": "无", "listnav": "False", "localeKey": "zh_CN", "month": "3", "pageable": True,
#                   "queryModel": {"currentPage": 1, "currentResult": 0, "entityOrField": False, "limit": 15, "offset": 0,
#                                  "pageNo": 0, "pageSize": 15, "showCount": 10, "sorts": [], "totalCount": 0,
#                                  "totalPage": 0, "totalResult": 0}, "rangeable": True, "totalResult": "0",
#                   "userModel": {"monitor": False, "roleCount": 0, "roleKeys": "", "roleValues": "", "status": 0,
#                                 "usable": False}, "xf": "2", "xxkbj": "0", "year": "2022", "yxzrs": "98"}],
#      "sfxsjc": "0"}

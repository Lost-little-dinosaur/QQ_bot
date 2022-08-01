import requests
import pickle
import nonebot


def check(token, User_Agent):  # 检查用户token是否有效
    # myBot = nonebot.get_bot()
    # pickle.dump(myBot, a_file)
    # a_file.close()
    # print("Success!")

    check_url = 'https://api.hduhelp.com/infoStream/v3'
    session = requests.session()
    header = {
        "User-Agent": User_Agent,
        "authorization": "token " + token
    }
    r1 = session.get(check_url, headers=header)
    r1.content.decode("utf-8")
    # print(token)
    # print(r1.text)
    # session.cookies['tp_up'] = tp_up
    # r2 = session.get("https://i.hdu.edu.cn/tp_up/view?m=up", headers=header)

    # if r1.json()['msg'] == "unauthorized" or "Pragma" in dict(r2.headers).keys():  # 如果没有authu认证，则返回False
    if "unauthorized" in r1.text:  # 如果没有authu认证，则返回False
        return False
    else:
        return True


if __name__ == '__main__':
    check_url = 'https://api.hduhelp.com/infoStream/v3'
    session = requests.session()
    token = '968021e6-ea14-4f13-8996-2875b3201614'
    header = {
        "authorization": "token " + token
    }
    r1 = session.get(check_url, headers=header)
    # print(token)
    print(r1.text)

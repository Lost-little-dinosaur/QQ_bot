import requests as r
import time
import json
# 导入相关库
 
def check(hero):
    remsg_list = []
    if hero == "":  # 判断输入的字符串是否是空的
        return "您输入无效"
    for type_str in ['qq','wx']:
        source = r.get("https://www.sapi.run/hero/select.php?hero=%s&type=%s" % (hero, type_str)).text
        # get获取，hero英雄，type为qq或wx
        _json = json.loads(source)
        # 返回json格式，转换为字典
        if _json["code"] == "200":
            remsg_list.append(f'————{type_str}区————')
            # code为200，表示返回正常，其余数值则错误
            title = _json["data"]["heroName"]  # 英雄名称
            remsg_list.append("英雄:%s" % title)
            area = _json["data"]["area"]  # 区名称
            areaPower = _json["data"]["areaPower"]  # 区最低战力
            areaTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_json["data"]["areaTime"])))
            # 更新时间是时间戳，这里将时间戳转到时间文本
            remsg_list.append("县/区:%s(%s) %s" % (area, areaPower, areaTime))
            city = _json["data"]["city"]
            cityPower = _json["data"]["cityPower"]
            cityTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_json["data"]["cityTime"])))
            remsg_list.append("市:%s(%s) %s" % (city, cityPower, cityTime))
            province = _json["data"]["province"]
            provincePower = _json["data"]["provincePower"]
            provinceTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_json["data"]["provinceTime"])))
            remsg_list.append("省:%s(%s) %s" % (province, provincePower, provinceTime))
        else:
            return "错误代码：%s %s" % (_json["code"], _json["msg"])
    return '\n'.join(remsg_list)
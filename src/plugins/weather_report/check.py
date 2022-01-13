import json

from .spider import report_analysis_mod1, seven_days


# 读取数据
def load_data():
    with open('database/weather_report.json', 'r') as f:
        data = json.load(f)
    return data


def weather_report():
    all_info = []
    data = load_data()
    # 第一层循环读取群号或QQ号
    for ids in data.keys():
        id_key, id_value = ids.split('&')
        info = data[ids]
        # 第二层循环读取城市名和需提取的信息
        for key in info.keys():
            cityname = key
            keys = info[key]
            all_info.append([
                id_key,
                id_value,
                report_analysis_mod1(cityname, keys, 1)
            ])
    return all_info


def change_schedule(session_id, inputmsg):
    delmode = 0
    # 分析输入信息
    try:
        city, method = inputmsg.split('=')
    except:
        return '您输入的信息有误，请重新检查格式是否为“城市名=检索模式”，例如“北京=详细”'
    # 分析用户id
    if "group" in session_id:
        _, id_value, _ = session_id.split('_')
        id_key = 'group_id'
    else:
        id_value = session_id
        id_key = 'user_id'
    # 分析输入
    if method == '极简':
        keys = ['title', 'temp_range', 'weather']
    elif method == '简单':
        keys = ['title', 'temp_range', 'weather', 'air_quality', 'umbrella']
    elif method == '一般':
        keys = ['title', 'temp_range', 'weather', 'air_quality', 'umbrella', 'UV_index', 'wear']
    elif method == '详细':
        keys = ['title', 'temp_range', 'weather', 'air_quality', 'wear', 'umbrella', 'car_wash', 'UV_index', 'allergy',
                'fishing', 'wear_short', 'travel', 'drying']
    elif method == '删除':
        delmode = 1
    else:
        return '未知检索模式，请输入“极简”、“简单”、“一般”，“详细”中的一种，或“删除”以删除此城市。'
    # 尝试读取原有信息
    nkey = id_key + '&' + id_value
    try:
        data = load_data()
    except:
        data = {}
    try:
        info = data[nkey]
    except:
        info = {}
    # 更新信息
    if delmode:
        info.popitem(city)
        with open('database/weather_report.json', 'w') as f:
            json.dump(data, f)
        return f'您已成功移除{city}的天气预报'
    else:
        info[city] = keys
        data[nkey] = info
        # 写入信息
        with open('database/weather_report.json', 'w') as f:
            json.dump(data, f)
        return f'请检查输出示例与预期是否相符\n\n{report_analysis_mod1(city, keys, 0)}\n\n如有误请检查您输入的城市名称是否正确，并删除此错误的城市'


def check_report(inputmsg):
    try:
        city, method = inputmsg.split('=')
    except:
        return '您输入的信息有误，请重新检查格式是否为“城市名=检索模式”，例如“北京=详细”'

    if method == '今日':
        keys = ['title', 'temp_range', 'weather', 'air_quality', 'wear', 'umbrella', 'car_wash', 'UV_index', 'allergy',
                'fishing', 'wear_short', 'travel', 'drying']
    elif method.endswith('日'):
        days = int(method.rsplit('日')[0])
        return seven_days(city, days)
    else:
        return '未知检索模式，请输入“今日”、“3-7日”中的一种。'

    return report_analysis_mod1(city, keys, 0)

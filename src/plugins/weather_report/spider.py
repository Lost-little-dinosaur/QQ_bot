import datetime, requests
from pypinyin import lazy_pinyin
from lxml import etree


def get_webpage(url):
    UA_camouflage = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'}
    webpage = requests.get(url=url, headers=UA_camouflage).text
    return etree.HTML(webpage)


def report_analysis_mod1(cityname, keys, delta):
    cityname = ''.join(lazy_pinyin(cityname))
    date_raw = datetime.datetime.now() + datetime.timedelta(delta)
    date = date_raw.strftime('%Y%m%d')
    url = f'https://www.tianqi.com/tianqi/{cityname}/{date}.html'
    data = get_webpage(url)
    info = {
        'title_raw': data.xpath('//div[@class="zixun_caltitle"]/span/text()')[0],
        'temp_range': '气温：' + data.xpath('//div[@class="tempbox_left"]/span/text()')[0],
        'weather': '天气：' + data.xpath('//div[@class="tempbox_left"]/span/text()')[1],
        'air_quality': '空气质量：' + data.xpath('//div[@class="tempbox_left"]/span/text()')[3],
        'wear': data.xpath('//div[@class="tempbox_chuanyi"]/span/text()')[0],
        'umbrella': '带伞需求：' + data.xpath('//div[@class="weather_life300"]//p/text()')[0],
        'car_wash': '洗车建议' + data.xpath('//div[@class="weather_life300"]//p/text()')[1],
        'UV_index': '紫外线：' + data.xpath('//div[@class="weather_life300"]//p/text()')[2],
        'allergy': '过敏反应：' + data.xpath('//div[@class="weather_life300"]//p/text()')[3],
        'fishing': '垂钓建议：' + data.xpath('//div[@class="weather_life300"]//p/text()')[4],
        'wear_short': '穿衣建议：' + data.xpath('//div[@class="weather_life300"]//p/text()')[5],
        'travel': '旅行建议：' + data.xpath('//div[@class="weather_life300"]//p/text()')[6],
        'drying': '晾衣建议：' + data.xpath('//div[@class="weather_life300"]//p/text()')[7],
    }
    _, time_proc = info['title_raw'].split('天气预报')
    info['title'] = time_proc + '预报'
    info.pop('title_raw')
    output = [info[key] for key in keys]
    return '\n'.join(output)


def seven_days(cityname, days):
    # 判断天数是否正确
    if not int(days) in [3, 4, 5, 6, 7]:
        return '天数超出可查询范围，请重新输入'
    cityname = ''.join(lazy_pinyin(cityname))
    date_raw = datetime.datetime.now()
    date = date_raw.strftime('%Y%m%d')
    url = f'https://www.tianqi.com/tianqi/{cityname}/{date}.html'
    data = get_webpage(url)
    info = data.xpath('//ul[@class="days_list clearfix"]//span/text()')
    info_out = []
    templist = []
    for i in data.xpath('//div[@class="zixun_caltitle"]/span/text()')[0]:
        try:
            int(i)
            break
        except:
            templist.append(i)
    info_out.append(''.join(templist))
    for i in range(days):
        i *= 14
        info_out.append('——————')
        info_out.append(info[i + 1] + '-' + info[i])  # 星期 0 日期 1
        info_out.append(info[i + 2])  # 天气 2
        info_out.append(info[i + 6] + info[i + 7] + info[i + 8])  # 气温 6 7 8
        info_out.append(info[i + 10] + info[i + 11])  # 风 10 11
        info_out.append('空气质量' + [x for x in info[i + 13].split('\t')][0])  # 空气质量 13
    return '\n'.join(info_out)

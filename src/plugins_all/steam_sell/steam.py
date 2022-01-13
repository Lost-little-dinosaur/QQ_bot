# -*- coding: utf-8 -*-
#鸣谢@倾城两仪式(qq:2118670594)提供的steam查询api
import requests,sqlite3,re
from bs4 import BeautifulSoup
from datetime import date
from threading import Thread

debugmod = True
#对数据库的操作
class DB:
    def __init__(self):
        self.conn = sqlite3.connect("database/steam_sell.db")
        self.cur = self.conn.cursor()
    #检查今日是否已有数据表
    def check_db(self,table_name):
        info = self.cur.execute('select name from sqlite_master where type = "table"')
        for i in info:
            if table_name in i:
                return True
        return False
    #清空原有数据
    def clear_db(self,table_name):
        #如果已有数据表,则表示今日数据已存在,应先清空原数据后再进行写入
        if self.check_db(table_name):
            self.cur.execute(f'DELETE FROM {table_name}')
        #若不存在该数据表,则表示今日数据不存在,应新建该表后在进行写入
        else:
            #注:自上至下依次为id,游戏名,价格,折扣力度(默认为0),好评率(默认为0),测评数量(默认为0),跳转链接
            #注:折扣力度、好评率、测评数量均应为整数或浮点数,以方便于后续进行排序
            self.cur.execute(
            f'''CREATE TABLE "{table_name}" (
            	"id"	INTEGER NOT NULL UNIQUE,
            	"name"	TEXT NOT NULL,
            	"price"	NUMERIC NOT NULL,
                "discount" NUMERIC NOT NULL DEFAULT 0,
                "game_review_summary"   TEXT NOT NULL,
                "game_favorable_rate"	NUMERIC NOT NULL DEFAULT 0,
            	"game_comments_count"	NUMERIC NOT NULL DEFAULT 0,
            	"jump_link"	BLOB NOT NULL,
            	PRIMARY KEY("id" AUTOINCREMENT)
            )''')
        #删除非今日的表
        info = self.cur.execute('select name from sqlite_master where type = "table"')
        for i in info:
            if not ('sqlite_sequence' or table_name) == str(i[0]):
                print(f'{i[0]}已被清除')
                self.cur.execute(f'DROP TABLE {i[0]}')
            print()
        #对操作进行提交
        self.conn.commit()
    #写入数据
    def write_to_db(self,table_name,info_list):
        self.cur.execute(f'''INSERT INTO {table_name} 
                         VALUES ("{info_list[0]}","{info_list[1]}","{info_list[2]}","{info_list[3]}","{info_list[4]}","{info_list[5]}","{info_list[6]}","{info_list[7]}")''')
        #对操作进行提交
        self.conn.commit()
    #查询数据
    def check_from_db(self,table_name,method='default',count=5,max_price=99999,min_price=0):    
        returnmsg = []
        #默认读取排行榜
        if method == 'default':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price}
            ORDER BY id ASC''')
        #默认读取排行榜
        elif method == 'default_reversal':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price}
            ORDER BY id DESC''')
        #读取最高价格
        elif method == 'high_price':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price}
            ORDER BY price DESC''')
        #读取最低价格
        elif method == 'low_price':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price}
            ORDER BY price ASC''')
        #读取评价数最高
        elif method == 'high_comments_count':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price} AND game_comments_count <> 0
            ORDER BY game_comments_count DESC''')
        #读取评价数最低
        elif method == 'low_comments_count':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price} AND game_comments_count <> 0
            ORDER BY game_comments_count ASC''')
        #读取高好评
        elif method == 'high_favorable_rate':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price} AND game_favorable_rate <> 0
            ORDER BY game_favorable_rate DESC''')
        #读取低好评
        elif method == 'low_favorable_rate':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price} AND game_favorable_rate <> 0
            ORDER BY game_favorable_rate ASC''')
        #读取高折扣
        elif method == 'high_discount':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price} AND discount <> 0
            ORDER BY discount DESC''')
        #读取低折扣
        elif method == 'low_discount':
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE price <={max_price} AND price >={min_price} AND discount <> 0
            ORDER BY discount ASC''')
        #尝试以method为游戏名寻找该游戏
        else:
            info = self.cur.execute(f'''
            SELECT * FROM {table_name}
            WHERE name LIKE "%{method}%"
            ORDER BY id ASC''')
        #将info的前count行以字典形式添加至returnmsg里面
        for row in info:
            returnmsg.append(f'总排名:{row[0]}\
                             \n游戏名:{row[1]}\
                             \n价格:   {row[2]}CNY\
                             \n折扣:   -{row[3]}%\
                             \n评价:   {row[4]}\
                             \n好评率:{row[5]}%\
                             \n评价数:{row[6]}\
                             \n跳转链接:{row[7]}')
            if len(returnmsg) >= count:
                break
        return returnmsg            
#num
total_num = 0
#————————以下为爬取部分————————
#鸣谢@倾城两仪式(qq:2118670594)提供的steam查询api
def run(url,db_nt):
    try:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51', 
            'Accept-Language': 'zh-CN '
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text
    except:
        return "爬取网站失败！"
    game_review_summary = []
    game_favorable_rate = []
    game_comments_count = []
    jump_link = []
    table_name = date.today().strftime("%b%d%Y")
    soup = BeautifulSoup(text, "html.parser")
    w = soup.find_all(class_="col search_reviewscore responsive_secondrow")
    for u in w:
        if u.span is not None:
            msg = re.sub('[,%]','',u.span["data-tooltip-html"].split("<br>")[1])
            msg1,_,msg2,_ = msg.split(' ')
            game_review_summary.append(u.span["data-tooltip-html"].split("<br>")[0])
            game_favorable_rate.append(msg1)
            game_comments_count.append(msg2)            
        else:
            game_review_summary.append("暂无评价！")
            game_favorable_rate.append(0)
            game_comments_count.append(0)
            
    link_text = soup.find_all("div", id="search_resultsRows")
    for k in link_text:
        b = k.find_all('a')
    for j in b:
        jump_link.append(j['href'])
        
    global total_num
    num = 0
    name_text = soup.find_all('div', class_="responsive_search_name_combined")
    for z in name_text:
        total_num = total_num + 1
        try:
            name = z.find(class_="title").string.strip()
            if z.find(class_="col search_discount responsive_secondrow").string is None:
                price = z.find(class_="col search_price discounted responsive_secondrow").text.strip().split("¥")
                db_nt.write_to_db(table_name,[total_num, name, price[2].strip(), int((1-float(price[2].strip())/float(price[1]))*100), game_review_summary[num], game_comments_count[num], game_favorable_rate[num], jump_link[num]])
            else:
                price = z.find(class_="col search_price responsive_secondrow").string.strip().split("¥")
                db_nt.write_to_db(table_name,[total_num, name, price[1], 0, game_review_summary[num], game_comments_count[num], game_favorable_rate[num], jump_link[num]])
        except:
            if debugmod:
                print(f'发生错误，序号是{num}')
        num = num + 1
#————————以下为对外的接口部分————————
def check(inputmsg,returnmod = 'p'):
    """将传入的命令进行分析，并调用数据查询模块

    Args:
        inputmsg (str): 去除命令头的用户的输入信息
    """
    #初始参数
    table_name=date.today().strftime("%b%d%Y")
    method='default'
    count=5
    max_price=99999
    min_price=0
    #解析命令
    for msg in inputmsg.split(' '):
        #查看是否是刷新指令
        if msg.startswith('刷新'):
            c = re.sub('\D','',msg)
            if c:
                c = int(c)
                #判断页数是否过大
                if c > 200:
                    return f'无法刷新{c}页，页数太大了'
            else:
                c=3
            refresh(c)
            return f"刷新{c}页数据，刷新完毕后无提示，直接查询即可"
        #查看是否有价格区间限制
        elif msg.startswith('高于'):
            min_price = float(re.sub('\D','',msg))
        elif msg.startswith('低于'):
            max_price = float(re.sub('\D','',msg))
        #查看是否有输出个数限制
        elif msg.startswith('个数'):
            count = float(re.sub('\D','',msg))
        #查看解析类型
        elif msg == '默认':
            pass
        elif msg == '倒序':
            method = 'default_reversal'
        elif msg == '最低价格':
            method = 'low_price'
        elif msg == '最高价格':
            method = 'high_price'
        elif msg == '最多好评':
            method = 'high_comments_count'
        elif msg == '最低好评':
            method = 'low_comments_count'
        elif msg == '最多评论':
            method = 'high_favorable_rate'
        elif msg == '最少评论':
            method = 'low_favorable_rate'
        elif msg == '最高折扣':
            method = 'high_discount'
        elif msg == '最低折扣':
            method = 'low_discount'
        else:
            method = msg.replace('^空格', ' ')
    db = DB()
    infolist = db.check_from_db(table_name,method,count,max_price,min_price)
    if returnmod == 'g':
        returnlist = []
        for info in infolist:
            infomsg = {
                "type": "node",
                "data": {
                    "name": "Well404",
                    "uin": "1070330078",
                    "content": info
                }
            }
            returnlist.append(infomsg)
        return returnlist
    elif returnmod == 'p':
        return '\n————————————————\n'.join(infolist)
#刷新数据库   
def refresh(maxrange=3):
    """刷新数据库内的数据

    Args:
        maxrange (int, optional): 最大获取页数. Defaults to 3.
    """
    def getinfo(maxrange):
        db_nt = DB()
        db_nt.clear_db(date.today().strftime("%b%d%Y")) 
        for i in range(1,maxrange+1):
            if debugmod:
                print(f'正在爬取第{i}页')
            Turn_link = f"https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win&page={i}"
            run(Turn_link,db_nt)
    tread = Thread(target=getinfo,args=(maxrange,))
    tread.start()
#检查数据库是否存在
def is_existed():
    table_name = date.today().strftime("%b%d%Y")
    db = DB()
    return db.check_db(table_name)

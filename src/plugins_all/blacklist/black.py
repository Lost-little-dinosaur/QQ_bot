import sqlite3,time

debugmod = False

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("database/blacklist.db")
        self.cur = self.conn.cursor()
    #解析群组或用户身份ID
    def session_id_analysis(self,session_id):
        if "group" in session_id:
            _,groupid,userid = session_id.split('_')
            session_id_analyzed = {"groupid":f"group{groupid}", "userid":userid}
        else:
            session_id_analyzed = {"groupid":"user", "userid":session_id}
        if debugmod:
            print(f'——————session_id_analysis:——————\
                    \n{str(session_id_analyzed)}\
                    \n————————————————————————————————')        
        return session_id_analyzed
    #解析命令部分,并调用对应的模块进行执行
    def analysis(self,get_message,session_id):
        session_id_analyzed = self.session_id_analysis(session_id)
        #判断是否是私人聊天
        if session_id_analyzed["groupid"] == "user":
            return '你是认真的吗？这可是私人聊天啊'
        else:
            #若不是则开始执行
            get_message = get_message.strip()
            #判断是否为show指令
            if "show" in get_message:
                if debugmod:
                    print('show active')
                return f'现在处于黑名单的qq号为：\n{self.check("all",session_id_analyzed)}'
            else:
                #切片
                userid = 'non'
                funcs = []
                retime=9999999999999.00
                for msg in get_message.split(' '):
                    if debugmod:
                        print(f'——————blacklist_msg:——————\
                                \nmsg:{msg}\
                                \n————————————————————————————————') 
                    #查找对应的字段，并分析               
                    if "qq=" in msg:
                        if debugmod:
                            print('qq active')
                        _,userid = msg.split('=')
                        if not 'all' in userid:
                            userid = int(userid.rstrip(']'))
                    elif "func=" in msg:
                        if debugmod:
                            print('func active')
                        _,func_raw = msg.split('=')
                        for func in func_raw.split('&amp;'):
                            funcs.append(func)
                    elif "retime=" in msg:
                        if debugmod:
                            print('retime active')
                        _,retime_raw = msg.split('=')
                        retime = float(f'{(float(retime_raw)*3600 + time.time()):.2f}')
                    elif "check" in msg:
                        if debugmod:
                            print('check active')
                        returnmsg = self.check(userid,session_id_analyzed)
                        if not returnmsg['userid'] == 'non':
                            return f"QQ号:{returnmsg['userid']}\
                                    \n禁用的功能:{returnmsg['disabledfunc']}\
                                    \n添加者QQ号:{returnmsg['adderid']}\
                                    \n剩余封禁时长:{((float(returnmsg['releasetime'])-time.time())/3600):.2f}h"
                        else:
                            return '此QQ号并未在黑名单中'
                    elif "remove" in msg:
                        if debugmod:
                            print('remove active')
                        return self.remove(userid,session_id_analyzed)
                if debugmod:
                    print(f'——————blacklist_analysis:——————\
                            \nuserid:{userid}\
                            \nsession_id_analyzed:{session_id_analyzed}\
                            \nfuncs:{funcs}\
                            \nretime:{retime}\
                            \n————————————————————————————————')    
                    print('add active')         
                return self.add(userid,session_id_analyzed,funcs,retime)        
    #创建新表
    def creat_table(self,session_id_analyzed):
        self.cur.execute(
            f'''CREATE TABLE "{session_id_analyzed["groupid"]}"
            ("id"	INTEGER NOT NULL UNIQUE,
	        "userid"	INTEGER NOT NULL,
	        "disabledfunc"	BLOB NOT NULL,
	        "adderid"	INTEGER NOT NULL,
	        "releasetime"	BLOB NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT))'''
            )
        self.conn.commit()
    #查询对应信息
    def check(self,userid,session_id_analyzed):
        returnmsg = {"userid"	   :"non",
                     "disabledfunc":"non",
                     "adderid"	   :"non",
                     "releasetime" :"non",
                     "db":"non"}
        try:
            dbname = session_id_analyzed["groupid"]
            allinfo = self.cur.execute(f'SELECT userid, disabledfunc, adderid, releasetime, releasetime \
                                       from "{dbname}"')
            #判断是否为show指令
            if str(userid) == 'all':
                keylist = []
                for row in allinfo:
                    keylist.append(row[0])
                return keylist
            for row in allinfo:
                if debugmod:
                    print(str(row[0]))
                if str(row[0]) == str(userid):
                    returnmsg = {"userid"	  :row[0],
                                "disabledfunc":row[1],
                                "adderid"	  :row[2],
                                "releasetime" :row[3],
                                'db':dbname}            
        except sqlite3.OperationalError:
            self.creat_table(session_id_analyzed)
            returnmsg = {"userid"	  :"non",
                        "disabledfunc":"non",
                        "adderid"	  :"non",
                        "releasetime" :"non",
                        "db":"just_builded"}
        if debugmod:
            print(f'——————returnmsg:——————\
                    \n{str(returnmsg)}\
                    \n———————————————————————')     
        return returnmsg
    #添加新id
    def add(self,userid,session_id_analyzed,func,retime):
        if userid == 'non':
            return 'QQ号格式不正确，添加失败'    
        try:
            returnmsg = self.check(userid,session_id_analyzed)
            if func == []:
                func = '全部'
            if returnmsg['userid'] == 'non':
                self.cur.execute(f'''INSERT INTO {session_id_analyzed["groupid"]} (userid, disabledfunc, adderid, releasetime)
                    VALUES ("{userid}", "{func}", "{session_id_analyzed["userid"]}", "{retime}")''')
                self.conn.commit()
                return f'''已成功禁用{userid}的{func}功能，时长为{((float(retime)-time.time())/3600):.2f}h'''
            else:
                self.cur.execute(f'''UPDATE "{session_id_analyzed["groupid"]}" 
                                    SET disabledfunc = "{func}", releasetime = "{retime}", adderid = {session_id_analyzed["userid"]} 
                                    WHERE userid = "{returnmsg['userid']}"''')                       
                self.conn.commit()  
                return f'''已成功更新禁用{userid}的{func}功能,时长为{((float(retime)-time.time())/3600):.2f}h'''  
        #若数据库连接失败则新建一个 
        except sqlite3.OperationalError:
            self.creat_table(session_id_analyzed)
            return f'已新建本群的数据表，请重新输入一次指令'
    #移除id
    def remove(self,userid,session_id_analyzed):
        try:
            if userid == 'all':
                self.cur.execute(f'''DELETE FROM "{session_id_analyzed["groupid"]}"''')
                self.conn.commit()
                return '已成功清空黑名单'
            else:                
                returnmsg = self.check(userid,session_id_analyzed)
                if not returnmsg['userid'] == 'non':
                    self.cur.execute(f'''DELETE FROM "{session_id_analyzed["groupid"]}"  
                                    WHERE userid = "{returnmsg['userid']}"''')
                    self.conn.commit()  
                    return f'''已成功将{returnmsg['userid']}移除黑名单'''      
                else:
                    return '此QQ号并未在黑名单中'
        except sqlite3.OperationalError:
            self.creat_table(session_id_analyzed)
            return '此QQ号并未在黑名单中'
db = DB()
#判断是否通过
def check(kw,session_id):
    session_id_analyzed = db.session_id_analysis(session_id)
    if session_id_analyzed["groupid"] == 'user':
        return True
    else:
        userid = session_id_analyzed["userid"]
        returnmsg = db.check(userid,session_id_analyzed)
        if returnmsg['disabledfunc'] == 'non':
            return True
        elif returnmsg['disabledfunc'] == '全部':
            return False
        elif float(returnmsg['releasetime']) < time.time():
            db.remove(userid,session_id_analyzed)
            return True
        elif check_kw(kw,returnmsg['disabledfunc']):
            return False
        else:
            return True

def check_kw(kw,kws):
    for dkw in eval(kws):
        if dkw in kw:
            return True
    return False
    
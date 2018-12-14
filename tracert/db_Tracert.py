#!/usr/bin/python3
 
import pymysql
import time

# 获取外网IP
def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    ### print('hhh2008 ip:' + ip)
    return ip


def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt,"html.parser").iframe
    return soup["src"]

def checkFile(x):
    filename=x+'.txt'
    result=True
    f = open(filename) # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        if ('请求超时。' in line)&(' 30 ' in line):
            result=False
    f.close() # close the file
    return result

def insertDB(x,checkFile_y):
    # 打开数据库连接
    db = pymysql.connect("172.26.79.249","tracert1","tracert1","tracert" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
 
    # 使用 execute()  方法执行 SQL 查询 
    # cursor.execute("SELECT VERSION()")
 
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
 
    # print ("Database version : %s " % data)

    hhh = ''
    f = open(x+'.txt')
    hhh = f .read()
    f.close()

    ### print (socket.gethostbyname(socket.gethostname()))
    ### print (get_out_ip(get_real_url()))
    ###   127.0.0.1

    ### 可能是你的帐号不允许从远程登陆，只能在localhost。
    ### 这个时候只要在localhost的那台电脑，登入MySQL后，更改
    ### "mysql" 数据库里的 "user" 表里的 "host" 项，从"localhost"改称"%"
    
    #time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    # SQL 插入语句
    sql = """INSERT INTO LOGS_TRACERT(IP_ADRESS_IN,IP_ADRESS_OUT,
             STATUS, CONTENT, DATE_TIME,DB_NAME)
             VALUES ("""
    sql = sql + "'" + socket.gethostbyname(socket.gethostname()) +"',"
    sql = sql + "'" + get_out_ip(get_real_url()) +"',"    
    sql = sql + checkFile_y +","
    sql = sql + "'"+ x+"数据库连接具体情况- "+ hhh +"',"
    sql = sql + "'"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"',"
    sql = sql + "'"+ x +"')"
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # cursor.execute(sql)
     
    # 关闭数据库连接
    db.close()
    return

tup = ('IOP', 'Emerald','AIAA' ,'SPIE','SIAM','ASME')
for x in tup:
    # print (x)
    checkFile_x = checkFile(x)
    if checkFile_x:
        print (x+ '连接正常.')
        checkFile_y="1"
    else:
        print (x+ '不能正常连接.')
        checkFile_y="0"
    insertDB(x,checkFile_y)

###   Version:2018.12.14 14:43   ###
    

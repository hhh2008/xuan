#!/usr/bin/python3
 
import pymysql
import time

# 打开数据库连接
db = pymysql.connect("localhost","tracert1","tracert1","tracert" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)

hhh = 'Hello world!'
#time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
# SQL 插入语句
sql = """INSERT INTO LOGS_TRACERT(IP_ADRESS,
         STATUS, CONTENT, DATE_TIME,DB_NAME)
         VALUES ("""
sql = sql + "'172..26..79..249',"
sql = sql + "'F',"
sql = sql + "'"+ hhh +"',"
sql = sql + "'"+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"',"
sql = sql + "'zzz2008')"
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

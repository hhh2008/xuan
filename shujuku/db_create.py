#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","","tracert" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)

sql = """CREATE TABLE LOGS_TRACERT (
         IP_ADRESS  CHAR(20) NOT NULL,
         STATUS CHAR(1),
         CONTENT TEXT,
         DATE_TIME DATE)"""

# SQL 插入语句
sql_b = """INSERT INTO EMPLOYEE1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 22, 'M', 3000)"""
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

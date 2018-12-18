#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "tracert", charset='utf8' )

### select `处理网址`,处理名称 from db_address_wai GROUP BY `处理网址`

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
### sql = "SELECT * FROM LOGS_TRACERT WHERE DB_NAME = '%s'" % ('ASME')

sql = "select `处理网址`,处理名称 from db_address_wai GROUP BY `处理网址`"
### f = open("file1", "r")  # 打开文件
fnew = open("c:\\tracert\\Tracert_All_GBK.bat", "w", encoding="GBK")


try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
#      IP_ADRESS = row[0]
#      STATUS = row[1]
#      CONTENT = row[2]
#      DATE_TIME = row[3]
#      DB_NAME = row[4]
      IP_ADRESS =row[0].strip()
      DB_NAME = row[1].replace(' ','')
      # 打印结果
#      print ("IP_ADRESS=%s,STATUS=%d,CONTENT=%s,DATE_TIME=%s,DB_NAME=%s"%(IP_ADRESS, STATUS, CONTENT, DATE_TIME, DB_NAME ))
      print ("IP_ADRESS=%s,DB_NAME=%s"%(IP_ADRESS, DB_NAME))
      fnew.write('tracert '+IP_ADRESS+' >c:\\tracert\\'+ DB_NAME +'.txt')
      fnew.write('\n')
except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()
fnew.close()  #关闭文件


### Version 2018-12-18 16:15



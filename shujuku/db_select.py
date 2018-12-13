#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "tracert1", "tracert1", "tracert", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM LOGS_TRACERT \
       WHERE DB_NAME = '%s'" % ('ASME')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      IP_ADRESS = row[0]
      STATUS = row[1]
      CONTENT = row[2]
      DATE_TIME = row[3]
      DB_NAME = row[4]
      # 打印结果
      print ("IP_ADRESS=%s,STATUS=%d,CONTENT=%s,DATE_TIME=%s,DB_NAME=%s"%(IP_ADRESS, STATUS, CONTENT, DATE_TIME, DB_NAME ))
except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()

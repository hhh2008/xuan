#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "tracert", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE db_address_wai SET 处理网址 = trim(trailing '/' from  (trim(leading 'http://' from 网址))) WHERE 网址 like " +'"' + 'http://%'+'"'

### '''sql = "UPDATE db_address_wai SET 处理网址 = trim(trailing '/' from  (trim(leading 'http://' from 网址))) WHERE 数据库名称 = 'SCI / CPCI-S'"'''

### trim(leading 'http://' from
### trim(leading 'https://' from
### trim(trailing '/' from
### WHERE 数据库名称 = 'SCI / CPCI-S'

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print('ok!')
except:
   # 发生错误时回滚
   db.rollback()
   print('no!')

# 关闭数据库连接
db.close()

### Version Time 2018-12-17 17:06

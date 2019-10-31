#!/usr/bin/env python3
#coding:utf8
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'pi',
    password = 'raspberry',
    database = 'boso',
    )
cur = conn.cursor()
try:
 cur.execute('select * from sensor')
 rows = cur.fetchall()
 for row in rows:
     print(row)
 conn.commit()
except:
  print("hell")

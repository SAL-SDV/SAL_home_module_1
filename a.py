#!/usr/bin/env python
#-*- coding:utf-8 -*-

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='pi',
    passwd='raspberry',
    db='boso')
cursor = connection.cursor()
cursor.execute("select * from sensor_config")
rows = cursor.fetchall()
for row in rows:
 print(row)
connection.commit()
connection.close()

connection2 = mysql.connector.connect(
    host='192.168.13.30',
    user='pi',
    passwd='raspberry',
    db='Gdb')

cursor2 = connection2.cursor()
cursor2.execute("select * from home_list")
rows2 = cursor2.fetchall()
for row2 in rows2:
 print(row2)
connection2.commit()

connection2.close()

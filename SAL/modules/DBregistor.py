#!/usr/bin/env python
#-*- coding:utf-8 -*-

import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    user='pi',
    passwd='raspberry',
    db='boso')

con2 = mysql.connector.connect(
    host='192.168.13.30',
    user='pi',
    passwd='raspberry',
    db='Gdb')

cur = con.cursor()
cur2 = con2.cursor()

try:
    table = '1_sensor'
    cur2.execute("DROP TABLE IF EXISTS %s;" % table)
    cur2.execute(
    """
    CREATE TABLE %s(
    id int(10) auto_increment not null primary key,
    date varchar(20) ,
    time varchar(20) ,
    place varchar(8)
    )
    """ % table)
    
    cur.execute("select * from sensor")
    rows = cur.fetchall()
    for row in rows:
        cur2.execute("INSERT INTO 1_sensor VALUES({0[0]},'{0[1]}','{0[2]}','{0[3]}');".format(row))

    cur2.execute("select * from 1_sensor")
    rows2 = cur2.fetchall()
    for row2 in rows2:
     print(row2)

    con.commit()
    con2.commit()

except mysql.connector.Error as err:
    print("Failed crete: {}".format(err))

finally:
    con.close()
    con2.close()

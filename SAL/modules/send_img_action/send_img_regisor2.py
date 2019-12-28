#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import os
import datetime



    #接続先を指定
con = mysql.connector.connect(
        host='localhost',
        user='user',
        passwd='user',
        db='sal')

cur = con.cursor()
    
path='/home/pi/SAL_Web-master/media/images/111001_2019:12:26:20:24:16.jpg/'

#pathは'/home/pi/SAL_Web-master/images/0000:00:00:00:00:00.jpg'のような形で入っているのでスライスで切り出す。
#datetimestr = '2019:12:26:20:24:16'

datetimestr = (''+path[-24:-5])
    
datetime = datetime.datetime.strptime(datetimestr, '%Y:%m:%d:%H:%M:%S')
    
id =1
cameraID=1

send_path = ( ''+path[-31:])

info = [id,datetime,send_path,cameraID]

try:
        table = 'imagelist'
        '''
        cur.execute("DROP TABLE IF EXISTS %s;" % table)
        cur.execute(
        """
        CREATE TABLE %s(
        id int(10) auto_increment not null primary key,
        date date,
        time time ,
        path varchar(50)
        )
        """ % table)
        '''
        cur.execute("INSERT INTO imagelist VALUES('{0[0]}','{0[1]}','{0[2]}',{0[3]});".format(info))

        cur.execute("select * from imagelist")
        rows = cur.fetchall()
        for row in rows:
         print(row)

        con.commit()

except mysql.connector.Error as err:
        print("Failed crete: {}".format(err))

finally:
        con.close()

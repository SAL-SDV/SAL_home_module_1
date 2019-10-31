#!/usr/bin/env python
#coding:utf8
'''
L and D monitor. need.
for conn. parallel process.
'''
from time import sleep
from urllib.parse import urlparse
import mysql.connector
import datetime
import time
import serial
import subprocess
import sys

args = ['service','mysqld','status']
while subprocess.Popen('service mysqld status', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').find('Active: active') == -1:
    sleep(1)


def dbconnect():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'pi',
            password = 'raspberry',
            database = 'boso',
        )
    except Exception as e:
        sys.exit(e)
    return conn

conn = dbconnect()

try:
    cur = conn.cursor()
    cur.execute('select * from sensor_config')
    sensor_list = cur.fetchall()
    sensor_list = [sensor_list[i][0] for i in range(len(sensor_list))]
except:
    pass

while(True):
    ser = serial.Serial('/dev/ttyUSB0',115200)
    test = str(ser.readline())
    slicer = test[13:21]
    cur = conn.cursor()

    checkflag = [flag for flag in range(len(sensor_list)) if str(sensor_list[flag]) == slicer]

    try:
        date = datetime.datetime.today()
        today = date.strftime('%Y-%m-%d')
        now = date.strftime('%H:%M:%S')
        cur.execute('insert into sensor (date,time,place) values (%s,%s,%s)',(str(today),str(now),str(slicer)))
        conn.commit()
    except IndexError:
        while True:
            place = input('>>>')
            if 0 < len(place) < 21: break
        cur.execute('insert into sensor_config (sensorID,door_name) values (%s,%s)',(str(slicer),str(place)))
        conn.commit()
        cur.execute('select * from sensor_config')
        sensor_list = cur.fetchall()
        sensor_list = [sensor_list[i][0] for i in range(len(sensor_list))]
    ser.close()
    sleep(4)

from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
import pymysql.cursors


def getConnection():
    return pymysql.connect(host='localhost',
                           user='user',
                           password='user',
                           db='sal',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor
                           )


def setting(request):
    table = []
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM sal.sensorlist "
        cursor.execute(sql)
        for row in cursor.fetchall():
            table.append(row)
        connection.close()

    for t in table:
        if request.GET.get(t["ID"] + '_update') == None or request.GET.get(t["ID"] + '_update') == '':
            print(t["ID"] + 'はnullですよ')
        else:
            print(t["ID"] + 'のNameを' +
                  request.GET.get(t["ID"] + '_update') + 'に変更しました。')
            sql = "UPDATE sal.SensorList SET Name = '" + \
                request.GET.get(t["ID"] + '_update') + \
                "' WHERE ID = '" + t["ID"] + "'; "

            connection = getConnection()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
                print(sql)
                # 更新
                sql = "SELECT * FROM sal.sensorlist "
                cursor.execute(sql)
                print(sql)
                table = []
                for row in cursor.fetchall():
                    table.append(row)
                connection.close()

    d = {
        'table': table,
    }
    return render(request, 'setting.html', d)


def home(request):
    # sqlに接続
    connection = getConnection()
    # select文 よりスマートな方法があるはず
    with connection.cursor() as cursor:
        sql = "SELECT path FROM sal.imagelist WHERE id = (SELECT MAX(id) FROM sal.imagelist)"
        cursor.execute(sql)
        result = cursor.fetchone()
        path = result["path"]

        sql = "SELECT imagedata FROM sal.imagelist WHERE id = (SELECT MAX(id) FROM sal.imagelist)"
        cursor.execute(sql)
        result = cursor.fetchone()
        imagedata = result["imagedata"]
    # sqlから切断
    connection.close()
    d = {
        'path': path,
        'imagedata': imagedata,
    }

    return render(request, 'home.html', d)


def logs(request):
    connection = getConnection()
    imagelogs = []
    sensorlogs = []
    with connection.cursor() as cursor:
        sql = "SELECT * FROM sal.imagelist "
        cursor.execute(sql)
        for row in cursor.fetchall():
            imagelogs.append(row)

        sql = "SELECT * FROM sal.sensorlog "
        cursor.execute(sql)
        for row in cursor.fetchall():
            sensorlogs.append(row)
        connection.close()
        # 調整中
        # sensorIndex = 0
        # imageIndex = 0
        # complogs = []
        # # {'Date': None, 'ID': None,
        # #             'SensorID': None, 'path': None}
        # while sensorIndex < len(sensorlogs) or imageIndex < len(imagelogs):
        #     if sensorIndex == len(sensorlogs):
        #         # complogs = imagelogs[imageIndex]
        #         imageIndex + 1
        #     elif imageIndex == len(imagelogs):
        #         # complogs = sensorlogs[sensorIndex]
        #         sensorIndex + 1
        #     else:
        #         if sensorlogs[sensorIndex]["Date"] < imagelogs[imageIndex]["Date"]:
        #             # complogs = sensorlogs[sensorIndex]
        #             sensorIndex + 1
        #         else:
        #             # complogs = imagelogs[imageIndex]
        #             imageIndex + 1
        # print(complogs)
    d = {
        # 'complogs': complogs,
        'imagelogs': imagelogs,
        'sensorlogs': sensorlogs
    }
    print(imagelogs[1])
    return render(request, 'logs.html', d)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
#↓更新にあわせて実行するモジュール(ここでは仮にsend_img_action.py)
from send_img_action import send_img_send as send
from send_img_action import send_img_registor as registor

# 監視対象のファイル
observed_file_type = ('.jpg')

# 設定
#BASEDIR = os.path.abspath(os.path.dirname(__file__))
#→このプログラムファイルが置かれている場所を監視する場合はこれ

#ラズパイの共有フォルダを指定
#共有フォルダ[share]内に、[DATA]フォルダを配置した
BASEDIR ='/home/pi/SAL/viewer/public/images'

# 変更したファイルが監視対象であるかを調べる
def match(path):
    return any([path.endswith(ft) for ft in observed_file_type])

# 変更時のイベントハンドラ
class ChangeHandler(FileSystemEventHandler):
    def on_create(self, event):
        if event.is_directory:
            return
        if match(event.src_path):
            print('Create',event.src_path)
            send.send(event.src_path) #ファイル作成時に実行
            registor.registor(event.src_path) #ファイル作成時に実行

    def on_modified(self, event):
        if event.is_directory:
            return
        if match(event.src_path):
            print('Modified',event.src_path)
            send.send(event.src_path)  #ファイル変更時に実行
            registor.registor(event.src_path) #ファイル作成時に実行

    def on_deleted(self, event):
        if event.is_directory:
            return
        if match(event.src_path):
            print('delete',event.src_path)
            #ファイルが消された時はなにもしない


if __name__ in '__main__':
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, BASEDIR, recursive=True)
    print('start dir=',BASEDIR)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

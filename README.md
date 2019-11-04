# SAL_home_module

SALで用いるホームモジュール用のレポジトリです。
```
・SAL/は前年使用していたnodejsベース-センサー情報、写真の表示が可能です。
・SAL_Web/は新しく作成したDjangoベース-現在写真の表示のみ可能です。
・a.jpg,a.py,db_test.pyはとりあえず無視しておいてください
```

ラズパイ０からデータを受け取った時に市役所サーバに転送する処理はSAL/modules/send_img.pyで行います。

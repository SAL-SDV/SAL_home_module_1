# module
***
このディレクトリではセンサ、カメラから受け取った情報に対する捜査を行うプログラムが格納されています。
```
・send_img.py  /viewer/public/imgフォルダの中身に変更（追加、変更、削除）が加えられたときに、変更に応じてsend_img_action.py,send_img_registorを実行します。
・send_img_action.py   変更されたファイルを市役所サーバ（現在はテスト用の自前ラズパイ）に送信するプログラムです。send_img.pyからimportされます。
・send_img_registor.py(仮実装)   変更されたファイルの情報を市役所サーバ（現在はテスト用の自前ラズパイ）のDBに登録するプログラムです。send_img.pyからimportされます。一部おかしい挙動はありますが動きます。
・DBregistor.py
・DBuploader.py
・B.py
・db_test_py
・test_c.sh
```

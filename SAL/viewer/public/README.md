# ラズパイ０被操作対象ディレクトリ
***
このディレクトリ配下にあるmovie,imagesディレクトリはラズパイ０が撮影したデータの転送先ディレクトリになっており、０が動いている間勝手にファイルが増えていきます。
```
・send_img.py  imgフォルダの中身に変更（追加、変更、削除）が加えられたときに、変更に応じてsend_img_action.py,send_img_registorを実行します。
・send_img_action.py   変更されたファイルを市役所サーバ（現在はテスト用の自前ラズパイ）に送信するプログラムです。send_img.pyからimportされます。
・send_img_registor.py(未実装)   変更されたファイルの情報を市役所サーバ（現在はテスト用の自前ラズパイ）のDBに登録するプログラムです。send_img.pyからimportされます。
・wd.2.py  昨年の先輩が作ったプログラムです。おそらく受信した画像をメールで送信する感じのやつです。怖いのでまだ試していません。
```
## weather-forecast-linebot
Weater-Forecast-LinebotはLINEBotを利用した天気予報返信アプリケーションです。

## 環境構築～プロジェクト作成（備忘）

１．Django用の仮想環境を構築
PRJフォルダに移動し以下のコマンドを実行
‵‵‵bash
py -m venv PRJ名
‵‵‵

２．Djangoのインストール
PRJフォルダで以下のコマンドを実行（最新版インストール）
‵‵‵bash
py -m pip install Django
‵‵‵
上記コマンドでエラーが出た場合、バージョン指定でインストール
‵‵‵bash
pip install -U django==2.2.1
‵‵‵
以下のコマンドでインストールされたか確認できる
‵‵‵bash
django-admin --version
‵‵‵

３．Djangoのプロジェクトを構成する
コードを置きたいディレクトリで以下のコマンドを実行
‵‵‵bash
django-admin startproject weatherForcast
‵‵‵
４．Djangoアプリを作成
３で作成したディレクトリで以下のコマンドを実行
‵‵‵bash
python manage.py startapp bot
‵‵‵

mysiteディレクトリが作成されたのを確認し、動作確認する
‵‵‵bash
python manage.py runserver
‵‵‵

５．herokuへデプロイ
herokuのアプリページのSettingsタブからpythonのbuildpackを追加する

以下のコマンドを実行しGitからPushする
‵‵‵bash
git push heroku master:main
‵‵‵


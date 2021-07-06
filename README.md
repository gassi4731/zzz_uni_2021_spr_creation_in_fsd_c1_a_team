# 2021年度 先端社会デザイン創成１ 雛形
## 前提条件
Python3が導入済
## 実行手順
1.Pythonの仮想環境（virtualenv）を作成する.
```
$ python3 -m venv venv
```
2.作成した仮想環境を有効にする．  
**for Windows**
```
$ .\venv\Scripts\activate.bat
```
**for Mac**
```
$ source ./venv/bin/activate
```
3.仮想環境にWebサーバを動かすために必要なライブラリをロードする．
```
(venv) $ python -m pip install -r requirements.txt
```
4.uvicornというコマンドがインストールされる．このコマンドを使ってWebサーバを起動する．
```
(venv) $ uvicorn main:app --reload
```

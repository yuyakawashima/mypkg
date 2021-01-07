# ロボットシステム学課題2　～おみくじ～
## 概要
ロボットシステム学の講義で作成したROSを改造し，おみくじを作成した．
## 動作環境
・Raspberry Pi 4 (4GB)  
・Ubuntu server 20.04 LTS  
・ROS version noetic  
## 使用道具
・Raspberry Pi 4 (4GB)
## インストール方法
```sh
$ cd ~/catkin_ws/src/
$ git clone https://github.com/yuyakawashima/mypkg.git
$ cd ..
$ catkin_make
$ source ~/.bashrc
```
bashrcに  
**source /opt/ros/noetic/setup.bash**  
が書かれていない場合，以下を実行  
```sh
$ source /opt/ros/noetic/setup.bash
``` 
## 実行方法
```sh
$ roslaunch mypkg mypkg.launch
```
#### 中断したい場合
動作中に「Ctrl + c」を入力する．  

## 実行動画

https://www.youtube.com/watch?v=Fh0UaaSiFsY
## 動画中の赤文字について

<img width="713" alt="2021-01-07 (6)" src="https://user-images.githubusercontent.com/72898960/103891702-aa736700-512d-11eb-83a5-eeff9bb426b1.png">  

内容は以下の通りである．  
```
必要なプロセス[count-2]が終了しました!  
プロセスはきれいに終わりました．  
ログファイル:  
シャットダウンを開始します!
```
ROSを強制的に終了させるために発生し，動きに支障が出るわけではない．  
#### 表示しない方法
実行中に「Ctrl + c」を入力する．  
## ライセンス
BSD 3-Clause License

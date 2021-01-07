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
端末1$ roscore
端末2$ rosrun mypkg twice.py
端末3$ rosrun mypkg count.py
```
####  終了時
端末1に「Ctrl + c」を入力する．   
## 実行動画
https://www.youtube.com/watch?v=vZpmDJJ3Qio
## ライセンス
BSD 3-Clause License

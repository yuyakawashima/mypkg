# ロボットシステム学課題2　～おみくじ～
## 目的
ROSについて学習し，ファイル間で通信する．
## 動作環境等
・Raspberry Pi 4
・Ubuntu server 20.04 LTS
・ROS version noetic
## 動作方法
#### 1 インストールする
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/yuyakawashima/mypkg.git
$ cd mypkg/scripts
$ chmod +x count.py
$ chmod +x twice.py
$ cd ..
$ catkin_make
$ source ~/.bashrc
```
#### 2 実行する
```
端末1$ roscore
端末2$ rosrun mypkg twice.py
端末3$ rosrun mypkg count.py
```
#### 3 終了時
端末1に「Ctrl + c」を入力する．

## 内容
①　1～7の内ランダムな整数を100個生成する．
②　PubからSubに通信している間，渡された値に応じて顔文字を出力．
③　渡された値の内，最も多かったものを選び，運勢を出力する．

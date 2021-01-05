#!/usr/bin/env python3

"""
BSD 3-Clause License

Copyright (c) 2020, Yuya Kawashima and Ryuichi Ueda
All rights reserved.
""" 
import rospy
from std_msgs.msg import Int32

c_1 = 0
c_2 = 0
c_3 = 0
c_4 = 0
c_5 = 0
c_6 = 0
c_7 = 0
c_max = 0
n = 0
word = 0

def cb(message):
    global n
    n = message.data

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(15)
while not rospy.is_shutdown():
    if n == 1:
        word = "▂▅▇█▓▒(’ω’)▒▓█▇▅▂"
        pub.publish(n)
        n = 0
        c_1 += 1
        print("\033[33m" + word + "\033[0m")
    elif n == 2:
        word = "─=≡Σ((( つ•̀ω•́)つ"
        pub.publish(n)
        n = 0
        c_2 += 1
        print("\033[36m" + word + "\033[0m")
    elif n == 3:
        word = "(っ’ヮ’c)"
        pub.publish(n)
        n = 0
        c_3 += 1
        print("\033[32m" + word + "\033[0m")
    elif n == 4:
        word = "＼(^ω^)／"
        pub.publish(n)
        n = 0
        c_4 += 1
        print("\033[37m" + word + "\033[0m")
    elif n == 5:
        word = "(#╹◡╹)"
        pub.publish(n)
        n = 0
        c_5 += 1
        print("\033[35m" + word + "\033[0m")
    elif n == 6:
        word = "(ﾉД`)"
        pub.publish(n)
        n = 0
        c_6 += 1
        print("\033[31m" + word + "\033[0m")
    elif n == 7:
        word = "ﾟ(ﾟ´Д｀ﾟ)ﾟ。"    
        pub.publish(n)
        n = 0
        c_7 += 1
        print("\033[34m" + word + "\033[0m")
    elif n == 100:
        break
    rate.sleep()

c_max = max(c_1, c_2, c_3, c_4, c_5, c_6, c_7)
if c_max == c_1:
    print("運勢は"+"\033[33m大吉\033[0m"+"です")
elif c_max == c_2:
    print("運勢は"+"\033[36m吉\033[0m"+"です")
elif c_max == c_3:
    print("運勢は"+"\033[32m中吉\033[0m"+"です")
elif c_max == c_4:
    print("運勢は"+"\033[37m小吉\033[0m"+"です")
elif c_max == c_5:
    print("運勢は"+"\033[35m末吉\033[0m"+"です")
elif c_max == c_6:
    print("運勢は"+"\033[31m凶\033[0m"+"です")
elif c_max == c_7:
    print("運勢は"+"\033[34m大凶\033[0m"+"です")

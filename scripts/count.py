#!/usr/bin/env python3

"""
BSD 3-Clause License

Copyright (c) 2020, Yuya Kawashima and Ryuichi Ueda
All rights reserved.
"""
import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(15)
n = random.randint(1,7)
s = 0
num = 0
num_max = 100
pub.publish(n)

while True:
    num_max = input('50以上の数字を入力:')

    try:
        int(num_max)
    except ValueError:
        print("\033[31m数字入を入れてくれ\033[0m")
        continue

    if int(num_max) < 50:
        print("\033[31m50以上の数字を入れてくれ\033[0m")
    else:
        break

while not rospy.is_shutdown():
    n = random.randint(1,7)
    s += n
    num = num + 1
    print(num,"回目:",n)
    if int(num_max) == int(num):      
        pub.publish(n)
        n = 100
        num = 0
        rospy.sleep(2)
        pub.publish(n)
        break
    pub.publish(n)
    rate.sleep()

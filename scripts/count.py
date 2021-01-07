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
num = 0
num_max = 100
pub.publish(n)

while True:
    num_max = input('50以上の数字を入力:')

    try:
        int(num_max)
    except ValueError:
        print("\033[31m数字を入れてくれ\033[0m")
        continue

    if int(num_max) < 50:
        print("\033[31m50以上の数字を入れてくれ\033[0m")
    else:
        num_max = int(num_max) + 1
        break

while not rospy.is_shutdown():
    n = random.randint(1,7)
    if num > 0:
        print(num,"回目:",n)
    num += 1
    pub.publish(n)
    if int(num_max) == int(num):      
        n = 100
        rospy.sleep(2)
        pub.publish(n)
        break
    rate.sleep()

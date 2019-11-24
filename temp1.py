import random

import tensorflow as tf
# 输出不同类型变量
# name = "Ashley"
# print("My name is %s" % name)
# age = 18
# height = 156
# print("My age is %d" % age)
# print("My height is %f" % height)

# 多维数组及输出
# x1 = [1, 2, 3]
# x2 = [4, 5, 6]
# x3 = [x1, x2]
# print(x3)

# x1 = tf.placeholder(shape=[3, 2],dtype=tf.float32)
#
# x2 = x1 * 7
#
# y = tf.nn.softmax(x2)
#
# session = tf.Session()
#
# print(session.run(y, feed_dict={x1: [[1, 2], [3, 4], [5, 6]]}))

random.seed

x = random.random() * 40 - 20

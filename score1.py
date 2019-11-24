import tensorflow as tf

# 定义占位符
x1 = tf.placeholder(dtype=tf.float32)
x2 = tf.placeholder(dtype=tf.float32)
x3 = tf.placeholder(dtype=tf.float32)

# 定义训练结果
yTrain = tf.placeholder(dtype=tf.float32)

# 定义变量（0.1表示其初始值）
w1 = tf.Variable(0, dtype=tf.float32)
w2 = tf.Variable(0, dtype=tf.float32)
w3 = tf.Variable(0, dtype=tf.float32)

# 定义结果过程
n1 = x1 * w1
n2 = x2 * w2
n3 = x3 * w3

# 计算结果
y = n1 + n2 + n3

# 定义结果误差
loss = tf.abs(yTrain-y)

# 定义优化器(0.001表示学习率)
optimizer = tf.train.RMSPropOptimizer(0.001)

# train对象按照学习率最小化的原则来调整可变参数
train = optimizer.minimize(loss)

# 创建Tensorflow会话
sess = tf.Session()

#可变参数初始化
init = tf.global_variables_initializer()
sess.run(init)

# 得到结果并输出
# result = sess.run([x1, x2, x3, w1, w2, w3, y], feed_dict={x1: 90, x2: 80, x3: 70})
# print(result)

for i in range(1):
    result = sess.run([train, x1, x2, x3, w1, w2, w3, y, yTrain, loss], feed_dict={x1: 90, x2: 80, x3: 70, yTrain: 85})
    print(result)

    result = sess.run([train, x1, x2, x3, w1, w2, w3, y, yTrain, loss], feed_dict={x1: 98, x2: 95, x3: 87, yTrain: 96})
    print(result)
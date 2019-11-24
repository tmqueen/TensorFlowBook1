import tensorflow as tf

# 多加一个入参就需要变更模型，因此使用向量会更合适
x = tf.placeholder(shape=[3], dtype=tf.float32)
yTrain = tf.placeholder(shape=[], dtype=tf.float32)

w = tf.Variable(tf.zeros([3]), dtype=tf.float32)

wn = tf.nn.softmax(w)

# n = x * w
n = x * wn

y = tf.reduce_sum(n)


loss = tf.abs(yTrain - y)

# optimizer = tf.train.RMSPropOptimizer(0.001)
optimizer = tf.train.RMSPropOptimizer(0.1)

train = optimizer.minimize(loss)

session = tf.Session()

init = tf.global_variables_initializer()

session.run(init)

# for i in range(1):
#     result = session.run([train, x, w, y, yTrain, loss], feed_dict={x: [90, 80, 70], yTrain: 85})
#     print(result)
#
#     result = session.run([train, x, w, y, yTrain, loss], feed_dict={x: [98, 95, 87], yTrain: 96})
#     print(result)

for i in range(1):
    result = session.run([train, x, wn, y, yTrain, loss], feed_dict={x: [90, 80, 70], yTrain: 85})
    print(result)

    result = session.run([train, x, wn, y, yTrain, loss], feed_dict={x: [98, 95, 87], yTrain: 96})
    print(result)
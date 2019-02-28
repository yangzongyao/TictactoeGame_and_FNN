#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 00:24:14 2019

@author: yang
"""

import tensorflow as tf
import readDataForNN as r
import numpy as np

#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

train_X, train_y = r.dataOperator()

train_X = np.array(train_X)
train_y = np.array(train_y)
orignal_y = train_y

train_X = train_X.reshape(train_X.shape[0],3,3)
train_y = train_y.reshape(train_y.shape[0],3,3)

t = train_X != train_y
t = t.astype(float)
train_X = train_X.astype(float)
train_y = t


# data augmentation
rot90_X = []
rot90_y = []
for i in train_X:
    rot90_X.append(np.rot90(i))

for i in train_y:
    rot90_y.append(np.rot90(i))

rot90_X = np.array(rot90_X)
rot90_y = np.array(rot90_y)

rot180_X = []
rot180_y = []
for i in rot90_X:
    rot180_X.append(np.rot90(i))

for i in rot90_y:
    rot180_y.append(np.rot90(i))

rot180_X = np.array(rot180_X)
rot180_y = np.array(rot180_y)

rot270_X = []
rot270_y = []
for i in rot180_X:
    rot270_X.append(np.rot90(i))

for i in rot180_y:
    rot270_y.append(np.rot90(i))

rot270_X = np.array(rot270_X)
rot270_y = np.array(rot270_y)

#train_X = np.array([*train_X, *rot90_X, *rot180_X, *rot270_X])
#train_y = np.array([*train_y, *rot90_y, *rot180_y, *rot270_y])
train_X = np.concatenate([train_X, rot90_X, rot180_X, rot270_X])
train_y = np.concatenate([train_y, rot90_y, rot180_y, rot270_y])


#del rot90_X, rot90_y, rot180_X, rot180_y, rot270_X, rot270_y, t

# data augmentation end

train_X = train_X.reshape(train_X.shape[0], 9)
train_y = train_y.reshape(train_y.shape[0], 9)

x = tf.placeholder(tf.float32, [None,9])

W0 = tf.Variable(tf.truncated_normal([9,15], stddev=0.1))
b0 = tf.Variable(tf.zeros([15]))

hidden0 = tf.matmul(x,W0) + b0
y0 = tf.nn.relu(hidden0)

W1 = tf.Variable(tf.truncated_normal([15,9], stddev=0.1))
b1 = tf.Variable(tf.zeros([9]))
hidden1 = tf.matmul(y0,W1) + b1
y = tf.nn.softmax(hidden1)

y_ = tf.placeholder(tf.float32, [None,9])

cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=y_)
cross_entropy_v = tf.reduce_mean(cross_entropy)

predict_location = tf.argmax(y, 1)
location = predict_location[0] // 3 + 1, predict_location[0] % 3 + 1

train_step = tf.train.GradientDescentOptimizer(1e-2).minimize(cross_entropy)


correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())



for i in range(5000):
    batch_index = np.random.randint(0,train_X.shape[0],150)
    batch_X = []
    batch_y = []
    for i in batch_index:
        batch_X.append(train_X[i])
        batch_y.append(train_y[i])
        #batch_X, batch_y = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x : batch_X, y_:batch_y})
    #print(sess.run(cross_entropy_v, feed_dict={x: batch_X, y_: batch_y}))
    if i % 100 == 0:
        print(sess.run(accuracy, feed_dict={x : train_X, y_ : train_y}))









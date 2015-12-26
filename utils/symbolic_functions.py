#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: symbolic_functions.py
# Author: Yuxin Wu <ppwwyyxx@gmail.com>

import tensorflow as tf
import numpy as np
__all__ = ['one_hot', 'batch_flatten']

def one_hot(y, num_labels):
    batch_size = tf.size(y)
    y = tf.expand_dims(y, 1)
    indices = tf.expand_dims(tf.range(0, batch_size), 1)
    concated = tf.concat(1, [indices, y])
    onehot_labels = tf.sparse_to_dense(
        concated, tf.pack([batch_size, num_labels]), 1.0, 0.0)
    onehot_labels.set_shape([None, num_labels])
    return tf.cast(onehot_labels, tf.float32)

def batch_flatten(x):
    total_dim = np.prod(x.get_shape()[1:].as_list())
    return tf.reshape(x, [-1, total_dim])
import tensorflow as tf


X_tf = tf.Variable([[1, 2], [3, 4], [5, 6]], dtype=tf.int32)
print("Matrix X_tf:\n", X_tf)
print("Matrix Shape", tf.shape(X_tf))

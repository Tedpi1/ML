import tensorflow as tf
X_tf=tf.Variable([7,-3,2], dtype=tf.int32)
Y_tf=tf.Variable([1,4,-2], dtype=tf.int32)

xt_dot= tf.reduce_sum(tf.multiply(X_tf, Y_tf))
print("TensorFlow Dot product of X_tf and Y_tf is:", xt_dot)
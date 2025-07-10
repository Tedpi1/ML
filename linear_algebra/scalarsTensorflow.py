import tensorflow as tf

x_tf=tf.Variable(25, dtype=tf.int16)
print(x_tf)
x_s=x_tf.shape
print(x_s)
y_tf=tf.Variable(30, dtype=tf.int16)
sum_tf=x_tf + y_tf
print(sum_tf)
d_type=sum_tf.dtype
print(d_type)

n_stf=sum_tf.numpy()
print(n_stf)
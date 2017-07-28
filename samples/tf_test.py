import tensorflow as tf
sess = tf.Session()
hello = sess.run(tf.constant('Hello World'))
print(hello)

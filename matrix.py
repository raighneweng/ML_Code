import tensorflow as tf

matrix1 = tf.constant([[1,2]])
matrix2 = tf.constant([[1],[2]])
matrix3 = tf.constant([ [[1,2],[3,4],[5,6]], [[7,8],[9,10],[11,12]]])

neg1 = tf.negative(matrix1)

with tf.Session() as sess:
  res = sess.run(neg1)

print(matrix1)
print(matrix2)
print(matrix3)
print(res)
# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)

# sess = tf.Session()
# binding = {a: 1.5, b: 2.5}
# c = sess.run(add, feed_dict=binding)
# print(c)
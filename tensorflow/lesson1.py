#matrix multipul
import tensorflow as tf

matrix1 = tf.constant([[3,3]])

matrix2 = tf.constant([[2],[2]])

# import numpy
# matrix11 = ([[3,3]])
#
# matrix22 = ([[2],[2]])
# matrix3 = numpy.dot(matrix11,matrix22)
#
# print(matrix3 )

product = tf.matmul(matrix1,matrix2)
#
# sess = tf.Session()
#
# result = sess.run(product)
# print(result)
# sess.close()
#
# with tf.Session() as sess:
#     result = sess.run(product)
#     print(result)
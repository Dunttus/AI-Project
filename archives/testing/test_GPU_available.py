import tensorflow as tf

print("Hello, PyCharm, Docker and Tensorflow!")

print(f"TensorFlow: {tf.__version__}")
tf.config.list_physical_devices('GPU')

# Testing GPU tensor assignment
# https://www.tensorflow.org/guide/gpu
# You should see:
# Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0

tf.debugging.set_log_device_placement(True)
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)
print(c)

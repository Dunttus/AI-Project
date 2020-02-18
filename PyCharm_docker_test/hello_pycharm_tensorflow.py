import tensorflow as tf

print("Hello, PyCharm, Docker and Tensorflow!")

print(f"TensorFlow: {tf.__version__}")
tf.config.list_physical_devices('GPU')
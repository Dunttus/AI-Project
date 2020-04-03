from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd

# Loading test dataset
TEST_DATASET = \
    "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/apache_access_log/access_log_testing"
test_file_path = tf.keras.utils.get_file("access_log", TEST_DATASET)

# Separate with space and adding column names
df = pd.read_csv(TEST_DATASET, sep=" ", header=None)
df.columns = ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
print(df)

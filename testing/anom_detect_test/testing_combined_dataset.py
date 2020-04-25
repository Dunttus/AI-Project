# SOME TEST CODE NOT FUNCTIONAL STILL IN PROGRESS

# %%

import tensorflow as tf
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
import pickle


# %%

TEST_DATASET = \
    "http://192.168.10.61/~joni/combine_access.log"
test_file_path = tf.keras.utils.get_file("access_log", TEST_DATASET)

# %%

df = pd.read_csv(TEST_DATASET,
                 sep=' ', quotechar='"', escapechar=' ', header=None)
df.columns = ["time", "ip", "status", "byte", "rtime",
              "method", "url", "protocol"]
df2 = df.drop(['time', 'ip', 'protocol', 'url'], axis=1)
df3 = df.drop(['time', 'ip', 'status', 'byte', 'rtime',
               'method', 'method', 'protocol'], axis=1)

# %%

print(df3)

# %%

print(df2)

# %%


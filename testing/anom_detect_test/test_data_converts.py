# SOME TEST CODE NOT FUNCTIONAL STILL IN PROGRESS

# %%

import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# %%

TEST_DATASET = \
    "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/apache_access_log/good_access.log"
test_file_path = tf.keras.utils.get_file("access_log", TEST_DATASET)

# %%

df = pd.read_csv(TEST_DATASET,
                 sep=' ', quotechar='"', escapechar=' ', header=None)
df.columns = ["time", "ip", "status", "byte", "rtime",
              "method", "url", "protocol"]
df2 = df.drop(['time', 'ip', 'protocol'], axis=1)

# %%

print(df2)

# %%

df2['status'] = pd.Categorical(df2['status'])
df2['status'] = df2.status.cat.codes
df2['byte'] = pd.Categorical(df2['byte'])
df2['byte'] = df2.byte.cat.codes
df2['rtime'] = pd.Categorical(df2['rtime'])
df2['rtime'] = df2.rtime.cat.codes
print(df2)

# %%

tokenizer = Tokenizer(num_words=1000)
num_classes = max(df2['url']) + 1

df['url'] = tokenizer.texts_to_matrix(df2['url'], mode='binary')
df['url'] = keras.utils.to_categorical(df2.url, num_classes)
print(df2['url'])

# %%

tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(df2['method'])
df2['method'] = tokenizer.sequences_to_matrix(df2['method'], mode=tfidf2)
print(df['method'])

# %%

num_classes = max(df2.status) + 1
df2['url' = pd.Categorical(df2['url'])
print(df2['url')


# %%

df2['url'] = df2['url'].str.split("", expand = True)
df2['url'] = df2.time.cat.codes

# %%

print(df2)
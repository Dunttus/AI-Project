# SOME TEST CODE NOT FUNCTIONAL STILL IN PROGRESS

# %%

import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
import pickle
# %%
import pandas, numpy


def pandas_output_options():
    # Run the function to display all rows & columns in pandas dataframes
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)


def numpy_output_options():
    # Disable scientific notation in decimal values
    numpy.set_printoptions(suppress=True)
    # Show everything please
    numpy.set_printoptions(threshold=numpy.inf)
    numpy.set_printoptions(linewidth=numpy.inf)
    numpy.set_printoptions(precision=5)

pandas_output_options()
numpy_output_options()
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

tokenizer = Tokenizer(num_words=128, char_level=True)
#num_classes = max(df2['url']) + 1
tokenizer.fit_on_texts(df.url)
print(type(df.url))
#df['url'] = tokenizer.texts_to_sequences(df['url'])
textdata = pad(tokenizer.texts_to_sequences(df['url']), maxlen=64, padding='post')
textdata2 = tokenizer.texts_to_matrix(df['url'], mode='tfidf')
#textdata3 = tokenizer.sequences_to_matrix(textdata, mode='')

# %%
print(textdata)
print(textdata2)
#print(len(textdata))
#print(textdata3)

# %%
print(df.method)
tokenizer = Tokenizer(num_words=4, filters='')
tokenizer.fit_on_texts(df['method'])
catdata = tokenizer.texts_to_sequences(df.method)
print(catdata)
#df2['method'] = tokenizer.sequences_to_matrix(df2['method'], mode=tfidf2)
#print(df['method'])

# %%

num_classes = max(df2.status) + 1
df2['url' = pd.Categorical(df2['url'])
print(df2['url')


# %%

df2['url'] = df2['url'].str.split("", expand = True)
df2['url'] = df2.time.cat.codes

# %%

print(df2)
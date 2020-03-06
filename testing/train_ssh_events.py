#!/usr/bin/env python
# coding: utf-8

# Code works with PyCharm View --> Scientific mode or Jupyter notebook.
# Code not fully functional yet


# %%

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# %%

# test that GPU is working
print(f"TensorFlow: {tf.__version__}")
tf.config.list_physical_devices('GPU')


# %%

# Downloading .csv files from github to local computer
TRAIN_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events.csv"
TEST_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events.csv"
BAD_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/bad_ssh_events.csv"

# Naming dataset's
train_file_path = tf.keras.utils.get_file("train.csv", TRAIN_DATASET)
test_file_path = tf.keras.utils.get_file("test.csv", TEST_DATASET)
bad_file_path = tf.keras.utils.get_file("bad.csv", BAD_DATASET)


# %%

# Creating Pandas object "df"
df = pd.read_csv(TRAIN_DATASET)

# Creating Pandas object "dft"
dft = pd.read_csv(TEST_DATASET)

# Creating Pandas object "dfb"
dfb = pd.read_csv(BAD_DATASET)


# %%

# Testing to read pandas object BAD_DATASET first 5 lines
dfb.head()


# %%

# count number of TRAIN_DATASET logs
df.groupby('event.outcome')['event.outcome'].count()


# %%

# count number of TEST_DATASET logs
dft.groupby('event.outcome')['event.outcome'].count()


# %%

# count number of BAD_DATASET logs
dfb.groupby('event.outcome')['event.outcome'].count()


# %%

# Add new column predict with values 1 or 0
df['predict'] = 0
dfb['predict'] = 1


# %%

# Combine df and dfb into dfc
dfc = df.append(dfb)
print(dfc)


# %%

# count number of BAD_DATASET logs
dfc.groupby('event.outcome')['event.outcome'].count()


# %%

# Re-naming column names dfc
dfc.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo', 'event.outcome': 'event'},
           axis='columns', inplace=True)


# %%

# Convert dfc data from object to numeric category values
dfc['time'] = pd.Categorical(dfc['time'])
dfc['time'] = dfc.time.cat.codes
dfc['user'] = pd.Categorical(dfc['user'])
dfc['user'] = dfc.user.cat.codes
dfc['geo'] = pd.Categorical(dfc['geo'])
dfc['geo'] = dfc.geo.cat.codes
dfc['event'] = pd.Categorical(dfc['event'])
dfc['event'] = dfc.event.cat.codes
print(dfc)


# %%

# List data types of TRAIN_DATASET
dfc.tail()


# %%

# target value predict with pop
target = dfc.pop('predict')


# %%

dataset = tf.data.Dataset.from_tensor_slices((dfc.values, target.values))


# %%

# shuffle dfc dataset with new object train_dataset
train_dataset = dataset.shuffle(len(dfc)).batch(1)


# %%

# Making model
def training_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])
    return model


# %%

# Increasing accuracy of model, current value not optimised. Having high value may decrease model reliability.
model = training_model()
model.fit(train_dataset, epochs=2, verbose=1)


# %%

# Re-naming column names dft
dft.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo', 'event.outcome': 'event'},
           axis='columns', inplace=True)


# %%

# Convert dft data from object to numeric category values
dft['time'] = pd.Categorical(dft['time'])
dft['time'] = dft.time.cat.codes
dft['user'] = pd.Categorical(dft['user'])
dft['user'] = dft.user.cat.codes
dft['geo'] = pd.Categorical(dft['geo'])
dft['geo'] = dft.geo.cat.codes
dft['event'] = pd.Categorical(dft['event'])
dft['event'] = dft.event.cat.codes
print(dft)


# %%
dataset = tf.data.Dataset.from_tensor_slices((dft.values, target.values))


# %%

results = model.evaluate(dft)
print(results)


#%%
dft_test = dft[0]
predict = model.predict([dft_test])
print("Data: ")
print("Prediction: " + int(predict[0]))
print(results)


# %%

prediction = pd.DataFrame(dft)
print(prediction)


# %%


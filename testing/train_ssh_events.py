#!/usr/bin/env python
# coding: utf-8

# Code works with PyCharm View --> Scientific mode or Jupyter notebook.
# Code not fully functional yet

# %%

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pandas as pd
import numpy as np

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

# Re-naming column names df example: @timestamp --> time
df.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo', 'event.outcome': 'event'},
          axis='columns', inplace=True)
# Re-naming column names dfb
dfb.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo', 'event.outcome': 'event'},
          axis='columns', inplace=True)

# %%

# Convert df data from object to numeric category values
df['time'] = pd.Categorical(df['time'])
df['time'] = df.time.cat.codes
df['user'] = pd.Categorical(df['user'])
df['user'] = df.user.cat.codes
df['geo'] = pd.Categorical(df['geo'])
df['geo'] = df.geo.cat.codes
df['event'] = pd.Categorical(df['event'])
df['event'] = df.event.cat.codes

# Convert dfb data from object to numeric category values
dfb['time'] = pd.Categorical(dfb['time'])
dfb['time'] = dfb.time.cat.codes
dfb['user'] = pd.Categorical(dfb['user'])
dfb['user'] = dfb.user.cat.codes
dfb['geo'] = pd.Categorical(dfb['geo'])
dfb['geo'] = dfb.geo.cat.codes
dfb['event'] = pd.Categorical(dfb['event'])
dfb['event'] = dfb.event.cat.codes

# %%

# Add new column predict with values 1 or 0
df['predict'] = 0
dfb['predict'] = 1

# %%

# Reading pandas object TRAIN_DATASET first 5 lines test
dfb.head();


# %%

# List data types of TRAIN_DATASET
dfb.dtypes

# %%

# Combine df and dfb into dfc
dfc = df.append(dfb)
print(dfc)

# %%

# Count number of events in dfc
dfc.groupby('event')['event'].count()

# %%

# target value predict with pop
target = dfc.pop('predict')

# %%

dataset = tf.data.Dataset.from_tensor_slices((dfc.values, target.values))

# %%

# shuffle dfc dataset
train_dataset = dataset.shuffle(len(dfc)).batch(1)

# %%

# Teach model
inputs = {key: tf.keras.layers.Input(shape=(), name=key) for key in dfc.keys()}
x = tf.stack(list(inputs.values()), axis=-1)

x = tf.keras.layers.Dense(10, activation='relu')(x)
output = tf.keras.layers.Dense(1)(x)

model_func = tf.keras.Model(inputs=inputs, outputs=output)

model_func.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])


# %%

dict_slices = tf.data.Dataset.from_tensor_slices((dfc.to_dict('list'), target.values)).batch(16)

# %%

# Increasing accuracy of model, current value not optimised. Having high value may decrease model reliability.
model_func.fit(dict_slices, epochs=5)

# %%

# Re-naming column names dfb
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

prediction = pd.DataFrame(dft)
print(prediction)

# %%
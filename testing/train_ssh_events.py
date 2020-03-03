#!/usr/bin/env python
# coding: utf-8

# Code works with PyCharm View --> Scientific mode or Jupyter notebook.

# %%

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pandas as pd

# %%

# test that GPU is working
print(f"TensorFlow: {tf.__version__}")
tf.config.list_physical_devices('GPU')

# %%

# Downloading .csv files from github to local computer
TRAIN_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events.csv"
TEST_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events.csv"

# Naming dataset's
train_file_path = tf.keras.utils.get_file("train.csv", TRAIN_DATASET)
test_file_path = tf.keras.utils.get_file("test.csv", TEST_DATASET)

# %%

# Creating Pandas object "df"
df = pd.read_csv(TRAIN_DATASET)

# %%

# Reading pandas object TRAIN_DATASET first 5 lines test
df.head()

# %%

df.dtypes

# %%

# Creating Pandas object "dg"
dg = pd.read_csv(TEST_DATASET)

# %%

# Reading pandas object TEST_DATASET first 5 lines test
dg.head()

# %%

# count number of TRAIN_DATASET logs
df.groupby('event.outcome')['event.outcome'].count()

# %%

# count number of TEST_DATASET logs
dg.groupby('event.outcome')['event.outcome'].count()

# %%

# Re-naming column names example: @timestamp --> time
df.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo', 'event.outcome': 'event'},
          axis='columns', inplace=True)

# %%

# convert data from object to category values
df['time'] = pd.Categorical(df['time'])
df['time'] = df.time.cat.codes
df['user'] = pd.Categorical(df['user'])
df['user'] = df.user.cat.codes
df['geo'] = pd.Categorical(df['geo'])
df['geo'] = df.geo.cat.codes
df['event'] = pd.Categorical(df['event'])
df['event'] = df.event.cat.codes

# %%

# Reading pandas object TRAIN_DATASET first 5 lines test
df.head()

# %%

# List data types of TRAIN_DATASET
df.dtypes

# %%


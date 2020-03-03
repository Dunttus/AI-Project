#!/usr/bin/env python
# coding: utf-8

# Code works with PyCharm View --> Scientific mode or Jupyter notebook.

#%%

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pandas as pd

#%%

# test that GPU is working
print(f"TensorFlow: {tf.__version__}")
tf.config.list_physical_devices('GPU')

#%%

# Downloading .csv files from github to local computer
TRAIN_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events.csv"
TEST_DATASET = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events.csv"

# Naming dataset's
train_file_path = tf.keras.utils.get_file("train.csv", TRAIN_DATASET)
test_file_path = tf.keras.utils.get_file("test.csv", TEST_DATASET)

#%%

# Creating Pandas object "df"
df = pd.read_csv(TRAIN_DATASET)

#%%

# Reading pandas object TRAIN_DATASET first 5 lines test
df.head()

#%%

# Creating Pandas object "dg"
dg = pd.read_csv(TEST_DATASET)

#%%

# Reading pandas object TEST_DATASET first 5 lines test
dg.head()

#%%

# count number of TRAIN_DATASET logs
df.groupby('event.outcome')['event.outcome'].count()

#%%

# count number of TEST_DATASET logs
dg.groupby('event.outcome')['event.outcome'].count()

#%%

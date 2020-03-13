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
TRAIN_DATASET_GOOD = \
    "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_event_good.csv"
TRAIN_DATASET_BAD = \
    "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events_bad.csv"
TEST_DATASET_GOOD = \
    "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events_good.csv"
TEST_DATASET_BAD = \
    "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events_bad.csv"

# Naming dataset's
traing_file_path = tf.keras.utils.get_file("traing.csv", TRAIN_DATASET_GOOD)
trainb_file_path = tf.keras.utils.get_file("trainb.csv", TRAIN_DATASET_BAD)
testg_file_path = tf.keras.utils.get_file("testg.csv", TEST_DATASET_GOOD)
testb_file_path = tf.keras.utils.get_file("testb.csv", TEST_DATASET_BAD)

# %%

# Creating Pandas variable "dfTraingood"
dfTraingood = pd.read_csv(TRAIN_DATASET_GOOD)

# Creating Pandas variable "dfTrainbad"
dfTrainbad = pd.read_csv(TRAIN_DATASET_BAD)

# Creating Pandas variable "dfTestgood"
dfTestgood = pd.read_csv(TEST_DATASET_GOOD)

# Creating Pandas variable "dfTestbad"
dfTestbad = pd.read_csv(TEST_DATASET_BAD)

# %%

# Testing to read pandas object BAD_DATASET first 5 lines
dfTraingood.head()

# %%

# count number of TRAIN_DATASET_GOOD logs
dfTraingood.groupby('event.outcome')['event.outcome'].count()

# %%

# count number of TRAIN_DATASET_BAD logs
dfTrainbad.groupby('event.outcome')['event.outcome'].count()

# %%

# count number of TEST_DATASET_BAD logs
dfTestgood.groupby('event.outcome')['event.outcome'].count()

# %%

# count number of TEST_DATASET_BAD logs
dfTestbad.groupby('event.outcome')['event.outcome'].count()

# %%

# Add new column predict with values 0 as normal or 1 as not normal "labeling data"
dfTraingood['predict'] = 0
dfTrainbad['predict'] = 1

# %%

# Combine dfTraingood and dfTrainbad into dfTraincombined
dfTraincombined = dfTraingood.append(dfTrainbad)
print(dfTraincombined)

# %%

# count number of dfTraincombined logs
dfTraincombined.groupby('event.outcome')['event.outcome'].count()

# %%

# Re-naming column names of dfTraincombined
dfTraincombined.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo',
                        'event.outcome': 'event'}, axis='columns', inplace=True)

# %%

# Convert dfTraincombined data from object to numeric category values
dfTraincombined['time'] = pd.Categorical(dfTraincombined['time'])
dfTraincombined['time'] = dfTraincombined.time.cat.codes
dfTraincombined['user'] = pd.Categorical(dfTraincombined['user'])
dfTraincombined['user'] = dfTraincombined.user.cat.codes
dfTraincombined['geo'] = pd.Categorical(dfTraincombined['geo'])
dfTraincombined['geo'] = dfTraincombined.geo.cat.codes
dfTraincombined['event'] = pd.Categorical(dfTraincombined['event'])
dfTraincombined['event'] = dfTraincombined.event.cat.codes
print(dfTraincombined)

# %%

# List data types of data
dfTraincombined.dtypes

# %%

# target whole dataset dfTraincombined with value predict
target = dfTraincombined.pop('predict')

# %%

# Creating input pipeline from dataset for Tensorflow
dataset = tf.data.Dataset.from_tensor_slices((dfTraincombined.values, target.values))

# %%

dfTraincombined.head()

# %%

# shuffle dfc dataset with new object train_dataset
train_dataset = dataset.shuffle(len(dfTraincombined)).batch(1)


# %%

# Making model
def training_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(3, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])
    return model


# %%

# Starts building model
# Having more epochs increase accuracy of the model. Having too high value may decrease model reliability.
# 1 epochs take about 10-min with gtx 1050TI
model = training_model()
model.fit(train_dataset, epochs=2, verbose=1)

# %%

# Add new column predict with values 0 as normal or 1 as not normal "labeling data"
dfTestgood['predict'] = 0
dfTestbad['predict'] = 1

# %%

# Combine dfTestgood and dfTestbad into dfTestcombined
dfTestcombined = dfTestgood.append(dfTestbad)
print(dfTestcombined)

# %%

# Re-naming column names dfTestcombined
dfTestcombined.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo',
                       'event.outcome': 'event'}, axis='columns', inplace=True)

# %%

# Data types of dfTestcombined
dfTestcombined.dtypes

# %%

# Convert dfTestcombined data from object to numeric category values
dfTestcombined['time'] = pd.Categorical(dfTestcombined['time'])
dfTestcombined['time'] = dfTestcombined.time.cat.codes
dfTestcombined['user'] = pd.Categorical(dfTestcombined['user'])
dfTestcombined['user'] = dfTestcombined.user.cat.codes
dfTestcombined['geo'] = pd.Categorical(dfTestcombined['geo'])
dfTestcombined['geo'] = dfTestcombined.geo.cat.codes
dfTestcombined['event'] = pd.Categorical(dfTestcombined['event'])
dfTestcombined['event'] = dfTestcombined.event.cat.codes
print(dfTestcombined)

# %%

# Data types of dfTestcombined
dfTestcombined.dtypes

# %%

# target whole dataset dfTestcombined with value predict
target = dfTestcombined.pop('predict')

# %%

# Creating input pipeline from dataset for Tensorflow
datasetTest = tf.data.Dataset.from_tensor_slices((dfTestcombined.values, target.values))

# %%

# shuffle dfTestcombined dataset with new object test_dataset
test_dataset = datasetTest.shuffle(len(dfTestcombined)).batch(1)

# %%

# Evaluate model
results = model.evaluate(test_dataset)
print(results)

# %%

# Predictions from test dataset
prediction = model.predict(dfTestcombined)
print(prediction)

# %%

# First position result
np.argmax(prediction[0])


# %%

# Loop results
for i in range(277):
    fullRange = np.argmax(prediction[i])
    print(fullRange)


# %%

# Loop answers
for i in range(277):
    fullRanged = np.argmax(dfTestcombined)
    print(fullRanged)


# %%

# Predictions from test dataset
prediction = model.predict(dfTestcombined)
print(prediction)


# %%


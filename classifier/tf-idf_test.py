# Multi-class classifier for determining kernel log level from log message
import tensorflow as tf

from sklearn.model_selection import train_test_split as split
from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
#pd.set_option('display.max_rows', None)
DS_FILE = "../datasets/loglevels/training_logs.json"
# This is the full set containing DataFrame object
df = pd.read_json(DS_FILE, lines=True)

# Vectorize the text parts
tfidf = TfidfVectorizer()
score = tfidf.fit_transform(df.MESSAGE)

# The decimal value is given to each word in each entry. We need to put this
# data to correspond a certain log level value (PRIORITY)
print(score)
print(df.MESSAGE)

# Now is a good time to split the data?
TRAINING_SET, TEST_SET = split(df, test_size=0.2)


# Before this, message portion has to be converted into numeral form
# Convert dataset from pandaframe to tensorflow
# Switch the message datatype to float aswell when that is done.
#TRAINING_SET = tf.data.Dataset.from_tensor_slices(
#   (tf.cast(TRAINING_SET['PRIORITY'].values, tf.int8),
#   tf.cast(TRAINING_SET['MESSAGE'].values, tf.float32)))


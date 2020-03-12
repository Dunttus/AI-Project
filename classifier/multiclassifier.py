# Multi-class classifier for determining kernel log level from log message
# https://realpython.com/python-keras-text-classification/
import tensorflow as tf

from sklearn.model_selection import train_test_split as split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

DS_FILE = "../datasets/loglevels/training_logs.json"
# This is the full set containing DataFrame object
df = pd.read_json(DS_FILE, lines=True)
TRAINING_SET, TEST_SET = split(df, test_size=0.2)

print(f"Training set entries: {TRAINING_SET.size}")
print(f"Testing set entries: {TEST_SET.size}")

# Vectorizing the entires without any preprocessing
vectorizer = CountVectorizer()
TEST_V = vectorizer.fit(TEST_SET['MESSAGE'])
print(TEST_V.vocabulary_)


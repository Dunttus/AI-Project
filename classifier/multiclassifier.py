# Multi-class classifier for determining kernel log level from log message
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd

DS_FILE = "../datasets/loglevels/training_logs.json"
# This is the full set containing DataFrame object
df = pd.read_json(DS_FILE, lines=True)

TRAINING_SET, TEST_SET = train_test_split(df, test_size=0.2)
print(f"Training set entries: {TRAINING_SET.size}")
print(f"Testing set entries: {TEST_SET.size}")

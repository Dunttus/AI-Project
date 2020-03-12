# Multiclass classifier for determining kernel log level from log message
import tensorflow as tf
import pandas as pd

# Dataset locations
DS_LOC = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/loglevels/"
DS_FILE = "testfile.json"
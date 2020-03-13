# Basic classifying neural network
# Example code modified from Jeff Heaton's lecture series
# https://github.com/jeffheaton/t81_558_deep_learning

import pandas as pd
import io
import requests
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping

# The data contains iris flower metrics that is used to distinguish between
# 3 subspecies of irises (kurjenmiekka in finnish). 4 metrics and a class.
df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/iris.csv",
    na_values=['NA', '?'])


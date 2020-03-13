# Example code modified from Jeff Heaton's lecture series
# https://github.com/jeffheaton/t81_558_deep_learning

# Simple regression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
# Download example data into a pandas dataframe
df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/auto-mpg.csv",
    na_values=['NA', '?'])
print(df.columns)
cars = df['name']
# Missing value handling
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())
# Pandas to Numpy
x = df[['cylinders', 'displacement', 'horsepower', 'weight',
       'acceleration', 'year', 'origin']].values
y = df['mpg'].values # regression

# Build the neural network
model = Sequential()
# Input Layer and Hidden layer 1
# input_dim specifies the input layer: x.shape[1] value is 7
# We have 7 inputs (x columns)
model.add(Dense(25, input_dim=x.shape[1], activation='relu'))
# Hidden layer 2
model.add(Dense(10, activation='relu'))
# Output layer
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
# x is the input feature vector, consisting of car features/attributes
# y is the miles per gallon
model.fit(x,y,verbose=2,epochs=100)


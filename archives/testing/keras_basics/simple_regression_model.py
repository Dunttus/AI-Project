# Simple regression neural network
# Example code modified from Jeff Heaton's lecture series
# https://github.com/jeffheaton/t81_558_deep_learning

# The model trains different every time? Is this expected behavior?

# Reduce tensorflow logging level
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn import metrics
import pandas as pd
import numpy

# Pandas options to display everything
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Download example data into a pandas dataframe
df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/auto-mpg.csv",
    na_values=['NA', '?'])
cars = df['name']
# Missing value handling
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())
# Pandas to Numpy
car_stats = df[['cylinders', 'displacement', 'horsepower', 'weight',
       'acceleration', 'year', 'origin']].values
# Miles Per Gallon
actual_mpg = df['mpg'].values
# This tells something about the data format that is fed to the NN.
print("Data formatted and ready to be fed into the NN (second item of the set):")
print(car_stats[1])
print(actual_mpg[1])
# Build the neural network
model = Sequential()
# Input Layer and Hidden layer 1
# input_dim specifies the input layer: car_stats.shape[1] value is 7
# We have 7 inputs (car_stats columns)
model.add(Dense(25, input_dim=car_stats.shape[1], activation='relu'))
# Hidden layer 2
model.add(Dense(10, activation='relu'))
# Output layer
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
# car_stats is the input feature vector, consisting of car features/attributes
model.fit(car_stats, actual_mpg, verbose=2, epochs=100)

# Prediction using the model:
# We feed the model a new feature vector, and get a prediction!
# The first car has 18 mileage with the following stats:
chevy = df.head(n=1)
print("The first car in the dataset")
print(chevy)
chevy_stats = chevy[['cylinders', 'displacement', 'horsepower', 'weight',
       'acceleration', 'year', 'origin']].values
print("Prediction data fed into the model:")
print(chevy_stats)
print("Predicted mileage - actual mileage")
print(model.predict(chevy_stats), " - ", chevy[['mpg']].values)

# We can run the whole dataset into the model to measure prediction accuracy
# car_stats here is the very same set that was used to train the model
# actual_mpg is the set that contains correct mileages on the training set
predicted_mpg = model.predict(car_stats)
# Root-mean-square-error is used commonly for regression metrics
rmse = numpy.sqrt(metrics.mean_squared_error(predicted_mpg, actual_mpg))
# Average deviation from the real values
print("RMSE for the model: ", rmse)


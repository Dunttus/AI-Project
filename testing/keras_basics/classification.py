# Basic classifying neural network
# Example code modified from Jeff Heaton's lecture series
# https://github.com/jeffheaton/t81_558_deep_learning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# The data contains iris flower metrics that is used to distinguish between
# 3 subspecies of irises (kurjenmiekka in finnish). 4 metrics and a class.
df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/iris.csv",
    na_values=['NA', '?'])

# The 4 metrics are separated, this is the feature vector
flower_data = df[['sepal_l', 'sepal_w', 'petal_l', 'petal_w']].values
# The following code constructs a classification array, each class has it's
# 'checkbox' ticked: [setosa versicolor virginica]
# [1 0 0], [0 1 0] or [0 0 1]
# This is what is essentially called one-hot-encoding
dummies = pd.get_dummies(df['species'])
species = dummies.columns
classes = dummies.values

# The model
model = Sequential()
# Hidden layer 1
model.add(Dense(50, input_dim=flower_data.shape[1], activation='relu'))
# Hidden layer 2
model.add(Dense(25, activation='relu'))
# Output layer
model.add(Dense(classes.shape[1],activation='softmax'))
# In the compilation, loss function is chosen, as one-hot-encoding was done
# earlier.
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(flower_data,classes,verbose=2,epochs=100)

# Prediction accuracy, now we are seeing the results defined by the softmax
# function. So this is a probability distribution for the class the metrics
# likely refer to.
pred = model.predict(flower_data)
# Turns off scientific notation (3.51e-04 to 0.000351)
np.set_printoptions(suppress=True)
print(pred)
# Numpy argmax function picks the highest value
predictions = np.argmax(pred,axis=1)
correct_classes = np.argmax(classes,axis=1)
print(f"Predicted: {predictions}")
print(f"Correct: {correct_classes}")
# Turn these into class names:
print(species[predictions])

# Test scoring: Accuracy metrics from scikit-library
# Gives just a percentage of how many went right.
# Confidence level could be taken into account too!
print(f"Accuracy score: {accuracy_score(correct_classes,predictions)}")
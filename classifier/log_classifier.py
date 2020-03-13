# Linux log classifier
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical
import pandas as pd

# Data
FILE = "ubuntu_logs_tail.json"
#FILE = "../datasets/loglevels/training_logs.json"
df = pd.read_json(FILE, lines=True)
df = df[['PRIORITY', 'MESSAGE']] # ubuntu_logs_tail needs this

# Bring on the Tokenizer!
# default: filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
tok = Tokenizer(num_words=100, oov_token="<OOV>")
tok.fit_on_texts(df.MESSAGE)
# Here we see some numbers get attention, do we want that?
#print(tok.word_index)
#print(tok.word_counts)
# This is essentially the feature vector. Feed it to the NN!
log_text_data = pad(tok.texts_to_sequences(df.MESSAGE),maxlen=None)
# One-hot-encoding the classes
classes = to_categorical(df['PRIORITY'])

model = Sequential()
# Hidden layer 1
model.add(Dense(16, input_dim=log_text_data.shape[1], activation='relu'))
# Hidden layer 2
model.add(Dense(8, activation='relu'))
# Output layer
model.add(Dense(classes.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(log_text_data,classes,verbose=2,epochs=50)

# Predictions
pred = model.predict(log_text_data)
numpy.set_printoptions(suppress=True)
predictions = numpy.argmax(pred,axis=1)
correct_classes = numpy.argmax(classes,axis=1)
print(f"Predicted: {predictions}")
print(f"Correct: {correct_classes}")
print(f"Accuracy score: {accuracy_score(correct_classes,predictions)}")



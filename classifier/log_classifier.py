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
#FILE = "ubuntu_logs_tail.json"
FILE = "../datasets/loglevels/training_logs.json"
df = pd.read_json(FILE, lines=True)
#df = df[['PRIORITY', 'MESSAGE']] # ubuntu_logs_tail needs this

def log_message_tokenizer():
    # default: filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    tok = Tokenizer(num_words=1000, oov_token="<OOV>")
    tok.fit_on_texts(df.MESSAGE)
    return pad(tok.texts_to_sequences(df.MESSAGE),maxlen=None)

def training_model():
    model = Sequential()
    model.add(Dense(16, input_dim=log_text_data.shape[1], activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(classes.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

def evaluate_model():
    pred = model.predict(log_text_data)
    numpy.set_printoptions(suppress=True)
    predictions = numpy.argmax(pred, axis=1)
    correct_classes = numpy.argmax(classes, axis=1)
    print(f"Accuracy score: {accuracy_score(correct_classes, predictions)}")

log_text_data = log_message_tokenizer()
# One-hot-encode the classes
classes = to_categorical(df['PRIORITY'])
model = training_model()
model.fit(log_text_data,classes,verbose=2,epochs=50)
evaluate_model()



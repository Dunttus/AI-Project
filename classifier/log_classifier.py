# Linux log classifier
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy
import pandas as pd
import datetime as dt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as ttsplit
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical

# Data
#DATASET = "ubuntu_logs_tail.json"
DATASET = "../datasets/loglevels/training_logs.json"
df = pd.read_json(DATASET, lines=True)
#df = df[['PRIORITY', 'MESSAGE']] # ubuntu_logs_tail needs this

# Save the model and parameters used with a timestamp
VERSION = "v0.1-"
TIMESTAMP = dt.datetime.now().isoformat(timespec='minutes')
FILE = "model_files/lokari-" + VERSION + TIMESTAMP

MODEL_SAVEFILE = FILE + ".h5"
MODEL_METADATA_FILE = FILE + ".param"
MODEL_EVALUATION_DATA_FILE = FILE + ".score"

# Model parameters
TEST_SET_SIZE = 0.2
EPOCHS = 50

def log_message_tokenizer():
    # default: filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    tok = Tokenizer(num_words=2000, oov_token="<OOV>")
    tok.fit_on_texts(df.MESSAGE)
    return pad(tok.texts_to_sequences(df.MESSAGE),maxlen=None)

def training_model():
    model = Sequential()
    model.add(Dense(64, input_dim=log_text_data_train.shape[1], activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(classes_train.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

def evaluate_model():
    pred = model.predict(log_text_data_test)
    predictions = numpy.argmax(pred, axis=1)
    correct_classes = numpy.argmax(classes_test, axis=1)
    acc = accuracy_score(correct_classes, predictions)
    return acc

def print_confidence_levels():
    pred = model.predict(log_text_data_train)
    numpy.set_printoptions(suppress=True)
    numpy.set_printoptions(threshold=numpy.inf)
    numpy.set_printoptions(linewidth=numpy.inf)
    print(pred)

def save_parameters(file):
    with open(file,"w") as f:
        f.write(f"TEST_SET_SIZE = {TEST_SET_SIZE}\n")
        f.write(f"EPOCHS = {EPOCHS}\n")

def save_evaluation_date(file):
    with open(file, "w") as f:
        f.write(f"Accuracy: {str(round(evaluate_model(),4))}\n")


# The dataset
log_text_data_full = log_message_tokenizer()
# One-hot-encode the classes_train
classes_full = to_categorical(df['PRIORITY'])

# Split the set to train and test
log_text_data_train, log_text_data_test, classes_train, classes_test = ttsplit(
    log_text_data_full, classes_full, test_size=TEST_SET_SIZE)

model = training_model()
model.fit(log_text_data_train, classes_train, verbose=2, epochs=EPOCHS)
print_confidence_levels()

# Save the model and stats
model.save(MODEL_SAVEFILE)
save_parameters(MODEL_METADATA_FILE)
save_evaluation_date(MODEL_EVALUATION_DATA_FILE)

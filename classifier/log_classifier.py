# Linux log classifier
from os import environ as env
import numpy
import pandas
import datetime as dt
import json
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as ttsplit
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical

env['TF_CPP_MIN_LOG_LEVEL'] = '2'
TIMESTAMP = dt.datetime.now().isoformat(timespec='seconds')

# The dataset is read into pandas-dataframe
DATASET = "../datasets/loglevels/training_logs.json"
df = pandas.read_json(DATASET, lines=True)

MODEL = { "VERSION" : "v0.1",
          "timestamp" : TIMESTAMP }

# Model path/filename and file for saving the model and stats
FILE = "model_files/lokari"
MODEL_FILE = FILE + "-" + MODEL['VERSION'] + "-" + TIMESTAMP + ".h5"
MODEL_METRICS_FILE = FILE + "-" + MODEL['VERSION'] + ".json"

# Model parameters
PARAM = {
"test_set_size" : 0.2,
"epochs" : 100
}

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

def evaluate_accuracy():
    # This function should probably be made into separate file as a class
    pred = model.predict(log_text_data_test)
    predictions = numpy.argmax(pred, axis=1)
    correct_classes = numpy.argmax(classes_test, axis=1)
    acc = accuracy_score(correct_classes, predictions)
    return {"accuracy" : round(acc, 3)}

def print_confidence_levels():
    pred = model.predict(log_text_data_train)
    numpy.set_printoptions(suppress=True)
    numpy.set_printoptions(threshold=numpy.inf)
    numpy.set_printoptions(linewidth=numpy.inf)
    print(pred)

# Make text data into numerical format
log_text_data_full = log_message_tokenizer()

# One-hot-encode the classes_train
classes_full = to_categorical(df['PRIORITY'])

# Split the set to train and test
log_text_data_train, log_text_data_test, classes_train, classes_test = ttsplit(
    log_text_data_full, classes_full, test_size=PARAM['test_set_size'])

# Generate and train the model
model = training_model()
model.fit(log_text_data_train, classes_train, verbose=2, epochs=PARAM['epochs'])

# Save the model
model.save(MODEL_FILE)

# Get statistics
SCORE = evaluate_accuracy()
print(SCORE)
# Attach acquired data into MODEL version
MODEL['parameters'] = PARAM
MODEL['score'] = SCORE
# Write stats into the file
with open(MODEL_METRICS_FILE, "a") as f:
    json.dump(MODEL, f)
    f.write('\n')


#!/usr/bin/python3

# Lokari Linux Log classifier version 0.2
# Reads journalctl generated json file and tries to determine the printk
# level.

# Usage (current boot user logs as an example):
# NOTE: you have to grep the output, as the demo to_categorical/onehotencode
# fails if the dataset has entries without PRIORITY value
# journalctl -o json -b > filename.json
# grep '"PRIORITY"' filename.json > grepped_file.json
# ./demo.py grepped_file.json

from sys import argv
from os import environ as env
# Reduce Tensorflow output to console
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.utils import to_categorical as onehotencode
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score
import pandas
import numpy as np
import pickle

def run(model, data):

    # Check that messages are valid strings
    data.MESSAGE = data.MESSAGE.apply(datatype_check)

    # Separate loglevels from messages
    messages = data.MESSAGE
    real_loglevel = data.PRIORITY

    # Load tokenizer and convert message data to tfidf tokens
    with open('tfidf_tokenizer.pickle', 'rb') as file:
        tokenizer = pickle.load(file)
    tokenized_msgs = tokenizer.texts_to_matrix(messages, mode='tfidf')

    # Convert the correct answers into one-hot-encoded arrays
    tokenized_answers = onehotencode(real_loglevel)

    # Feed the data into the model
    pred = model.predict(tokenized_msgs)

    # Print the results in a nice format
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

    print("Message, distribution, predicted level, real level")
    for i in range(len(messages)):
        print(messages[i][:30], pred[i],
              np.argmax(pred[i]), real_loglevel[i])

    predictions = np.argmax(pred, axis=1)
    correct_classes = np.argmax(tokenized_answers, axis=1)
    acc = accuracy_score(correct_classes, predictions)
    print("Demoset accuracy: ", round(acc, 4) * 100, "%")
    return

def datatype_check(data):

    # We want all lines to be of type string
    if isinstance(data, str):
        return data

    else:
        # UTF-8 fails here, invalid continuation byte
        if isinstance(data, list):
            data = bytes(data).decode("latin-1")
            return data

        if data is None:
            data = ""
            return data
        else:
            print("ERROR: Format could not be converted: ", type(data))
            print(data)
            exit(1)

data = pandas.read_json(argv[1], lines=True)
model = load_model('Lokari-v0.2.h5')
run(model, data)
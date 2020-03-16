# Lokari log classifier

from os import environ as env
# Reduce Tensorflow output to console
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from datetime import datetime as dt
import pandas as pd
import numpy
from Lokari.nlp import basic_tokenizer
from Lokari.models import training_model
from Lokari.evaluate import accuracy
from tensorflow.keras.utils import to_categorical as onehotencode
from sklearn.model_selection import train_test_split as ttsplit

TIMESTAMP = dt.now().isoformat(timespec='seconds')
DATASET_PATH = '../datasets/loglevels/'
DATASET_FILE = 'training_logs.json'
MODEL = { "VERSION" : "v0.1",
          "timestamp" : TIMESTAMP }

PARAM = { "epochs" : 50 }

def main():
    print(f"Lokari-{MODEL['VERSION']}")
    data = pd.read_json(DATASET_PATH + DATASET_FILE, lines=True)

    messages_all = basic_tokenizer(data.MESSAGE)
    loglevels_all = onehotencode(data.PRIORITY)

    # Split the data to train/test sets
    messages_train, messages_test, loglevels_train, loglevels_test = ttsplit(
        messages_all, loglevels_all, test_size=0.2)

    # Compile the model, count input and output nodes from datasets
    input_nodes = messages_all.shape[1]
    output_nodes = loglevels_all.shape[1]
    model = training_model(input_nodes, output_nodes)

    # Train the model
    model.fit(messages_train, loglevels_train, verbose=2, epochs=PARAM['epochs'])

    # Save the model

    # Get evaluation data
    prediction = model.predict(messages_test)
    acc = accuracy(prediction, loglevels_test)
    print(acc)
    # Save evaluation data

# Output modifying functions for debugging purposes
def pandas_output_options():
    # Run the function to display all rows & columns in pandas dataframes
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

def numpy_output_options():
    # Disable scientific notation in decimal values
    numpy.set_printoptions(suppress=True)
    # Show everything please
    numpy.set_printoptions(threshold=numpy.inf)
    numpy.set_printoptions(linewidth=numpy.inf)

if __name__ == '__main__':
    pandas_output_options()
    numpy_output_options()
    main()

# Lokari log classifier

from os import environ as env
# Reduce Tensorflow output to console
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from datetime import datetime as dt
import pandas as pd
import numpy
from Lokari.nlp import basic_tokenizer
from tensorflow.keras.utils import to_categorical as onehotencode

TIMESTAMP = dt.now().isoformat(timespec='seconds')
DATASET_PATH = "../datasets/loglevels/"
DATASET_FILE = "testing_logs.json"
MODEL = { "VERSION" : "v0.1",
          "timestamp" : TIMESTAMP }

def main():
    print(f"Lokari-{MODEL['VERSION']}")
    data = pd.read_json(DATASET_PATH + DATASET_FILE, lines=True)

    message = basic_tokenizer(data.MESSAGE)
    loglevel = onehotencode(data.PRIORITY)
    print(message)
    print(loglevel)

    # Split the data to train/test sets

    # Generate and train the model

    # Save the model

    # Get evaluation data

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

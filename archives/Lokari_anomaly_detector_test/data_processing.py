from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def read_file():
    # This function reads the training data into a pandas dataframe
    df = pd.read_csv('../datasets/apache_access_log/access_log_testing',
                     sep=' ', quotechar='"', escapechar=' ', header=None)
    df.columns = ["time", "ip", "status", "byte", "rtime",
                  "method", "url", "protocol"]
    return df

def process_http_status_codes(data):
    # Does this data even need conversion?
    # We have a limited number of integers that we should be able to
    # feed to an embedding layer.

    # Convert dataframe into strings
    data = pd.Categorical(data.astype(str))
    data = data.codes
    return data

def process_text(data):
    tok = Tokenizer(num_words=64, filters='',
                    lower=False, split='',char_level=True)
    df['url'] = df['url'].astype(str)
    tok.fit_on_texts(df['url'])
    textdata = pad(tok.texts_to_sequences(df['url']), maxlen=64, padding='post')
    return data

# Create dataframe from a file
df = read_file()

# Initialize empty dataframe with column names
numdata = pd.DataFrame(columns=['status','byte','rtime','method'])

# Process and add status code data to final numdata vector
numdata['status'] = process_http_status_codes(df['status'])



print(numdata)
textdata = ()

#model.create(numdata,textdata)

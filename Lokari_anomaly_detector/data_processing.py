from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical as onehotencode

from Lokari_anomaly_detector import model

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def read_file():
    df = pd.read_csv('../datasets/apache_access_log/access_log_testing',
                     sep=" ", header=None)
    df.columns = ["time", "ip", "status", "byte", "rtime",
                  "method", "url", "protocol"]
    return df

def process_html_status_codes(data):
    #data = data.astype(str)

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

# Add status code data
numdata['status'] = process_html_status_codes(df['status'])



print(numdata)
textdata = ()

#model.create(numdata,textdata)
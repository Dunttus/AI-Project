from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers import Embedding, Input
from tensorflow.keras.models import Model

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def read_file():
    # This function reads the training data into a pandas dataframe
    df = pd.read_csv('../../datasets/apache_access_log/access_log_testing',
                     sep=' ', quotechar='"', escapechar=' ', header=None)
    df.columns = ["time", "ip", "status", "byte", "rtime",
                  "method", "url", "protocol"]
    return df

def process_http_status_codes(data):

    data = pd.Categorical(data.astype(str))
    data = data.codes
    return data


# Create dataframe from a file
df = read_file()

# Initialize empty dataframe with column names
numdata = pd.DataFrame(columns=['status'])

# Process and add status code data to final numdata vector
numdata['status'] = process_http_status_codes(df['status'])

# Test embedding layer



print(numdata)


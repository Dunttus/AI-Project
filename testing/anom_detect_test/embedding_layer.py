from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers import Embedding, Input, Dense, Flatten
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
# input_dim: int > 0. Size of the vocabulary, i.e. maximum integer index + 1.
status_input = Input(shape=numdata.shape[1], name='status_input')
status_emb = Embedding(output_dim=10, input_dim=5, input_length=1)(status_input)
status_flat = Flatten()(status_emb)
status_output = Dense(5, activation='relu')(status_flat)
model = Model(inputs=status_input, outputs=status_output)
model.compile(optimizer='adam', loss='categorical_crossentropy')
output_array = model.predict(numdata)
print(model.summary())
print(numdata)
print(output_array)
# TODO: decide output array size


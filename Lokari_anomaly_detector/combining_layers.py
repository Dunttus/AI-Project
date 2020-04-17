from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers \
    import Embedding, Input, Dense, Flatten, concatenate
from tensorflow.keras.models import Model

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
    data = pd.Categorical(data.astype(str))
    data = data.codes
    return data


def http_status_layer(data):
    inp = Input(shape=data.shape[1], name='status_input')
    emb = Embedding(output_dim=10, input_dim=5, input_length=1)(inp)
    flat = Flatten()(emb)
    outp = Dense(5, activation='relu')(flat)
    return inp, outp


def method_layer(data):
    inp = Input(shape=data.shape[1], name='method_input')
    emb = Embedding(output_dim=10, input_dim=5, input_length=1)(inp)
    flat = Flatten()(emb)
    outp = Dense(9, activation='relu')(flat)
    return inp, outp

# Create dataframe from a file
df = read_file()

# Process and add status data
status = pd.DataFrame() #(columns=['status'])
status['tokens'] = process_http_status_codes(df['status'])
print(status.tokens)
st_in, st_out = http_status_layer(status)

# Process and add method data
method = pd.DataFrame() #(columns=['status'])
method['tokens'] = process_http_status_codes(df['method'])
print(method.tokens)
met_in, met_out = method_layer(method)


# Construct the model

# Combine the outputs to a single output
output = concatenate([st_out, met_out])
output = Dense(14, activation='relu')(output)
output = Dense(1, activation='relu')(output)
model = Model(inputs=[st_in, met_in], outputs=[output])
model.compile(optimizer='adam', loss='binary_crossentropy')

# Train model MISSING STILL

# This output is untrained model, unclear how to interpret this...
output_array = model.predict([status, method])
print(model.summary())
print(output_array)



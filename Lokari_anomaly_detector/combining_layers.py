from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers \
    import Embedding, Input, Dense, Flatten, concatenate
from tensorflow.keras.models import Model

import numpy
# Disable scientific notation in decimal values
numpy.set_printoptions(suppress=True)
# Show everything please
numpy.set_printoptions(threshold=numpy.inf)
numpy.set_printoptions(linewidth=numpy.inf)
numpy.set_printoptions(precision=5)


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
    outp = Dense(1, activation='relu')(flat)
    return inp, outp


def method_layer(data):
    inp = Input(shape=data.shape[1], name='method_input')
    emb = Embedding(output_dim=10, input_dim=5, input_length=1)(inp)
    flat = Flatten()(emb)
    outp = Dense(1, activation='relu')(flat)
    return inp, outp

# Create dataframe from a file
df = read_file()

# Process and add status data
status = pd.DataFrame() #(columns=['status'])
status['status'] = process_http_status_codes(df['status'])
print(status.status)
st_in, st_out = http_status_layer(status)

# Process and add method data
method = pd.DataFrame() #(columns=['status'])
method['method'] = process_http_status_codes(df['method'])
print(method.method)
met_in, met_out = method_layer(method)


# Combine the outputs to a single output
output = concatenate([st_out, met_out])

# Symmetric autoencoder
output = Dense(10, activation='relu')(output)
output = Dense(10, activation='relu')(output)
output = Dense(20, activation='relu')(output)
output = Dense(5, activation='relu')(output)
output = Dense(20, activation='relu')(output)
output = Dense(10, activation='relu')(output)
output = Dense(10, activation='relu')(output)

# The final output corresponds to the concatenated input layer.
output = Dense(14, activation='relu')(output)

model = Model(inputs=[st_in, met_in], outputs=[st_out, met_out])
model.compile(optimizer='adam', loss='mse')
print(model.summary())
# Train the autoencoder!

model.fit([status, method],[status,method],epochs=500)

# This output is untrained model, unclear how to interpret this...
output_array = model.predict([status, method])
print(output_array)



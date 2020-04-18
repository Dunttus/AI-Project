from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers \
    import Embedding, Input, Dense, Flatten, Concatenate, Reshape
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

train_data = '../datasets/apache_access_log/access_log_testing'
test_data = '../datasets/apache_access_log/access_log_compare'

def read_file(FILE):
    # This function reads the training data into a pandas dataframe
    df = pd.read_csv(FILE,
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
    outp = Dense(10, activation='relu')(flat)
    return inp, outp


def method_layer(data):
    inp = Input(shape=data.shape[1], name='method_input')
    emb = Embedding(output_dim=10, input_dim=5, input_length=1)(inp)
    flat = Flatten()(emb)
    outp = Dense(10, activation='relu')(flat)
    return inp, outp

# Create dataframe from a file
df = read_file(train_data)

# Process and add status data
status = pd.DataFrame()
status['tokens'] = process_http_status_codes(df['status'])
print(status.tokens)
st_in, st_out = http_status_layer(status)

# Process and add method data
method = pd.DataFrame()
method['tokens'] = process_http_status_codes(df['method'])
print(method.tokens)
met_in, met_out = method_layer(method)

# Merge the layers, could use the Dot layer here too to combine them already
outputmerge = Concatenate(name='o_cat', axis=1)([st_out, met_out])

# Symmetric autoencoder
output = Dense(20, activation='relu')(outputmerge)
output = Dense(40, activation='relu')(output)
output = Dense(10, activation='relu')(output)
output = Dense(40, activation='relu')(output)
output = Dense(20, activation='relu')(output)
# The outputs have to match the last layer of the model
final1 = Dense(1, activation='relu')(output)
final2 = Dense(1, activation='relu')(output)
#final1 = Reshape((1,))(final1)
#final2 = Reshape((1,))(final2)

model = Model(inputs=[st_in, met_in], outputs=[final1, final2])
model.compile(optimizer='adam', loss='mse')
print(model.summary())

# Train the autoencoder
model.fit([status, method],[status,method],epochs=10)

# Mean square error for each input.
# These approach zero when model can reshape it's own input?
output_array = model.predict([status, method])
print(output_array)

# Use the model: test what happens on another kind of input
# At this point, need a consistent way of categorizing the inputs.
# The last log line of the access_log_compare
# has been edited to contain unseen combination.

df2 = read_file(test_data)
status2 = pd.DataFrame()
status2['tokens'] = process_http_status_codes(df2['status'])
method2 = pd.DataFrame()
method2['tokens'] = process_http_status_codes(df2['method'])

output_array2 = model.predict([status2, method2])
print(output_array2)

# NOTES: There is a difference that can bee seen. Sometimes the values
# zero out.
# TODO: include url to data
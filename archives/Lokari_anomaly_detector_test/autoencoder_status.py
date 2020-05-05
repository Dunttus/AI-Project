from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers \
    import Embedding, Input, Dense, Flatten, concatenate
from tensorflow.keras.models import Model

import numpy
# Disable scientific notation in decimal values
numpy.set_printoptions(suppress=True)
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


def categorize_http_status_codes(data):
    data = pd.Categorical(data.astype(str))
    data = data.codes
    return data

# Create dataframe from a file
df = read_file()

# Process and add status data
data = pd.DataFrame()
data['status'] = categorize_http_status_codes(df['status'])
print(data.status)

# Embedding model, makes 10 float array of the data
inp = Input(shape=data.shape[1], name='status_input')
emb = Embedding(output_dim=10, input_dim=5, input_length=1)(inp)
flat = Flatten()(emb)
output = Dense(10, activation='relu')(flat)

embedder = Model(inputs=inp, outputs=output)
embedder.compile(optimizer='adam', loss='mse')
print(embedder.predict(data))
print(embedder.summary())
# Symmetric autoencoder
#output = Dense(20, activation='relu')(output)
#output = Dense(5, activation='relu')(output)
#output = Dense(20, activation='relu')(output)
#output = Dense(10, activation='relu')(output)

# The final output corresponds to the input layers?
#output = Dense(14, activation='relu')(output)


#model = Model(inputs=inp, outputs=output)
#model.compile(optimizer='adam', loss='mse')
#print(model.summary())
# Train the autoencoder!
#model.fit([status, method],[status,method],epochs=500)

# Mean square error for each input.
#output_array = model.predict(data)
#print(output_array)



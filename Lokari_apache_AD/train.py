# Lokari Apache log anomaly detector:
# Train the baseline model
from os import environ as env
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense
from tensorflow.keras.models import Model
from Lokari_apache_AD.autoencoder.model import construct_model
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad


# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Read training data
data = read('training_dataset/good_access.log')

# Process training data
# Returns: ['status', 'byte', 'rtime', 'method'] and tokenized url text as
# numpy array.
data, urldata = process_apache_log(data)
#print(urldata)

# Construct the model
model = construct_model(data, urldata)


# Train the model
# neural network is trained to learn an average presentation of usual data


# Testing
def test_status_input():
    inp = Input(shape=1, name='status')
    emb = Embedding(input_dim=10, output_dim=10, input_length=1)(inp)
    flat = Flatten()(emb)
    out = Dense(10, activation='relu')(flat)

    model = Model(inputs=[inp], outputs=[out])
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    print(model.summary())
    output_array = model.predict(data.status)
    print(output_array)
    return

def test_url_input():
    inp = Input(shape=urldata.shape[1], name='url')
    emb = Embedding(input_dim=128, output_dim=32, input_length=52)(inp)
    flat = Flatten()(emb)
    out = Dense(32, activation='relu')(flat)

    model = Model(inputs=[inp], outputs=[out])
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    print(model.summary())
    output_array = model.predict(urldata)
    print(output_array)
    return


#test_url_input()

# Save the model
# the model is saved to a file to use with the monitor.py



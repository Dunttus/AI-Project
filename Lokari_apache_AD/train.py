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
# Returns: ['status', 'byte', 'rtime', 'method', 'url']
data = process_apache_log(data)
#print(data)

# Have to have numpy arrays!
# Testing with model.predict fails with
# ValueError: Failed to convert a NumPy array to a Tensor
# (Unsupported object type list).

# Construct the model
#model = construct_model(data)

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
    inp = Input(shape=1, name='url')
    emb = Embedding(input_dim=10, output_dim=10, input_length=1)(inp)
    flat = Flatten()(emb)
    out = Dense(10, activation='relu')(flat)

    model = Model(inputs=[inp], outputs=[out])
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    print(model.summary())
    output_array = model.predict(data.url)
    print(output_array)
    return

#test_status_input()
#data.url = pad(data.url)
#print(data.url)
#test_url_input()

# Save the model
# the model is saved to a file to use with the monitor.py



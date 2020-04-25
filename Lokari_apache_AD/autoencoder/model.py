# Main model construction code, returns an instance of Model
# viewable with print((model.summary())

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense


# These processing functions need to be linked to these!
# Data shapes have to match


def http_status_layer(data):

    inp = Input(shape=data.shape[1], name='status_input')
    # input_dim: how many categories altogether?
    # output_dim: how many embeddings to create?
    emb = Embedding(input_dim=7, output_dim=32, input_length=1)(inp)
    flat = Flatten()(emb)
    outp = Dense(32, activation='relu')(flat)
    return inp, outp


def method_layer(data):
    inp = Input(shape=data.shape[1], name='method_input')
    emb = Embedding(input_dim=5, output_dim=20, input_length=1)(inp)
    flat = Flatten()(emb)
    outp = Dense(32, activation='relu')(flat)
    return inp, outp


def url_layer(data):
    inp = Input(shape=data.shape[1], name='url_input')
    outp = Dense(64, activation='relu')(inp)
    return inp, outp


def autoencoding_layers():

    return


def construct_model():

    return model


input_list = []
output_list = []
model = Model(inputs=input_list, outputs=output_list)
# Check the loss function, binary?
model.compile(optimizer='adam̈́', loss='categorical_crossentropy')
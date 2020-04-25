# Main model construction code, returns an instance of Model
# viewable with print((model.summary())

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense


# These processing functions need to be linked to these!
# Data shapes have to match


def http_status_layer(data):

    inp = Input(name='status_input',shape=data.shape)
    # input_dim: how many categories altogether?
    # output_dim: how many embeddings to create?
    # With http status codes, how many are of significance?
    # The Out-Of-Vocabulary context should be done in processing stage!
    emb = Embedding(input_dim=7, output_dim=32, input_length=1)(inp)
    outp = Flatten()(emb)
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

def bytes_rtime_input(data):

    return


def autoencoding_layers():

    return

def construct_model(data):

    print(data.status)
    input_list = []
    output_list = []
    # ['status', 'byte', 'rtime', 'method', 'url']
    io_status = http_status_layer(data.status)
    input_list.append(io_status[0])
    output_list.append(io_status[1])

    print(input_list)
    print(output_list)


    model = Model(inputs=input_list, outputs=output_list)
    # Check the loss function, binary?
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    print(model.summary())

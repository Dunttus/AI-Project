# Main model construction code, returns an instance of Model
# viewable with print((model.summary())

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad

# These processing functions need to be linked to these!
# Data shapes have to match


def http_status_layer(data):
    inp = Input(name='status_input',shape=data.shape)
    # input_dim: how many categories altogether?
    # output_dim: how many embeddings to create?
    # With http status codes, how many are of significance?
    # The Out-Of-Vocabulary context should be done in processing stage!
    emb = Embedding(input_dim=20, output_dim=10, input_length=1)(inp)
    outp = Flatten()(emb)
    return inp, outp


def bytes_layer(data):
    inp = Input(name='bytes_input', shape=data.shape)
    outp = Dense(1, activation='relu')(inp)
    return inp, outp


def rtime_layer(data):
    inp = Input(name='rtime_input', shape=data.shape)
    outp = Dense(1, activation='relu')(inp)
    return inp, outp


def method_layer(data):
    inp = Input(name='method_input', shape=data.shape)
    emb = Embedding(input_dim=7, output_dim=4, input_length=1)(inp)
    outp = Flatten()(emb)
    return inp, outp


def url_layer(data):
    # Pad the data here! This really should be done in the process.py, this
    # is a workaround because the datatypes don't fit well together. Done
    # here, the padding function works out of the box.
    data = pad(data)
    inp = Input(name='url_input', shape=data.shape)
    # TODO: Check word level tokenizing options, ref process.py tokenize_url
    # TODO: Check input_length relation to data.shape
    emb = Embedding(input_dim=128, output_dim=32, input_length=128)(inp)
    outp = Flatten()(emb)
    return inp, outp


def autoencoding_layers():

    return


def fill_io_lists(data):

    input_list = []
    output_list = []
    io_status = http_status_layer(data.status)
    input_list.append(io_status[0])
    output_list.append(io_status[1])

    io_bytes = bytes_layer(data.byte)
    input_list.append(io_bytes[0])
    output_list.append(io_bytes[1])

    io_rtime = rtime_layer(data.rtime)
    input_list.append(io_rtime[0])
    output_list.append(io_rtime[1])

    io_method = method_layer(data.method)
    input_list.append(io_method[0])
    output_list.append(io_method[1])

    io_url = url_layer(data.url)
    input_list.append(io_url[0])
    output_list.append(io_url[1])

    return input_list, output_list


def construct_model(data):

    #print(data)
    input_list, output_list = fill_io_lists(data)

    print(input_list)
    print(output_list)


    model = Model(inputs=input_list, outputs=output_list)
    # Check the loss function, binary?
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    print(model.summary())

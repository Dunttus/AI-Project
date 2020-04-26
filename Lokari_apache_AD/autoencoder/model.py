# Main model construction code, returns an instance of Model
# viewable with print((model.summary())

from tensorflow.keras.models import Model
from tensorflow.keras.layers import \
    Input, Embedding, Flatten, Dense, Concatenate

# These processing functions need to be linked to these!
# Data shapes have to match


def http_status_layer(data):
    inp = Input(name='status_input',shape=1)

    # Embedding layer
    # input_dim: how many categories altogether?
    # output_dim: how many embeddings to create?
    # With http status codes, how many are of significance?
    # The Out-Of-Vocabulary context should be done in processing stage!
    emb = Embedding(input_dim=20, output_dim=10, input_length=1)(inp)
    outp = Flatten()(emb)
    return inp, outp


def bytes_layer(data):
    inp = Input(name='bytes_input', shape=1)
    outp = Dense(1, activation='relu')(inp)
    return inp, outp


def rtime_layer(data):
    inp = Input(name='rtime_input', shape=1)
    outp = Dense(1, activation='relu')(inp)
    return inp, outp


def method_layer(data):
    inp = Input(name='method_input', shape=1)
    emb = Embedding(input_dim=7, output_dim=4, input_length=1)(inp)
    outp = Flatten()(emb)
    return inp, outp


def url_layer(data):
    inp = Input(name='url_input', shape=data.shape[1])
    # TODO: Check word level tokenizing options, ref process.py tokenize_url
    # TODO: Check input_length relation to data.shape
    emb = Embedding(input_dim=128, output_dim=16, input_length=52)(inp)
    outp = Flatten()(emb)
    return inp, outp


def fill_io_lists(data, urldata):

    input_list, output_list = [], []

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

    io_url = url_layer(urldata)
    input_list.append(io_url[0])
    output_list.append(io_url[1])

    return input_list, output_list


def add_autoencoding_layers(merged_input):

    output = Dense(512, activation='relu')(merged_input)
    output = Dense(256, activation='relu')(output)
    output = Dense(128, activation='relu')(output)
    output = Dense(32, activation='relu')(output)
    output = Dense(128, activation='relu')(output)
    output = Dense(256, activation='relu')(output)
    output = Dense(512, activation='relu')(output)

    # Final outputs, need to have 5 of them. Might be a better solution
    # somewhere, but outputs have to correspond the inputs to train
    # the autoencoder properly.

    final_output_list = []

    # TODO: get output sizes from the data itself rather than manually
    # This is bound to break! Testing dataset has longest url text
    # of 52 length.

    final_output_list.append(Dense(1, name='status')(output))
    final_output_list.append(Dense(1, name='byte')(output))
    final_output_list.append(Dense(1, name='rtime')(output))
    final_output_list.append(Dense(1, name='method')(output))
    final_output_list.append(Dense(52, name='url')(output))

    return final_output_list


def construct_model(data, urldata):

    #print(data)
    input_list, output_list = fill_io_lists(data, urldata)

    # Merge the output layers from input
    merged_input = Concatenate(name='concat', axis=1)(output_list)

    # Add the autoencoder proper
    final_output_list = add_autoencoding_layers(merged_input)

    model = Model(inputs=input_list, outputs=final_output_list)

    model.compile(optimizer='adam', loss='mse')
    print(model.summary())

    # Train the autoencoder
    model.fit([data.status, data.byte, data.rtime, data.method, urldata],
              [data.status, data.byte, data.rtime, data.method, urldata],
              epochs=1000)


# TODO: save function, save to dir: saved_tokenizers/
def save_tokenizer():

    return


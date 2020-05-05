from tensorflow.keras.layers import Input, Embedding, Flatten, Dense
import config as config


def fill_io_lists(data, urldata):

    # Initialize empty lists
    input_list, output_list = [], []

    # Call individual functions to create model inputs and outputs to
    # concatenating layer.
    io_status = http_status_input(data.status)
    input_list.append(io_status[0])
    output_list.append(io_status[1])

    io_bytes = bytes_input(data.byte)
    input_list.append(io_bytes[0])
    output_list.append(io_bytes[1])

    io_rtime = rtime_input(data.rtime)
    input_list.append(io_rtime[0])
    output_list.append(io_rtime[1])

    io_method = method_input(data.method)
    input_list.append(io_method[0])
    output_list.append(io_method[1])

    io_url = url_input(urldata)
    input_list.append(io_url[0])
    output_list.append(io_url[1])

    return input_list, output_list


def http_status_input(data):
    inp = Input(name='status_input',shape=1)

    # TODO: transport these parameters to config
    # Embedding layer
    # input_dim: how many categories altogether?
    # output_dim: how many embeddings to create?
    # With http status codes, how many are of significance?
    # The Out-Of-Vocabulary context should be done in processing stage!
    emb = Embedding(input_dim=20, output_dim=10, input_length=1)(inp)
    outp = Flatten()(emb)
    return inp, outp


def bytes_input(data):
    inp = Input(name='bytes_input', shape=1)
    outp = Dense(1, activation='relu')(inp)
    return inp, outp


def rtime_input(data):
    inp = Input(name='rtime_input', shape=1)
    outp = Dense(1, activation='relu')(inp)
    return inp, outp


def method_input(data):
    inp = Input(name='method_input', shape=1)
    emb = Embedding(input_dim=7, output_dim=4, input_length=1)(inp)
    outp = Flatten()(emb)
    return inp, outp


def url_input(data):
    inp = Input(name='url_input', shape=data.shape[1])
    # TODO: Check word level tokenizing options, ref process.py tokenize_url
    # TODO: Check input_length relation to data.shape
    emb = Embedding(input_dim=128, output_dim=16,
                    input_length=config.URL_LENGTH)(inp)
    outp = Flatten()(emb)
    return inp, outp

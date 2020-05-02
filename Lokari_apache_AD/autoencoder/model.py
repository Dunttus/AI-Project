# Main mdel construction code, returns an instance of Model
# viewable with print((model.summary())

from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import \
    Input, Embedding, Flatten, Dense, Concatenate
import Lokari_apache_AD.config as config
import matplotlib.pyplot as plt


def construct_model(data, urldata):

    # Generate inputs for the incoming data and outputs for concatenating layer
    input_list, output_list = fill_io_lists(data, urldata)

    # Merge the output layers from input
    merged_input = Concatenate(name='concat', axis=1)(output_list)

    # Add the autoencoder proper
    final_output_list = add_autoencoding_layers(merged_input)
    model = Model(inputs=input_list, outputs=final_output_list)

    monitor = model_monitor()

    model.compile(optimizer='adam',
                  loss='mse')
    print(model.summary())

    # Train the autoencoder
    history = model.fit(
            [data.status, data.byte, data.rtime, data.method, urldata],
            [data.status, data.byte, data.rtime, data.method, urldata],
            epochs=config.EPOCHS,
            callbacks=[monitor]
    )

    if config.SAVE:
        model_file = 'saved_models/' + config.VERSION + \
                     '/Lokari-v' + config.VERSION + '.h5'
        model.save(model_file)
        plot_training(history)


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


def add_autoencoding_layers(merged_input):

    output = Dense(256, activation='relu')(merged_input)
    output = Dense(128, activation='relu')(output)
    output = Dense(16, activation='relu')(output)
    output = Dense(128, activation='relu')(output)
    output = Dense(256, activation='relu')(output)

    final_output_list = [Dense(1, name='status')(output),
                         Dense(1, name='byte')(output),
                         Dense(1, name='rtime')(output),
                         Dense(1, name='method')(output),
                         Dense(config.URL_LENGTH, name='url')(output)]

    return final_output_list


def model_monitor():

    mon = EarlyStopping(
            monitor='loss',
            min_delta=config.MIN_DELTA,
            patience=config.PATIENCE,
            verbose=1,
            mode='auto',
            restore_best_weights=True
            )

    return mon


def plot_training(history):

    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['status_loss'], label='Status')
    plt.plot(history.history['byte_loss'], label='Byte')
    plt.plot(history.history['rtime_loss'], label='Request time')
    plt.plot(history.history['method_loss'], label='Method')
    plt.plot(history.history['url_loss'], label='Url')
    plt.yscale('log')
    plt.legend()
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plot_file = 'saved_models/' + config.VERSION + \
                '/training_plot-' + config.VERSION + '.png'
    plt.savefig(plot_file)

    return

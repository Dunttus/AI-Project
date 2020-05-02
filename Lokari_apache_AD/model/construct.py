# Main mdel construction code, returns an instance of Model
# viewable with print((model.summary())

from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Concatenate
from Lokari_apache_AD.model.inputs import fill_io_lists
import Lokari_apache_AD.config as config
import matplotlib.pyplot as plt


def construct_model(data, urldata):

    # Generate inputs for the incoming data and outputs for concatenating layer
    input_list, output_list = fill_io_lists(data, urldata)

    # Merge the output layers from all the inputs
    merged_input = Concatenate(name='concat', axis=1)(output_list)

    # Add the autoencoder proper
    final_output_list = add_autoencoding_layers(merged_input)
    model = Model(inputs=input_list, outputs=final_output_list)

    monitor = model_monitor()

    # TODO: Check additional compiling options
    model.compile(optimizer='adam',
                  loss='mse')
    print(model.summary())

    # Train the autoencoder, history assignment is for graphics
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

    return model


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

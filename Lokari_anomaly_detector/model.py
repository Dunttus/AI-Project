from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.layers import Input, Dense, concatenate
from tensorflow.keras.models import Model


def anom_model(numdata, textdata):

    num_input = Input(shape=numdata.shape[1], name='num_input')
    text_input = Input(shape=textdata.shape[1], name='text_input')

    # NLP branch:
    first_nlp = Dense(64, activation='relu')(text_input)
    second_nlp = Dense(32, activation='relu')(first_nlp)
    nlp_output = Dense(8, activation='relu')(second_nlp)

    # Combining the branches with concatenate
    # Autoencoding layer: 8 + 4 inputs and outputs
    # Concatenation is done for 8 layers from nlp_output and 4 from num_input
    output = concatenate([num_input, nlp_output])
    output = Dense(12, activation='sigmoid')(output)
    output = Dense(1, activation='sigmoid')(output)
    model = Model(inputs=[num_input, text_input], outputs=[output])

    # Check: Loss function! Normalization in the autoencoding phase??
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=None,
                  loss_weights=None, sample_weight_mode=None,
                  weighted_metrics=None, target_tensors=None)

    # All options
    # y value is the same as input?? Check this in depth
    #model.fit(x=[numdata, textdata],
    #          y=None,
    #          batch_size=None,
    #          epochs=10, verbose=1,
    #          callbacks=None, validation_split=0.0, validation_data=None,
    #          shuffle=True, class_weight=None, sample_weight=None,
    #          initial_epoch=0, steps_per_epoch=None, validation_steps=None,
    #          validation_freq=1, max_queue_size=10, workers=1,
    #          use_multiprocessing=False)
    return model
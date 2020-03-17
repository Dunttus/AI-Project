from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

def training_model(i_nodes, o_nodes):

    model = Sequential()
    model.add(Dense(64, input_dim=i_nodes, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(o_nodes, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model

def new_training_model(i_nodes, o_nodes):

    model = Sequential()
    model.add(Dense(256, input_dim=i_nodes, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(o_nodes, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model


def model_monitor():
    # This monitor stops when no new learning is occurring
    # check: val_loss, min_delta, mode
    # patience = how many epochs can pass without improvement
    mon = EarlyStopping(
        monitor='val_loss',
        min_delta=1e-3,
        patience=10,
        verbose=1,
        mode='auto',
        restore_best_weights=True
    )
    return mon
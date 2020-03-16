from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def training_model(i_nodes, o_nodes):

    model = Sequential()
    model.add(Dense(64, input_dim=i_nodes, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(o_nodes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    return model
from os import environ as env
# Reduce Tensorflow output to console
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.utils import to_categorical as onehotencode
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score
import pandas
import numpy as np
import pickle

def run(model):

    # Load test data and tokenizer
    data = pandas.read_json('demologs.json', lines=True)
    with open('tfidf_tokenizer.pickle', 'rb') as file:
        tokenizer = pickle.load(file)

    # Separate loglevels from messages
    messages = data.MESSAGE
    real_loglevel = data.PRIORITY

    # Convert data to tfidf tokens
    tokenized_msgs = tokenizer.texts_to_matrix(messages, mode='tfidf')

    # Convert the correct answers into one-hot-encoded arrays
    tokenized_answers = onehotencode(real_loglevel)

    # Feed the data into the model
    pred = model.predict(tokenized_msgs)

    # Print the results in a nice format
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

    print("Message, distribution, predicted level, real level")
    for i in range(len(messages)):
        print(messages[i][:30], pred[i],
              np.argmax(pred[i]), real_loglevel[i])

    predictions = np.argmax(pred, axis=1)
    correct_classes = np.argmax(tokenized_answers, axis=1)
    acc = accuracy_score(correct_classes, predictions)
    print("Demoset accuracy: ", round(acc, 4) * 100, "%")
    return

model = load_model('Lokari-v0.2.h5')
run(model)
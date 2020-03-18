from os import environ as env
# Reduce Tensorflow output to console
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from Lokari.nlp import load_tokenizer
from tensorflow.keras.utils import to_categorical as onehotencode
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

def run(model):
    DEMO_FILE = 'demologs.json'

    # Read the demo data
    data = pd.read_json(DEMO_FILE, lines=True)
    messages = data.MESSAGE
    real_loglevel = data.PRIORITY
    # Load tokenizer & convert data to tfidf tokens
    tokenizer = load_tokenizer()
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
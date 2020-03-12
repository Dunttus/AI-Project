# As from Ashu Prasad's blog, with small modifications
# https://towardsdatascience.com/natural-language-processing-with-tensorflow-e0a701ef5cef

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
import pandas as pd

# Testing file
FILE = "ubuntu_logs_tail.json"
LOG_DATA = ['PRIORITY', 'MESSAGE']
#FILE = "../datasets/loglevels/training_logs.json"
df = pd.read_json(FILE, lines=True)
# Testing data needs to be stripped, not needed on big file
df = df[LOG_DATA]

# Bring on the Tokenizer!
tok = Tokenizer(num_words=100, oov_token="<OOV>")
tok.fit_on_texts(df.MESSAGE)
# Here we see some numbers get attention, do we want that?
print(tok.word_index)
print(tok.word_counts)
seq = pad(tok.texts_to_sequences(df.MESSAGE),maxlen=None)
print(seq)

# Hyperparameters
vocab_size = 1000
embedding_dim = 16
max_length = 16
trunc_type='post'
padding_type='post'
oov_tok = '<OOV>'
training_size = 20000

# The model
# Embedding layer needs to be examined closer!
model = keras.Sequential([
    keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    keras.layers.Flatten(),
    keras.layers.Dense(6, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
model.summary()

# tbc...
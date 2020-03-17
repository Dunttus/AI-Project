# This code constructs a reusable word-number encoding corpus
# from log files. IN PROGRESS
import numpy
import json
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad

# Get the words from the big logs:

DATASET_PATH = '../datasets/loglevels/'
DATASET_FILE = 'ubuntu_tail_logs.json'
data = pd.read_json(DATASET_PATH + DATASET_FILE, lines=True)


numpy.set_printoptions(threshold=numpy.inf)
numpy.set_printoptions(linewidth=numpy.inf)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def create_tokenizer(data):
    tok = Tokenizer(num_words=1000,
                    filters='',
                    lower=True,
                    split=' ',
                    char_level=True,
                    oov_token=None,
                    document_count=0)

    tok.fit_on_texts(data)
    seq = pad(tok.texts_to_sequences(data),
             maxlen=256,
             padding='post'
            )
    print(f"Word index: {tok.word_index}")
    print(f"Word count: {tok.word_counts}")
    print(seq)
    return tok

tok = create_tokenizer(data['MESSAGE'])

tokenizer_json = tok.to_json()
# Saving tokenizer
with open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json))

# Loading tokenizer
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizerloaded = tokenizer_from_json(data)

# Use the loaded tokenizer
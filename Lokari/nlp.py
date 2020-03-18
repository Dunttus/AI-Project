# Natural Language Processing functions for Lokari log classifier
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
import pickle

def basic_tokenizer(data):
    tok = Tokenizer(num_words=2000,
                    oov_token="<OOV>")
    tok.fit_on_texts(data)
    seq = pad(tok.texts_to_sequences(data),
              maxlen=64,
              padding='post'
              )
    return seq

def char_tokenizer(data):
    tok = Tokenizer(num_words=256,
                    filters='',
                    lower=False,
                    split='',
                    char_level=True,
                    oov_token=None,
                    document_count=0)

    tok.fit_on_texts(data)
    seq = pad(tok.texts_to_sequences(data),
             maxlen=512,
             padding='post')

    return seq

def tfidf_matrix_tokenizer(data):
    # Best logarithmic loss value with this
    tok = Tokenizer(num_words=6144)
    tok.fit_on_texts(data)
    save_tokenizer(tok)
    mtrx = tok.texts_to_matrix(data, mode='tfidf')

    return mtrx

def save_tokenizer(tokenizer):

    with open('demo_model/tfidf_tokenizer.pickle', 'wb') as file:
        pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)

    return

def load_tokenizer():

    with open('tfidf_tokenizer.pickle', 'rb') as file:
        tokenizer = pickle.load(file)

    return tokenizer
# Do these options really have effect on tfidf?
#char_level=True,
#filters='',
#lower=False)

# Natural Language Processing functions for Lokari log classifier
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad

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
    mtrx = tok.texts_to_matrix(data, mode='tfidf')

    return mtrx

# Do these options really have effect on tfidf?
#char_level=True,
#filters='',
#lower=False)

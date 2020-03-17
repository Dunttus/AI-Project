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
    tok = Tokenizer(num_words=1000,
                    filters='',
                    lower=True,
                    split=' ',
                    char_level=True,
                    oov_token=None,
                    document_count=0)

    tok.fit_on_texts(data)
    seq = pad(tok.texts_to_sequences(data),
             maxlen=512,
             padding='post')

    return seq





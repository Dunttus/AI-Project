# Natural Language Processing functions for Lokari log classifier
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad

def basic_tokenizer(data):
    tok = Tokenizer(num_words=2000, oov_token="<OOV>")
    tok.fit_on_texts(data)
    seq = pad(tok.texts_to_sequences(data), maxlen=100)
    return seq





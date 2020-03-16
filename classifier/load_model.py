# Still testing not fully functional

from tensorflow import keras
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer

# Loading trained model from model_files/lokari_v0.1.h5'
model = keras.models.load_model('model_files/lokari_v0.1.h5')
model.summary()

# Reading test data
DATASET = "./test_data/test_data_to_load.json"
df = pd.read_json(DATASET, lines=True)
print(df)
classes_full = to_categorical(df['PRIORITY'])
print(classes_full)

def log_message_tokenizer():
    # default: filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    tok = Tokenizer(num_words=1000, oov_token="<OOV>")
    tok.fit_on_texts(df.MESSAGE)
    return pad(tok.texts_to_sequences(df.MESSAGE), maxlen=None)

def predicttest():
    log_text_data_full = log_message_tokenizer()
    print(log_text_data_full)
    pred = (classes_full, log_text_data_full)
    print(pred)
    outputs = model.predict(pred)
    print(outputs)

predicttest()
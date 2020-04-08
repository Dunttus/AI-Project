from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical as onehotencode
from tensorflow.keras.layers import Input, Dense, concatenate
from tensorflow.keras.models import Model
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../datasets/apache_access_log/access_log_testing',
                 sep=" ", header=None)
df.columns = ["time", "ip", "status", "byte", "rtime",
              "method", "url", "protocol"]

print(df.dtypes)
print(df)

# Transform the data into ML-model readable format, and making new dataframes.
# These are fed into a dual model, one which processes text, and the other
# deals with numbers and categorical data.
numdata = pd.DataFrame(columns=['status','byte','rtime','method'])
numdata_processed = pd.DataFrame()
textdata = pd.DataFrame()

# time = timestamp OMITTED FOR NOW
# ip = requesting ip address OMITTED FOR NOW
# status = HTTP status code
# convert the status codes to strings for one-hot-encoding to work
numdata['status'] = df['status'].astype(str)
numdata['status'] = pd.Categorical(numdata['status'])
numdata.status = numdata.status.cat.codes
status_ohe = onehotencode(numdata.status)
print(status_ohe)

# TODO: onehotencode creates a numpy array, so combining with pandas dataframe
# TODO: doesn't work out of the box.



#print(testdf.shape)
# byte = size of the requested object
# int64 type not good for model.fit function
numdata['byte'] = df['byte']
# rtime = time taken to serve the request
# int64 not good for model.fit
numdata['rtime'] = df['rtime']
# method
# transform to categorical data? shows as int still
numdata['method'] = pd.Categorical(df['method'])
numdata.method = numdata.method.cat.codes
# url = first line of request

# This is a char-based tokenizer, maxlen is the number of characters used
# num_words=64 -is this enough for all characters in logs? test sample
# has 53 characters...
# HTTP Request body does %<code> with exotic characters %20 = space
tok = Tokenizer(num_words=64, filters='',
                lower=False, split='',char_level=True)
df['url'] = df['url'].astype(str)
tok.fit_on_texts(df['url'])
textdata = pad(tok.texts_to_sequences(df['url']), maxlen=64, padding='post')
#protocol OMITTED FOR NOW

print(numdata.dtypes)
print(numdata)
print("Final numeric data processed:")
print(numdata_processed)
print(textdata)

# https://keras.io/getting-started/functional-api-guide/
# https://keras.io/getting-started/sequential-model-guide/
# https://keras.io/models/model/

# Define 2 different inputs and their sizes
print(f"Numerical feature vector inputs: {numdata.shape[1]}")
print(f"Text tokenizer vector inputs: {textdata.shape[1]}")
num_input = Input(shape=numdata.shape[1], name='num_input')
text_input = Input(shape=textdata.shape[1], name='text_input')

# NLP branch:
first_nlp = Dense(64, activation='relu')(text_input)
second_nlp = Dense(32, activation='relu')(first_nlp)
nlp_output = Dense(8, activation='relu')(second_nlp)

# Combining the branches with concatenate
# Autoencoding layer: 8 + 4 inputs and outputs
# Concatenation is done for 8 layers from nlp_output and 4 from num_input
output = concatenate([num_input, nlp_output])
output = Dense(12, activation='sigmoid')(output)
output = Dense(1, activation='sigmoid')(output)
model = Model(inputs=[num_input, text_input], outputs=[output])

# Check: Loss function! Normalization in the autoencoding phase??
model.compile(optimizer='adam', loss='mean_squared_error', metrics=None,
              loss_weights=None, sample_weight_mode=None,
              weighted_metrics=None, target_tensors=None)

# All options
# y value is the same as input?? Check this in depth
#model.fit(x=[numdata, textdata],
#          y=None,
#          batch_size=None,
#          epochs=10, verbose=1,
#          callbacks=None, validation_split=0.0, validation_data=None,
#          shuffle=True, class_weight=None, sample_weight=None,
#          initial_epoch=0, steps_per_epoch=None, validation_steps=None,
#          validation_freq=1, max_queue_size=10, workers=1,
#          use_multiprocessing=False)
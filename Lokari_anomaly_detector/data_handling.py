from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.layers import Input
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
textdata = pd.DataFrame()

# time = timestamp OMITTED FOR NOW
# ip = requesting ip address OMITTED FOR NOW
# status = HTTP status code
numdata['status'] = pd.Categorical(df['status'])
# byte = size of the requested object
numdata['byte'] = df['byte']
# rtime = time taken to serve the request
numdata['rtime'] = df['rtime']
# method
numdata['method'] = pd.Categorical(df['method'])
numdata.method = numdata.method.cat.codes
# url = first line of request
# This is a char-based tokenizer, maxlen is the number of characters used
# num_words=64 -is this enough for all characters in logs? test sample
# has 53 characters...
tok = Tokenizer(num_words=64, filters='',
                lower=False, split='',char_level=True)
df['url'] = df['url'].astype(str)
tok.fit_on_texts(df['url'])
textdata = pad(tok.texts_to_sequences(df['url']), maxlen=80, padding='post')
#protocol OMITTED FOR NOW

print(numdata.dtypes)
print(numdata)
print(textdata)
print(df)

# Next we are going to put the model together
num_input = Input()
text_input = Input()
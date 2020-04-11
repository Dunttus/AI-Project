from os import environ as env
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
from tensorflow.keras.utils import to_categorical as onehotencode
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../datasets/apache_access_log/access_log_testing',
                 sep=" ", header=None)
df.columns = ["time", "ip", "status", "byte", "rtime",
              "method", "url", "protocol"]

numdata = pd.DataFrame(columns=['status','byte','rtime','method'])
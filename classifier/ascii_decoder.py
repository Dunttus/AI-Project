import pandas as pd

DS_LOC = "../datasets/loglevels/"
FILE = "decode_this.json"

LOG_DATA = ['PRIORITY', 'MESSAGE']

def test_function(x):
    return x

df = pd.read_json(DS_LOC + FILE, lines=True)
df = (df[LOG_DATA])
print(df)
df.MESSAGE = df.MESSAGE.apply(test_function)
print(df)

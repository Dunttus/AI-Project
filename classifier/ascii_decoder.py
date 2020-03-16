import pandas as pd

DS_LOC = "../datasets/loglevels/"
FILE = "decode_this.json"

LOG_DATA = ['PRIORITY', 'MESSAGE']

def datatype_check(data):

    # We want all lines to be of type string
    if isinstance(data, str):
        return data

    else:
        # UTF-8 fails here, invalid continuation byte
        if isinstance(data, list):
            data = bytes(data).decode("latin-1")
            return data

        else:
            print("ERROR: Format could not be converted: ", type(data))
            exit(1)

df = pd.read_json(DS_LOC + FILE, lines=True)
df = (df[LOG_DATA])
df.MESSAGE = df.MESSAGE.apply(datatype_check)

print(df)

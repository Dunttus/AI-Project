from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd

FILE = "ubuntu_logs_tail.json"
df = pd.read_json(FILE, lines=True)

print(df)
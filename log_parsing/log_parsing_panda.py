import pandas as pd
import re

LOG_DATA = ['PRIORITY', 'MESSAGE']
# RegExp for three dots
ENDING_DOTS = re.compile('[.]{1,}$')

pd.set_option('display.max_colwidth', None)

# With a large file, this takes time to execute!
raw_df = pd.read_json("ubuntu_logs_test", lines=True)
df = raw_df[LOG_DATA]
print(df)
word_count = df['MESSAGE'].apply(lambda txt: len(txt.split(' '))).sum()
print(f"Total words in the message data: {word_count}")

# Preprocess text:
# https://en.wikipedia.org/wiki/Stop_words
# Log data can be thought as a language on it's own, so lets not drop stop
# words (most common ones) yet. Looking at the test data, three dots '...'
# can be at least filtered out with regular expression.

def remove_dots(text):
    return ENDING_DOTS.sub('', text)

print("Periods and tbc dots away!")
print(df['MESSAGE'].apply(remove_dots))
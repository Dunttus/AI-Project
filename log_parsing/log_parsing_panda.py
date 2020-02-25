import pandas as pd
import re
from sklearn.model_selection import train_test_split

LOG_DATA = ['PRIORITY', 'MESSAGE']
# RegExp for one or more dots in the end of MESSAGE
ENDING_DOTS = re.compile('[.]{1,}$')

pd.set_option('display.max_colwidth', None)

# With a large file, this takes some time to execute!
raw_df = pd.read_json("ubuntu_logs_test", lines=True)
df = raw_df[LOG_DATA]
print(df)
word_count = df['MESSAGE'].apply(lambda txt: len(txt.split(' '))).sum()

# Preprocess text:
# https://en.wikipedia.org/wiki/Stop_words
# Log data can be thought as a language on it's own, so lets not drop stop
# words (most common ones) yet.

def remove_dots(text):
    return ENDING_DOTS.sub('', text)

# Check the SettingWithCopyWarning, code works though.
print("Periods and tbc dots away!")
df['MESSAGE'] = df['MESSAGE'].apply(remove_dots)
print(df)

print(f"Total words in the message data: {word_count}")
print("Value distribution in 'PRIORITY':")
print(df['PRIORITY'].value_counts(dropna=False))

# Splitting the dataset to training and testing sets
x = df.PRIORITY
y = df.MESSAGE
x_train, x_test, y_train, y_test = train_test_split(x, y)
print("\nPRIORITY training set:")
print(x_train)
print("\nPRIORITY test set:")
print(x_test)
print("\nMESSAGE training set:")
print(y_train)
print("\nMESSAGE test set:")
print(y_test)
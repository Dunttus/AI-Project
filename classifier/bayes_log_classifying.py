import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

LOG_DATA = ['PRIORITY', 'MESSAGE']
# RegExp for one or more dots in the end of MESSAGE
ENDING_DOTS = re.compile('[.]{1,}$')

pd.set_option('display.max_colwidth', None)

# With a large file, this takes some time to execute!
raw_df = pd.read_json("ubuntu_logs_tail.json", lines=True)
df = raw_df[LOG_DATA]
print(df)
word_count = df['MESSAGE'].apply(lambda txt: len(txt.split(' '))).sum()

# Preprocess text:
# https://en.wikipedia.org/wiki/Stop_words
# Log data can be thought as a language on it's own, so lets not drop stop
# words (most common ones) yet.
# Stopword candidates: the, and

def remove_dots(text):
    return ENDING_DOTS.sub('', text)

# Check the SettingWithCopyWarning, code works though.
print("Periods and tbc dots away!")
#df['MESSAGE'] = df['MESSAGE'].apply(remove_dots)
df.MESSAGE = df.MESSAGE.apply(remove_dots)
print(df)

print(f"Total words in the message data: {word_count}")
print("Value distribution in 'PRIORITY':")
print(df['PRIORITY'].value_counts(dropna=False))

# Splitting the dataset to training and testing sets
x = df.PRIORITY
y = df.MESSAGE
x_train, x_test, y_train, y_test = train_test_split(x, y)

# Bag of Words
# https://scikit-learn.org/stable/modules/feature_extraction.html#the-bag-of-words-representation

# Vectorize the data, note that y_train is a random sample from whole y
vec = CountVectorizer()
messages_vectorized = vec.fit_transform(y_train)
print(messages_vectorized.toarray())

# Test tf-idf term weighting
# Term frequency times inverse document-frequency
# https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

tfdif = TfidfTransformer()
messages_tfdf = tfdif.fit_transform(messages_vectorized)
print(messages_tfdf.toarray())

# This classifier might suit for our purposes
# https://scikit-learn.org/stable/modules/naive_bayes.html#categorical-naive-bayes
from sklearn.naive_bayes import CategoricalNB

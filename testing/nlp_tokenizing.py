import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Example code and notes from Ashu Prasad's article:
# https://towardsdatascience.com/natural-language-processing-with-tensorflow-e0a701ef5cef

# This becomes the word corpus (word collection)
text = ['Hello world',
        'Goodbye world',
        'Hi world',
        'Good morning and hello, world']
# Tokenizer hyperparameter: num_words takes 100 most common words in the set
tok = Tokenizer(num_words = 100, oov_token="<OOV>")
tok.fit_on_texts(text)
# Each word corresponds to a number
print(tok.word_index)
# This command prints stats
print(tok.word_counts)
# Next step is to make sequences
seq = tok.texts_to_sequences(text)
print(seq)
# The tok -object is alive! We can pass other stuff for it now:
text2 = ['Hello dear',
         'What a nice morning',
         'I would give a world for a cup of good coffee']
seq2 = tok.texts_to_sequences(text2)
# Now the word collection comes into play: only words from the first set are
# recognized. This is where OOV -tokens come into play (out of vocabulary).
print(seq2)
# We have to pad the sentences to make them of equal length.
seq2 = pad_sequences(seq2)
print(seq2)
# pad_sequences parameters: padding='post' -> padding comes after the sequence
# maxlen=<value> can be used to limit the longest sentence
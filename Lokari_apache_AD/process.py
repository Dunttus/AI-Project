# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
import pandas, numpy
from keras_preprocessing.text import Tokenizer


# TODO: Minimize cardinality (amount of categories) in functions

def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    #print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    processed.status = tokenize_http_status(data.status)
    processed.byte = normalize_response_size(data.byte)
    processed.rtime = normalize_response_time(data.rtime)
    processed.method = tokenize_http_methods(data.method)

    # TODO: separate this to it's own dataframe!
    processed.url = tokenize_url(data.url)

    #print(processed)
    #print(processed.dtypes)
    return processed


def tokenize_http_status(data):

    tokenizer = Tokenizer(num_words=20, filters='')
    tokenizer.fit_on_texts(data.astype(str))
    # save tokenizer here??
    data = tokenizer.texts_to_sequences(data.astype(str))
    data = numpy.array(data)
    return data


def normalize_response_size(size):

    # calculate average size and normalize?

    return size


def normalize_response_time(time):

    # calculate average size and normalize?

    return time


def tokenize_http_methods(data):

    tokenizer = Tokenizer(num_words=6, filters='')
    tokenizer.fit_on_texts(data)
    # save tokenizer here??
    data = tokenizer.texts_to_sequences(data)
    data = numpy.array(data)
    return data


def tokenize_url(data):

    data = pandas.DataFrame()

    # TODO: Check word-level tokenizing, tf-idf is probably better
    # TODO: Check tokenizer settings, is it eg. lowercasing on default?
    tokenizer = Tokenizer(num_words=128, char_level=True)
    tokenizer.fit_on_texts(data)
    data = tokenizer.texts_to_sequences(data)
    data = numpy.array(data)

    # TODO: make a new dataframe!
    # Pad the data later to be of equal length?
    # Keras pad_sequences changes the datatype to numpy.ndarray, which doesn't
    # fit into a pandas column easy.

    # tfidf tokenizer code
    #data = tokenizer.texts_to_matrix(data, mode='tfidf')

    return data

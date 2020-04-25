# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
import numpy
from keras_preprocessing.text import Tokenizer


# TODO: Minimize cardinality (amount of categories) in functions

def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    #print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    processed.status = tokenize_http_status(data.status)
    print(type(processed.status))

    processed.byte = normalize_response_size(data.byte)
    processed.rtime = normalize_response_time(data.rtime)
    processed.method = tokenize_http_methods(data.method)
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

    # TODO: Check word-level tokenizing
    # TODO: Check tokenizer settings, is it eg. lowercasing on default?
    tokenizer = Tokenizer(num_words=128, char_level=True)
    tokenizer.fit_on_texts(data)
    data = tokenizer.texts_to_sequences(data)
    data = numpy.array(data)
    # Pad the data later to be of equal length?
    # Keras pad_sequences changes the datatype to numpy.ndarray, which doesn't
    # fit into a pandas column easy.

    # tfidf piece tokenizer for testing
    #data = tokenizer.texts_to_matrix(data, mode='tfidf')

    return data

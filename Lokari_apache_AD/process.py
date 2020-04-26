# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
import pandas, numpy
from keras_preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad


# TODO: Minimize cardinality (amount of categories) in functions

def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol','url'],)
    #print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    processed.status = tokenize_http_status(data.status)
    processed.byte = normalize_response_size(data.byte)
    processed.rtime = normalize_response_time(data.rtime)
    processed.method = tokenize_http_methods(data.method)

    # Separate url data because it has more than one columns after
    # processing.
    urldata = data.drop(columns=['time', 'ip', 'status', 'byte','rtime',
                             'method', 'protocol'])
    urldata = tokenize_url(urldata.url)

    #print(urldata)
    #print(processed)
    #print(processed.dtypes)
    return processed, urldata


def tokenize_http_status(data):

    tokenizer = Tokenizer(num_words=20, filters='')
    tokenizer.fit_on_texts(data.astype(str))
    # save tokenizer
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
    # save tokenizer
    data = tokenizer.texts_to_sequences(data)
    data = numpy.array(data)
    return data


def tokenize_url(data):

    # TODO: Check word-level tokenizing, tf-idf is probably better
    tokenizer = Tokenizer(num_words=128, filters='', char_level=True,
                          lower=False)
    tokenizer.fit_on_texts(data)
    # save tokenizer
    # TODO: Set padding length to a constant
    data = pad(tokenizer.texts_to_sequences(data))

    # tfidf tokenizer code
    #data = tokenizer.texts_to_matrix(data, mode='tfidf')
    #print(padded)
    return data

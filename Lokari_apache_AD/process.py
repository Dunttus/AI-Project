# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
from keras_preprocessing.text import Tokenizer


def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    processed.status = tokenize_http_status(data.status)
    processed.method = tokenize_http_methods(data.method)

    print(processed)

    return processed


def tokenize_http_status(data):

    tokenizer = Tokenizer(num_words=20, filters='')
    tokenizer.fit_on_texts(data.astype(str))
    # save tokenizer here??
    data = tokenizer.texts_to_sequences(data.astype(str))
    return data


def normalize_response_size(bytes):

    # calculate average size and normalize? zscore?

    return


def normalize_response_time(milliseconds):

    # calculate average size and normalize? zscore?

    return


def tokenize_http_methods(data):

    tokenizer = Tokenizer(num_words=6, filters='')
    tokenizer.fit_on_texts(data)
    # save tokenizer here??
    data = tokenizer.texts_to_sequences(data)
    return data


def tokenize_url():

    # Separate path and query?
    # load tokenizer
    # process

    return
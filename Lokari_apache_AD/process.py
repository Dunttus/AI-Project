# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
from keras_preprocessing.text import Tokenizer


def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    processed.method = tokenize_http_methods(data.method)
    print(processed)

    return processed


def tokenize_http_status():

    # load tokenizer
    # process

    return


def normalize_response_size(bytes):

    # calculate average size and normalize? zscore?

    return


def normalize_response_time(milliseconds):

    # calculate average size and normalize? zscore?

    return


def tokenize_http_methods(data):

    #print(data)
    http_status_tokenizer = Tokenizer(num_words=6, filters='')
    http_status_tokenizer.fit_on_texts(data)
    # save tokenizer here??

    catdata = http_status_tokenizer.texts_to_sequences(data)
    return catdata


def tokenize_url():

    # Separate path and query?
    # load tokenizer
    # process

    return
# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences as pad


def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    processed.status = tokenize_http_status(data.status)
    processed.byte = normalize_response_size(data.byte)
    processed.rtime = normalize_response_time(data.rtime)
    processed.method = tokenize_http_methods(data.method)
    processed.url = tokenize_url(data.url)
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

    return bytes


def normalize_response_time(time):

    # calculate average size and normalize? zscore?

    return time


def tokenize_http_methods(data):

    tokenizer = Tokenizer(num_words=6, filters='')
    tokenizer.fit_on_texts(data)
    # save tokenizer here??
    data = tokenizer.texts_to_sequences(data)
    return data


def tokenize_url(data):

    tokenizer = Tokenizer(num_words=128, char_level=True)
    tokenizer.fit_on_texts(data)

    print(type(data))
    # This doesn't work correctly yet. Have to put the whole sequence
    # in to the url column.
    data = pad(tokenizer.texts_to_sequences(data), maxlen=64,
                   padding='post')
    #textdata2 = tokenizer.texts_to_matrix(data, mode='tfidf')

    return data
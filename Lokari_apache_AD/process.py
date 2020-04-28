# Convert the log data into fully numerical presentation.
# If the model is being trained, save all tokenizers used.
import pickle
import pandas, numpy
from keras_preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
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
    save_tokenizer_status(tokenizer)
    data = tokenizer.texts_to_sequences(data.astype(str))
    data = numpy.array(data)
    return data


def normalize_response_size(data):

    # Average size of a response
    mean = data.mean()
    # Standard deviation in response size values
    std = data.std()
    # Zscore = Normalized deviation, values <-2 and 2< present 5% confidence
    data = (data - mean) / std

    return data


def normalize_response_time(data):

    # Average time of a response
    mean = data.mean()
    # Standard deviation in response time values
    std = data.std()
    # Zscore = Normalized deviation, values <-2 and 2< present 5% confidence
    data = (data - mean) / std

    return data


def tokenize_http_methods(data):

    tokenizer = Tokenizer(num_words=6, filters='')
    tokenizer.fit_on_texts(data)
    save_tokenizer_method(tokenizer)
    data = tokenizer.texts_to_sequences(data)
    data = numpy.array(data)
    return data


def tokenize_url(data):

    # TODO: Check word-level tokenizing, tf-idf is probably better
    tokenizer = Tokenizer(num_words=128, filters='', char_level=True,
                          lower=False)
    tokenizer.fit_on_texts(data)
    save_tokenizer_url(tokenizer)
    # TODO: Set padding length to a constant
    data = pad(tokenizer.texts_to_sequences(data))

    # tfidf tokenizer code
    #data = tokenizer.texts_to_matrix(data, mode='tfidf')
    #print(padded)
    return data


def save_tokenizer_status(tokenizer):

    with open('saved_models/model_name_and_version/status.pickle', 'wb') as file:
        pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)

    return


def save_tokenizer_method(tokenizer):

    with open('saved_models/model_name_and_version/method.pickle', 'wb') as file:
        pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)

    return


def save_tokenizer_url(tokenizer):

    with open('saved_models/model_name_and_version/url.pickle', 'wb') as file:
        pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)

    return

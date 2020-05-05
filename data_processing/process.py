# Convert the log data into fully numerical presentation.
import pickle, numpy
from os import mkdir
from keras_preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences as pad
import config as config


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

    if config.SAVE:
        tokenizer = Tokenizer(num_words=20, filters='', oov_token=0)
        tokenizer.fit_on_texts(data.astype(str))
        save_tokenizer(tokenizer, "status")

    if not config.SAVE:
        tokenizer = load_tokenizer("status")

    data = tokenizer.texts_to_sequences(data.astype(str))
    data = numpy.array(data)
    return data


def normalize_response_size(data):

    # IDEA: These could be categorized as well? At least static pages give
    # consistent response sizes. Dataset can be examined with
    # data.value_counts()

    if config.SAVE:
        # Average size of a response
        mean = data.mean()
        # Standard deviation in response size values
        std = data.std()
        save_numbers(mean, std, "size")

        # Zscore = Normalized deviation, values <-2 and 2< present 5% confidence
        # How many standard deviations from the mean?

    if not config.SAVE:
        mean, std = load_numbers("size")

    # Zscore = Normalized deviation, values <-2 and 2< present 5% confidence
    # How many standard deviations from the mean?
    data = (data - mean) / std

    return data


def normalize_response_time(data):

    if config.SAVE:
        # Average time of a response
        mean = data.mean()
        # Standard deviation in response time values
        std = data.std()
        save_numbers(mean, std, "rtime")

    if not config.SAVE:
        mean, std = load_numbers("rtime")

    data = (data - mean) / std

    return data


def tokenize_http_methods(data):

    # num_words has to contain all the categories, otherwise numpy.array
    # doesn't work.
    # TODO: test one-hot-encoding
    if config.SAVE:
        tokenizer = Tokenizer(num_words=10, filters='')
        tokenizer.fit_on_texts(data)
        save_tokenizer(tokenizer, "method")

    if not config.SAVE:
        tokenizer = load_tokenizer("method")

    data = tokenizer.texts_to_sequences(data)
    data = numpy.array(data)
    return data


def tokenize_url(data):

    if config.SAVE:
        tokenizer = Tokenizer(num_words=128, filters='', char_level=True,
                              lower=False)
        tokenizer.fit_on_texts(data)
        save_tokenizer(tokenizer, "url")

    if not config.SAVE:
        tokenizer = load_tokenizer("url")

    # We have maximum of 64 character long requests.
    data = pad(tokenizer.texts_to_sequences(data),
               maxlen=64,
               padding='post')

    # TODO: Test word-level tokenizer
    # TODO: Test tfidf tokenizing
    # tfidf tokenizer code
    #data = tokenizer.texts_to_matrix(data, mode='tfidf')
    #print(padded)
    return data


def save_tokenizer(tokenizer, name):

    try:
        mkdir('saved_models/' + config.VERSION)

    except FileExistsError:
        print('Tokenizer ' + name + ' exists for this version, overwriting...')

    filename = 'saved_models/' + config.VERSION + '/' + name + '.pickle'

    with open(filename, 'wb') as file:
        pickle.dump(tokenizer, file, protocol=pickle.HIGHEST_PROTOCOL)

    return


def save_numbers(mean, std, name):

    filename = 'saved_models/' + config.VERSION + '/' + name + '.txt'
    data = str(mean) + "\n" + str(std) + "\n"

    with open(filename, 'w') as file:
        file.write(data)

    return


def load_tokenizer(name):

    filename = 'saved_models/' + config.VERSION + '/' + name + '.pickle'
    with open(filename, 'rb') as file:
        tokenizer = pickle.load(file)

    return tokenizer


def load_numbers(name):

    filename = 'saved_models/' + config.VERSION + '/' + name + '.txt'
    with open(filename, 'r') as file:
        mean = file.readline()
        std = file.readline()

    mean = float(mean)
    std = float(std)

    return mean, std

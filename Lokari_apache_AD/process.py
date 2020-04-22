# These functions are for training at the moment

def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    # Tokenizers have to be created before processing

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


def tokenize_http_methods():

    # This is the way to categorize methods
    # Check otuput format
    tokenizer = Tokenizer(num_words=4, filters='')
    tokenizer.fit_on_texts(df['method'])
    catdata = tokenizer.texts_to_sequences(df.method)
    print(catdata)
    # load tokenizer
    # process

    return


def tokenize_url():

    # Separate path and query?
    # load tokenizer
    # process

    return
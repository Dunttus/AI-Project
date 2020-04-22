def process_apache_log(data):

    # ["time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # We are dropping some for now
    processed = data.drop(columns=['time','ip','protocol'])
    print(processed.columns)
    # ['status', 'byte', 'rtime', 'method', 'url']

    return processed



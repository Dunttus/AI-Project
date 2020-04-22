import pandas


def read(target):

    # TODO: Check how this works with a single line coming from the monitor
    dataframe = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None)
    dataframe.columns = [
        "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]

    return dataframe

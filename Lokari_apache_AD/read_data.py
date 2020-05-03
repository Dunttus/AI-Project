import pandas


def read(target):

    dataframe = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None)
    dataframe.columns = [
        "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]

    return dataframe


def readlines(target):

    # Returns an iterator with chunksize
    iterator = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None,
        chunksize=1)

    return iterator

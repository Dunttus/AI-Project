import pandas
import io
import config

def read(target):

    dataframe = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None)

    # If the log is not in correct format, the next line fails
    try:
        dataframe.columns = [
            "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]

    # We assume default log format
    except ValueError:
        config.DEFAULT_FLAG = True
        print("Error: Not the custom log format with rtime")
        print("Trying to parse default apache/nginx log format...")

        dataframe = parsedefault(target)

    return dataframe


def readlines(target):

    # We have to know here what format the data is to process it for
    # the check_training_data function. Simple flag is used.
    # The flag is set if an exception in read_data.read triggers
    if config.DEFAULT_FLAG:
        iterator = pandas.read_csv(target, sep=' ', header=None, chunksize=1)
        return iterator

    # Returns an iterator with chunksize
    iterator = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None,
        chunksize=1)

    return iterator


def put_columns(dataframe):

    if config.DEFAULT_FLAG:

        dataframe.columns = ["ip", "user", "authuser", "time", "tz",
                             "method+request+protocol", "status", "byte",
                             "unknown",
                             "agent"]

        # Split method+request+protocol
        mrpframe = dataframe["method+request+protocol"]
        splitted = mrpframe.str.split(pat=" ", expand=True)
        splitted.columns = ["method", "url", "protocol"]
        dataframe = dataframe.join(splitted)

        # Drop the extras
        dataframe = dataframe.drop(columns=["user", "authuser", "tz",
                                            "method+request+protocol",
                                            "unknown", "agent"])

        # Add a dummy 'rtime' column
        dataframe['rtime'] = 1

        return dataframe

    dataframe.columns = [
        "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]

    return dataframe


def put_final_columns(dataframe):

    dataframe.columns = [
        "status", "byte", "rtime", "method", "url"]

    return dataframe


def read_text(text):

    stream = io.StringIO(text)

    if config.DEFAULT_FLAG:
        df = pandas.read_csv(stream, sep=' ', header=None)
        dataframe = put_columns(df)
        return dataframe

    dataframe = pandas.read_csv(
        stream, sep=' ', quotechar='"', escapechar=' ', header=None)
    put_columns(dataframe)

    return dataframe


def parsedefault(target):

    dataframe = pandas.read_csv(target, sep=' ', header=None)
    dataframe.columns = ["ip", "user", "authuser", "time", "tz",
                         "method+request+protocol", "status", "byte", "unknown",
                         "agent"]

    # Split method+request+protocol
    mrpframe = dataframe["method+request+protocol"]
    splitted = mrpframe.str.split(pat=" ",expand=True)
    splitted.columns = ["method", "url", "protocol"]
    dataframe = dataframe.join(splitted)

    # Drop the extras
    dataframe = dataframe.drop(columns=["user", "authuser", "tz",
                                        "method+request+protocol",
                                        "unknown", "agent"])

    # Add a dummy 'rtime' column
    dataframe['rtime'] = 1

    return dataframe




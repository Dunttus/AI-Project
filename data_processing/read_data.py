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
        # If this is null, return a dummy as str.split fails if there is no
        # string to split
        if mrpframe.hasnans:
            mrpframe.loc[1] = "dummy"

        splitted = mrpframe.str.split(pat=" ",expand=True)
        splitted = splitted.iloc[:, 0:3]

        # Bad lines have only one or 2 elements here...
        # Get number of columns:
        if len(splitted.columns) == 1:
            splitted.columns = ["method"]
            splitted["url"] = "-"
            splitted["protocol"] = "-"

        if len(splitted.columns) == 2:
            splitted.columns = ["method", "url"]
            splitted["protocol"] = "-"

        if len(splitted.columns) == 3:
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
                         "methodrequestprotocol", "status", "byte", "unknown",
                         "agent"]

    # Split method+request+protocol
    mrpframe = dataframe["methodrequestprotocol"]
    splitted = mrpframe.str.split(pat=" ",expand=True)
    # This is where the default format varies
    # Drop the extra columns that might appear
    splitted = splitted.iloc[:,0:3]
    splitted.columns = ["method", "url", "protocol"]
    # So far so good, now we just drop the bad apples
    splitted = splitted.dropna()
    dataframe = dataframe.join(splitted)

    # Drop the extras
    dataframe = dataframe.drop(columns=["user", "authuser", "tz",
                                        "methodrequestprotocol",
                                        "unknown", "agent"])
    # Drop na values again...
    dataframe = dataframe.dropna()
    # Add a dummy 'rtime' column
    dataframe['rtime'] = 1

    return dataframe




import pandas
import io


def read(target):

    dataframe = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None)

    # If the log is not in correct format, the next line fails
    try:
        dataframe.columns = [
            "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]

    # We assume default log format
    except ValueError:
        print("Error: Not the custom log format with rtime")
        print("Trying to parse default apache/nginx log format...")

        dataframe = parsedefault(target)

    return dataframe


def readlines(target):

    # Returns an iterator with chunksize
    iterator = pandas.read_csv(
        target, sep=' ', quotechar='"', escapechar=' ', header=None,
        chunksize=1)

    return iterator


def put_columns(dataframe):

    dataframe.columns = [
        "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]

    return dataframe


def put_final_columns(dataframe):

    dataframe.columns = [
        "status", "byte", "rtime", "method", "url"]

    return dataframe


def read_text(text):

    stream = io.StringIO(text)
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

    # Addd a dummy 'rtime' column
    dataframe['rtime'] = 0

    return dataframe

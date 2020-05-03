# Lokari Apache log anomaly detector:
# Set up a generator function to get new lines in a file
from time import sleep


def follow(target):

    # Set the file object position to end
    target.seek(0, 2)

    while True:
        line = target.readline()
        if not line:
            sleep(0.1)
            continue
        yield line

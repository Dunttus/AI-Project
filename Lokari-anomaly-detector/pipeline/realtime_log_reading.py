# Using python generators to read a new line in a file
from time import sleep


def follow(file):

    # Set the file object position to end
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            sleep(1)
            continue
        yield line


with open('testfile', 'r') as file:

    # In case of an anomaly, we have to be able to give user a heads up,
    # along with the log line that caused it! Maybe related lines too?

    for new_line in follow(file):
        print(new_line, end='')





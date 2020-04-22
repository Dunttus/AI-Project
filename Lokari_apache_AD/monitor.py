# Lokari Apache log anomaly detector:
# Set up a generator function to get new lines in a file

from time import sleep

FILE = 'testing_files/access.log'


def follow(target):

    # Set the file object position to end
    target.seek(0, 2)
    while True:
        line = target.readline()
        if not line:
            sleep(1)
            continue
        yield line


with open(FILE, 'r') as file:

    # In case of an anomaly, we have to be able to give user a heads up,
    # along with the log line that caused it! Maybe related lines too?

    for new_line in follow(file):
        # 1. read_data
        # 2. process
        # 3. compare
        # 4. report result
        print(new_line, end='')





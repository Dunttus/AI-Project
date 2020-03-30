# Using python generators to read a new line in a file


def follow(file):

    # Set the file object position to end
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            # sleep a bit? this is quite resource intensive atm
            continue

        yield line


with open('testfile', 'r') as file:

    for new_line in follow(file):
        print(new_line, end='')



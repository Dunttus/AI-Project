def datatype_check(data):

    # We want all lines to be of type string
    if isinstance(data, str):
        return data

    else:
        # UTF-8 fails here, invalid continuation byte
        if isinstance(data, list):
            data = bytes(data).decode("latin-1")
            return data

        if data is None:
            data = ""
            return data

        else:
            print("ERROR: Format could not be converted: ", type(data))
            print(data)
            exit(1)


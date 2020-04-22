import pandas, numpy


def pandas_output_options():
    # Run the function to display all rows & columns in pandas dataframes
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)


def numpy_output_options():
    # Disable scientific notation in decimal values
    numpy.set_printoptions(suppress=True)
    # Show everything please
    numpy.set_printoptions(threshold=numpy.inf)
    numpy.set_printoptions(linewidth=numpy.inf)
    numpy.set_printoptions(precision=5)


def set_output():
    pandas_output_options()
    numpy_output_options()
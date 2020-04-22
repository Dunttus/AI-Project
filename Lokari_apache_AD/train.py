# Lokari Apache log anomaly detector:
# Train the baseline model
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
import numpy, pandas

# Set output options for pandas and numpy
set_output()

# Read training data
# read_data.py is given the file
# read_data.py returns pandas dataframe
data = read('training_dataset/good_access.log')

# Process training data
# the dataframe is sliced and processed into numbers
print(data)


# Train the model
# neural network is trained to learn an average presentation of usual data


# Save the model
# the model is saved to a file to use with the monitor.py



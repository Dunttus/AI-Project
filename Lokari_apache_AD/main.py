# The main function to start monitor and use the trained model

# In testing: testing with handcrafted bad_access.log

# Lokari Apache log anomaly detector:
# Train the baseline model
from os import environ as env
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
import Lokari_apache_AD.config as config

print("Lokari anomaly detector version: " + config.VERSION)

# This works across the modules
config.SAVE = False

# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Read training data
data = read('training_dataset/good_access.log')

# Process training data
# Returns: ['status', 'byte', 'rtime', 'method'] and tokenized url text as
# numpy array.
data, urldata = process_apache_log(data)



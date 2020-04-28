# Lokari Apache log anomaly detector:
# Train the baseline model
from os import environ as env
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
from Lokari_apache_AD.autoencoder.model import construct_model
import Lokari_apache_AD.config as config

print(config.VERSION)

# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Read training data
data = read('training_dataset/combine_access.log')

# Process training data
# Returns: ['status', 'byte', 'rtime', 'method'] and tokenized url text as
# numpy array.
data, urldata = process_apache_log(data)

# Construct, train and save the model
#model = construct_model(data, urldata)

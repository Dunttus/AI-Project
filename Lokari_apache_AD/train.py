# Lokari Apache log anomaly detector:
# Train the baseline model
from os import environ as env
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
from Lokari_apache_AD.model.construct import construct_model
from Lokari_apache_AD.rmsdcalc import rmsd_calc
from Lokari_apache_AD.checks import check_training_data
import Lokari_apache_AD.config as config

print("Lokari anomaly detector: training version: " + config.VERSION)
config.SAVE = True

# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Read training data
data = read(config.TRAINING_DATA)

# Process training data
# Returns: ['status', 'byte', 'rtime', 'method'] and tokenized url text as
# numpy array.
data, urldata = process_apache_log(data)

# Construct, train and save the model
model = construct_model(data, urldata)

# Calculate and save the baseline MSE score for the trained model
baseline_score = rmsd_calc(data, urldata, model)

# Find anomalies from the training data
check_training_data(model)

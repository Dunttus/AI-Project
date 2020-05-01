# The main function to start monitor and use the trained model

# In testing: testing with handcrafted bad_access.log

# Lokari Apache log anomaly detector:
# Train the baseline model
from os import environ as env
import numpy, pandas
from tensorflow.keras.models import load_model
from sklearn import metrics
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
import Lokari_apache_AD.config as config

# This works across the modules: overrides config.py parameters
# When loading a model, these 2 are the only relevant parameters
config.VERSION = "0.32-1"
config.SAVE = False

print("Lokari anomaly detector version: " + config.VERSION)
# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load model
model_file = 'saved_models/' + config.VERSION + \
             '/Lokari-v' + config.VERSION + '.h5'
model = load_model(model_file)

# Test with a single line, status code only
sampledata = read('training_dataset/single.log')

# Process new log lines

data, url = process_apache_log(sampledata)
test = [data.status, data.byte, data.rtime,
        data.method, url]
sample = model.predict(test)
p_status = sample[0]
p_status = pandas.DataFrame(p_status)
t_status = test[0]

status_score = numpy.sqrt(metrics.mean_squared_error(p_status,t_status))
print("Status MSE:", status_score)

p_byte = sample[1]
p_byte = pandas.DataFrame(p_byte)
t_byte = test[1]
byte_score = numpy.sqrt(metrics.mean_squared_error(p_byte,t_byte))
print("Byte MSE:", byte_score)

p_rtime = sample[2]
p_rtime = pandas.DataFrame(p_rtime)
t_rtime = test[2]
rtime_score = numpy.sqrt(metrics.mean_squared_error(p_rtime,t_rtime))
print("Rtime MSE:", rtime_score)

p_method = sample[2]
p_method = pandas.DataFrame(p_method)
t_method = test[2]
method_score = numpy.sqrt(metrics.mean_squared_error(p_method,t_method))
print("Method MSE:", method_score)

# Take the pre-trained autoencoder
# Use it to make predictions (i.e., reconstruct the digits in our dataset)
# Measure the MSE between the original input and reconstructions
# Compute quantiles for the MSEs, and use these quantiles to identify outliers
# and anomalies

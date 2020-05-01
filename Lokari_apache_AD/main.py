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
from Lokari_apache_AD.msecalc import msescore
import Lokari_apache_AD.config as config

# This works across the modules: overrides config.py parameters
# When loading a model, these 2 are the only relevant parameters
config.VERSION = "0.32-combined"
config.SAVE = False

print("Lokari anomaly detector version: " + config.VERSION)
# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load model
model_file = 'saved_models/' + config.VERSION + \
             '/Lokari-v' + config.VERSION + '.h5'
model = load_model(model_file)

# We need to know the baseline error scores to be able to compare them
# with new incoming data. This part needs to be run only once.

# TODO: make a function to calculate MSEs from the data
# TODO: make sense of url MSE
# NOTE: url MSE might not be needed for basic functionality, as URL data
# affects the inputs, outputs and the training process anyway. Test it.
# NOTE: the original dataset is needed here!
# TODO: This could be done in the training process!

# The data that is fed to the model, can be multi-line
sampledata = read('training_dataset/bad_access.log')
# Process new log lines
data, url = process_apache_log(sampledata)
# The data that has not been through autoencoder yet
test = [data.status, data.byte, data.rtime,
        data.method, url]
# Run the incoming data through autoencoder
sample = model.predict(test)

# Calculate error scores for before autoencoding and
# after autoencoding.
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

p_method = sample[3]
p_method = pandas.DataFrame(p_method)
t_method = test[3]
method_score = numpy.sqrt(metrics.mean_squared_error(p_method,t_method))
print("Method MSE:", method_score)

# Take the pre-trained autoencoder
# Use it to make predictions (i.e., reconstruct the digits in our dataset)
# Measure the MSE between the original input and reconstructions
# Compute quantiles for the MSEs, and use these quantiles to identify outliers
# and anomalies

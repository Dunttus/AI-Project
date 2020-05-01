# The main function to start monitor and use the trained model
# Lokari Apache log anomaly detector:
from os import environ as env
from tensorflow.keras.models import load_model
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
# NOTE: the original dataset is needed here!
# TODO: This really should be done in the training process!

model_data = read('training_dataset/combine_access.log')
m_data, m_url = process_apache_log(model_data)
m_before_ae = [m_data.status, m_data.byte, m_data.rtime,
               m_data.method, m_url]
m_after_ae = model.predict(m_before_ae)
print("Model Status MSE:", msescore(m_after_ae[0], m_before_ae[0]))
print("Model Byte MSE:", msescore(m_after_ae[1], m_before_ae[1]))
print("Model Rtime MSE:", msescore(m_after_ae[2], m_before_ae[2]))
print("Model Method MSE:", msescore(m_after_ae[3], m_before_ae[3]))

# The data that is fed to the model, can be multi-line
incoming_data = read('training_dataset/bad_single.log')
# Process new log line(s)
data, url = process_apache_log(incoming_data)
# The data that has not been through autoencoder yet
before_ae = [data.status, data.byte, data.rtime,
             data.method, url]
# Run the incoming data through autoencoder
after_ae = model.predict(before_ae)

# Calculate error scores for before autoencoding and
# after autoencoding.

print("Status MSE:", msescore(after_ae[0], before_ae[0]))
print("Byte MSE:", msescore(after_ae[1], before_ae[1]))
print("Rtime MSE:", msescore(after_ae[2], before_ae[2]))
print("Method MSE:", msescore(after_ae[3], before_ae[3]))
# TODO: make sense of url MSE

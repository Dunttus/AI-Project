# The main function to start monitor and use the trained model

# In testing: testing with handcrafted bad_access.log

# Lokari Apache log anomaly detector:
# Train the baseline model
from os import environ as env
from tensorflow.keras.models import load_model
from Lokari_apache_AD.read_data import read
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
import Lokari_apache_AD.config as config

print("Lokari anomaly detector version: " + config.VERSION)

# This works across the modules: overrides config.py parameters
# When loading a model, these 2 are the only relevant parameters
config.VERSION = "0.31"
config.SAVE = False

# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Read data
data = read('training_dataset/bad_access.log')

# Load model
model_file = 'saved_models/' + config.VERSION + \
             '/Lokari-v' + config.VERSION + '.h5'
model = load_model(model_file)

# Process new log lines
data, urldata = process_apache_log(data)

# Predict!
print(data, urldata)
#model.predict(data, urldata)
# The input numbers have to be like in the training process:
# Error when checking model input: the list of Numpy arrays that you are passing
# to your model is not the size the model expected. Expected to see 5 array(s),
# for inputs ['status_input', 'bytes_input', 'rtime_input', 'method_input',
# 'url_input'] but instead got the following list of 1 arrays:
# [array([[list([2]), 5.314763282542259, -23.88064518697932, 1],
# [list([2]), 2.199473587826113, -22.899680407606645, 2],
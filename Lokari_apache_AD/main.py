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

# This works across the modules: overrides config.py parameters
# When loading a model, these 2 are the only relevant parameters
config.VERSION = "0.32-1"
config.SAVE = False

print("Lokari anomaly detector version: " + config.VERSION)
# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Read data
data = read('training_dataset/single.log')

# Load model
model_file = 'saved_models/' + config.VERSION + \
             '/Lokari-v' + config.VERSION + '.h5'
model = load_model(model_file)

# Process new log lines
data, urldata = process_apache_log(data)
input_list = [data.status, data.byte, data.rtime, data.method, urldata]

# Predict!
#print(input_list)
output = model.predict(input_list)

#print("Mean squared errors of the prediction:")
print("Status:", output[0][0][0])
print("Response bytes:", output[1][0][0])
print("Response time error:", output[2][0][0])
print("Method error:", output[3][0][0])
print("Url error vector:")
for i in range(64):
    print(output[4][0][i])

# Now make some sense from that output...

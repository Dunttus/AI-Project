# The main function to start monitor and use the trained model
# Lokari Apache log anomaly detector:
from os import environ as env
from tensorflow.keras.models import load_model
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.rmsdcalc import load_baseline_scores
import Lokari_apache_AD.config as config

# This works across the modules: overrides config.py parameters
# When loading a model, these 2 are the only relevant parameters
config.VERSION = "test"
config.SAVE = False
print("Lokari anomaly detector version: " + config.VERSION)

# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load model
model_file = 'saved_models/' + config.VERSION + \
             '/Lokari-v' + config.VERSION + '.h5'
model = load_model(model_file)

# Load the baseline model scores
model_scores = load_baseline_scores()
m_status_score = model_scores[0]
m_byte_score = model_scores[1]
m_rtime_score = model_scores[2]
m_method_score = model_scores[3]
m_url_score = model_scores[4]

# This is where the monitoring loop should start!


# The main function to start monitor and use the trained model
# Lokari Apache log anomaly detector:
from os import environ as env
from tensorflow.keras.models import load_model
from Lokari_apache_AD.read_data import readlines
from Lokari_apache_AD.output_opts import set_output
from Lokari_apache_AD.process import process_apache_log
from Lokari_apache_AD.msecalc import msescore, load_baseline_scores
import Lokari_apache_AD.config as config
import matplotlib.pyplot as plt

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
# The data that is fed to the model
FILENAME = 'training_dataset/good_access.log'

incoming_data = readlines(FILENAME)
line_number = 1
statustest = []

for line in incoming_data:

    line.columns = [
        "time", "ip", "status", "byte", "rtime", "method", "url", "protocol"]
    # Process new log line(s)
    data, url = process_apache_log(line)
    # The data that has not been through autoencoder yet
    before_ae = [data.status, data.byte, data.rtime,
                 data.method, url]
    # Run the incoming data through autoencoder
    after_ae = model.predict(before_ae)

    # Calculate error scores
    status_score = msescore(after_ae[0], before_ae[0])
    byte_score = msescore(after_ae[1], before_ae[1])
    rtime_score = msescore(after_ae[2], before_ae[2])
    method_score = msescore(after_ae[3], before_ae[3])
    url_score = msescore(after_ae[4], url)

    #print("***INCOMING DATA ERROR NUMBERS***")
    #print("Status MSE:", status_score)
    #print("Byte MSE:", byte_score)
    #print("Rtime MSE:", rtime_score)
    #print("Method MSE:", method_score)
    #print("URL MSE:", url_score)

    # Compare the error scores: if the MSEs on incoming data are higher, the
    # probability of an anomaly is higher.

    d_status_score = status_score - m_status_score
    d_byte_score = byte_score - m_byte_score
    d_rtime_score = rtime_score - m_rtime_score
    d_method_score = method_score - m_method_score
    d_url_score = url_score - m_url_score

    #print("***DIFFERENCE - POSITIVE IS TOWARDS ANOMALY***")
    #print("Status MSE:", d_status_score)
    #print("Byte MSE:", d_byte_score)
    #print("Rtime MSE:", d_rtime_score)
    #print("Method MSE:", d_method_score)
    #print("URL MSE:", d_url_score)

    statustest.append([d_status_score,
                       d_byte_score,
                       d_rtime_score,
                       d_method_score,
                       d_url_score])

    if d_status_score > 0:
        print(f"Anomaly in status: Line {line_number}, score: {d_status_score}")

    if d_byte_score > 0:
        print(f"Anomaly in byte: Line {line_number}, score: {d_byte_score}")

    if d_rtime_score > 0:
        print(f"Anomaly in rtime: Line {line_number}, score: {d_rtime_score}")

    if d_method_score > 0:
        print(f"Anomaly in method: Line {line_number}, score: {d_method_score}")

    if d_url_score > 0:
        print(f"Anomaly in url: Line {line_number}, score: {d_url_score}")

    line_number += 1


# Save the results
plt.plot(statustest)
plot_file = 'saved_models/' + config.VERSION + \
            '/validation_plot-' + config.VERSION + '.png'
plt.savefig(plot_file)

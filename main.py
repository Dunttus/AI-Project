# The main function to start monitor and use the trained model
# Lokari Apache log anomaly detector:
from os import environ as env
from tensorflow.keras.models import load_model
from data_processing.output_opts import set_output
from data_processing.process import process_apache_log
from data_processing.rmsdcalc import load_baseline_scores, rmsdscore
from data_processing.read_data import read_text
import config as config
from time import sleep


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


# Monitoring function (generator)
def follow(target):

    # Set the file object position to end
    target.seek(0, 2)

    while True:
        line = target.readline()
        if not line:
            sleep(0.1)
            continue
        yield line


# Start monitoring a file
with open(config.MONITORED_LOG, 'r') as file:

    print(f"Started monitoring: {config.MONITORED_LOG}")
    for new_line in follow(file):

        try:
            dataframe = read_text(new_line)

        except:
            print("Could not process line:")
            print(new_line)
            continue

        data, url = process_apache_log(dataframe)

        before_ae = [data.status, data.byte, data.rtime, data.method, url]
        after_ae = model.predict(before_ae)

        status_score = rmsdscore(after_ae[0], before_ae[0])
        byte_score = rmsdscore(after_ae[1], before_ae[1])
        rtime_score = rmsdscore(after_ae[2], before_ae[2])
        method_score = rmsdscore(after_ae[3], before_ae[3])
        url_score = rmsdscore(after_ae[4], url)

        d_status_score = status_score - m_status_score
        d_byte_score = byte_score - m_byte_score
        d_rtime_score = rtime_score - m_rtime_score
        d_method_score = method_score - m_method_score
        d_url_score = url_score - m_url_score

        if d_status_score > config.RMSD_THRESHOLD:
            print(f"Hit in status: {d_status_score}")

        if d_byte_score > config.RMSD_THRESHOLD:
            print(f"Hit in byte: {d_byte_score}")

        if d_rtime_score > config.RMSD_THRESHOLD:
            print(f"Hit in rtime: {d_rtime_score}")

        if d_method_score > config.RMSD_THRESHOLD:
            print(f"Hit in method: {d_method_score}")

        if d_url_score > config.RMSD_THRESHOLD:
            print(f"Hit in url: {d_url_score}")

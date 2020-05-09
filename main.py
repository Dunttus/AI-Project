# The main function to start monitor and use the trained model
# Lokari Apache log anomaly detector:
from os import environ as env
from tensorflow.keras.models import load_model
from data_processing.output_opts import set_output
from data_processing.read_data import read_text
from data_processing.evaluate import evaluate_log_line
import config as config
from time import sleep


# This works across the modules: overrides config.py parameters
# When loading a model, these 2 are the only relevant parameters
config.SAVE = False
print("Lokari anomaly detector version: " + config.VERSION)

# Set output options for pandas and numpy, minimize TensorFlow output
set_output()
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load model
model_file = 'saved_models/' + config.VERSION + \
             '/Lokari-v' + config.VERSION + '.h5'
model = load_model(model_file)


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

        scores = evaluate_log_line(dataframe, model)
        anomaly = False
        reason = ""
        if scores[0] > config.RMSD_STATUS:
            reason += " status: " + str(round(scores[0], 3))
            anomaly = True

        if scores[1] > config.RMSD_BYTE:
            reason += " byte: " + str(round(scores[1], 3))
            anomaly = True

        if scores[2] > config.RMSD_RTIME:
            reason += " rtime: " + str(round(scores[2], 3))
            anomaly = True

        if scores[3] > config.RMSD_METHOD:
            reason += " method: " + str(round(scores[3], 3))
            anomaly = True

        if scores[4] > config.RMSD_URL:
            reason += " url: " + str(round(scores[4], 3))
            anomaly = True

        if anomaly:
            print("HIT", reason)
            print(new_line)
        # TODO: Write anomalies to a file

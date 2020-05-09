# This code runs the training data against the newly trained model
import config
from data_processing.read_data import readlines, put_columns
from data_processing.evaluate import evaluate_log_line
from data_processing.plots import draw_anomaly_check, draw_anomaly_check_log


def check_training_data(model):

    # This has to be for process_apache_log not to overwrite tokenizers!
    config.SAVE = False

    training_data = []
    log_lines = []

    print("Checking training data for anomalies.")
    print("With big training set, this might take a while")

    print("\nLoading the training set...")
    with open(config.TRAINING_DATA, 'r') as file:
        for line in file:
            log_lines.append(line)

    print("Calculating anomaly scores for the logs...")

    for line in readlines(config.TRAINING_DATA):

        newline = put_columns(line)
        scores = evaluate_log_line(newline, model)
        training_data.append(scores)

    print("Started anomaly detection...")
    get_anomalies(log_lines, training_data)

    print("Drawing and saving plots to saved_models directory...")
    draw_anomaly_check(training_data)
    draw_anomaly_check_log(training_data)

    print("All done, ready to deploy!")

    return


def get_anomalies(log_lines, training_data):

    line = 0
    anomalous_entries = []

    for scores in training_data:

        anomaly = False
        reason = ""
        if scores[0] > config.RMSD_STATUS:
            reason += " status: " + str(round(scores[0],3))
            anomaly = True

        if scores[1] > config.RMSD_BYTE:
            reason += " byte: " + str(round(scores[1],3))
            anomaly = True

        if scores[2] > config.RMSD_RTIME:
            reason += " rtime: " + str(round(scores[2],3))
            anomaly = True

        if scores[3] > config.RMSD_METHOD:
            reason += " method: " + str(round(scores[3],3))
            anomaly = True

        if scores[4] > config.RMSD_URL:
            reason += " url: " + str(round(scores[4],3))
            anomaly = True

        if anomaly:
            print("Anomaly found from line", line + 1, "\n  ", reason)
            anomalous_entries.append(str(log_lines[line]))
            reason += "\n"
            anomalous_entries.append(reason)

        line += 1

    anomalies_file = config.TRAINING_DATA + '.anomalies'
    print("Writing anomalous entries in training data to: ", anomalies_file)

    with open(anomalies_file, 'w') as file:
        for line in anomalous_entries:
            file.write(line)

    return

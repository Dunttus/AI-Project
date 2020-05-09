# This code runs the training data against the newly trained model
import config
from data_processing.read_data import readlines, put_columns, put_final_columns
from data_processing.rmsdcalc import load_baseline_scores
from data_processing.process import process_apache_log
from data_processing.rmsdcalc import rmsdscore
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

    model_scores = load_baseline_scores()
    m_status_score = model_scores[0]
    m_byte_score = model_scores[1]
    m_rtime_score = model_scores[2]
    m_method_score = model_scores[3]
    m_url_score = model_scores[4]

    print("Calculating anomaly scores for the logs...")

    for line in readlines(config.TRAINING_DATA):

        put_columns(line)
        data, url = process_apache_log(line)
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

        training_data.append([d_status_score,
                              d_byte_score,
                              d_rtime_score,
                              d_method_score,
                              d_url_score])

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

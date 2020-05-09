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

    with open(config.TRAINING_DATA, 'r') as file:
        for line in file:
            log_lines.append(line)

    model_scores = load_baseline_scores()
    m_status_score = model_scores[0]
    m_byte_score = model_scores[1]
    m_rtime_score = model_scores[2]
    m_method_score = model_scores[3]
    m_url_score = model_scores[4]

    print("***Checking training data for anomalies...***")
    print("This takes a bit depending on the dataset size...")

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

    # Draw the plots and save them
    print("Drawing and saving plots...")
    draw_anomaly_check(training_data)
    draw_anomaly_check_log(training_data)

    # We need to calculate the anomaly thresholds depending how the model
    # performs against the training data.


def notworkingyettest():

    line = 0
    anomalous_entries = []

    for scores in training_data:
        #print("Line number:", line)
        anomaly = False
        reason = ""
        if scores[0] > :
            reason += "status "
            anomaly = True

        if scores[1] > :
            reason += "byte "
            anomaly = True

        if scores[2] > :
            reason += "rtime "
            anomaly = True

        if scores[3] > :
            reason += "method "
            anomaly = True

        if scores[4] > :
            reason += "url "
            anomaly = True

        if anomaly:
            print("Anomaly found from line ", line)
            data = str(log_lines[line]) + reason
            anomalous_entries.append(log_lines[line])

        line += 1
        #print(scores)
        #print(mean)
        #print(std)

    #print(anomalous_entries)

    anomalies_file = config.TRAINING_DATA + '.anomalies'
    with open(anomalies_file, 'w') as file:
        for line in anomalous_entries:
            file.write(line)

    return




def check_training_log_lines(line_number):

    model_scores = load_baseline_scores()
    m_status_score = model_scores[0]
    m_byte_score = model_scores[1]
    m_rtime_score = model_scores[2]
    m_method_score = model_scores[3]
    m_url_score = model_scores[4]

    if d_status_score > 0:
        print(f"Hit in status: Line {line_number}, score: {d_status_score}")

    if d_byte_score > 0:
        print(f"Hit in byte: Line {line_number}, score: {d_byte_score}")

    if d_rtime_score > 0:
        print(f"Hit in rtime: Line {line_number}, score: {d_rtime_score}")

    if d_method_score > 0:
        print(f"Hit in method: Line {line_number}, score: {d_method_score}")

    if d_url_score > 0:
        print(f"Hit in url: Line {line_number}, score: {d_url_score}")

    return
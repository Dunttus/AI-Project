# This code runs the training data against the newly trained modeö
import config as config
from data_processing.read_data import readlines, put_columns
from data_processing.rmsdcalc import load_baseline_scores
from data_processing.process import process_apache_log
from data_processing.rmsdcalc import rmsdscore
from data_processing.plots import draw_anomaly_check, draw_anomaly_check_log


def check_training_data(model):

    # This has to be for process_apache_log not to overwrite tokenizers!
    config.SAVE = False

    model_scores = load_baseline_scores()
    m_status_score = model_scores[0]
    m_byte_score = model_scores[1]
    m_rtime_score = model_scores[2]
    m_method_score = model_scores[3]
    m_url_score = model_scores[4]

    training_plot = []
    log_lines = []
    line_number = 1

    print("***Checking training data for anomalies:***")

    for line in readlines(config.TRAINING_DATA):

        log_lines.append(line)

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

        training_plot.append([d_url_score,
                              d_byte_score,
                              d_rtime_score,
                              d_method_score,
                              d_status_score])

        if d_status_score > config.RMSD_THRESHOLD:
            print(f"Hit in status: Line {line_number}, score: {d_status_score}")

        if d_byte_score > config.RMSD_THRESHOLD:
            print(f"Hit in byte: Line {line_number}, score: {d_byte_score}")

        if d_rtime_score > config.RMSD_THRESHOLD:
            print(f"Hit in rtime: Line {line_number}, score: {d_rtime_score}")

        if d_method_score > config.RMSD_THRESHOLD:
            print(f"Hit in method: Line {line_number}, score: {d_method_score}")

        if d_url_score > config.RMSD_THRESHOLD:
            print(f"Hit in url: Line {line_number}, score: {d_url_score}")

        line_number += 1

    draw_anomaly_check(training_plot)
    draw_anomaly_check_log(training_plot)

    print(training_plot)
    print(log_lines[0])

    # TODO: Calculate a good default value for RMSD_THRESHOLD
    # TODO: maybe have to separate all 5 values?

    return

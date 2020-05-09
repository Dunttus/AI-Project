from data_processing.process import process_apache_log
from data_processing.rmsdcalc import rmsdscore, load_baseline_scores


def check_log_line(line, model):

    # Load the baseline model scores
    model_scores = load_baseline_scores()
    m_status_score = model_scores[0]
    m_byte_score = model_scores[1]
    m_rtime_score = model_scores[2]
    m_method_score = model_scores[3]
    m_url_score = model_scores[4]

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

    return [d_status_score,
            d_byte_score,
            d_rtime_score,
            d_method_score,
            d_url_score]

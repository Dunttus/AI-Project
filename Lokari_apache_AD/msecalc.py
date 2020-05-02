import numpy,pandas
from sklearn import metrics
import Lokari_apache_AD.config as config


def msescore(after_ae, before_ae):

    after_ae = pandas.DataFrame(after_ae)
    score = numpy.sqrt(metrics.mean_squared_error(after_ae, before_ae))

    return score


def mse_calc(data, urldata, model):

    before_ae = [data.status, data.byte, data.rtime, data.method, urldata]
    after_ae = model.predict(before_ae)

    status_score = msescore(after_ae[0], before_ae[0])
    byte_score = msescore(after_ae[1], before_ae[1])
    rtime_score = msescore(after_ae[2], before_ae[2])
    method_score = msescore(after_ae[3], before_ae[3])
    url_score = msescore(after_ae[4], urldata)

    print("***MODEL ERROR NUMBERS***")
    print("Model Status MSE:", status_score)
    print("Model Byte MSE:", byte_score)
    print("Model Rtime MSE:", rtime_score)
    print("Model Method MSE:", method_score)
    print("Model URL MSE:", url_score)

    scores = [status_score, byte_score, rtime_score, method_score, url_score]
    if config.SAVE:
        save_baseline_scores(scores)

    return scores


def save_baseline_scores(scores):

    filename = 'saved_models/' + config.VERSION + '/baseline_scores.txt'
    data = ""

    for i in range(len(scores)):
        data += str(scores[i]) + "\n"

    with open(filename, 'w') as file:
        file.write(data)

    return


def load_baseline_scores():

    filename = 'saved_models/' + config.VERSION + '/baseline_scores.txt'

    with open(filename, 'r') as file:
        status_score = float(file.readline())
        byte_score = float(file.readline())
        rtime_score = float(file.readline())
        method_score = float(file.readline())
        url_score = float(file.readline())

    scores = [status_score, byte_score, rtime_score, method_score, url_score]

    return scores

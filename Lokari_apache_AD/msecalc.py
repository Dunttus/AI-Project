import numpy,pandas
from sklearn import metrics


def msescore(after_ae, before_ae):

    after_ae = pandas.DataFrame(after_ae)
    score = numpy.sqrt(metrics.mean_squared_error(after_ae, before_ae))

    return score

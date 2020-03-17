import numpy
from sklearn.metrics import accuracy_score, log_loss

def accuracy(predicted_data, correct_data):

    # Raw hit/miss ratio for classification success
    predictions = numpy.argmax(predicted_data, axis=1)
    correct_classes = numpy.argmax(correct_data, axis=1)
    acc = accuracy_score(correct_classes, predictions)
    print(f"Accuracy: {round(acc, 3)}")

    return


def logarithmic_loss(prediction, correct_data):

    # Logarithmic loss
    # http://wiki.fast.ai/index.php/Log_Loss
    # http://neuralnetworksanddeeplearning.com/chap3.html
    # The more confidence levels are off, this value becomes bigger

    lloss = log_loss(correct_data, prediction)
    print(f"Logarithmic loss: {round(lloss,3)}")

    return
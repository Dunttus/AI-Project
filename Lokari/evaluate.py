import numpy
from sklearn.metrics import accuracy_score

def accuracy(predicted_data, correct_data):

    predictions = numpy.argmax(predicted_data, axis=1)
    correct_classes = numpy.argmax(correct_data, axis=1)
    acc = accuracy_score(correct_classes, predictions)
    print(f"accuracy: {round(acc, 3)}")

    return

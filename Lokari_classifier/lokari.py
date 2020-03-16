# Lokari log classifier
from os import environ as env
from datetime import datetime as dt
from Lokari_classifier.testmodule import test

# Reduce Tensorflow output to console
env['TF_CPP_MIN_LOG_LEVEL'] = '2'

TIMESTAMP = dt.now().isoformat(timespec='seconds')
DATASET_PATH = "../datasets/loglevels/"
DATASET_FILE = "training_logs.json"
MODEL = { "VERSION" : "v0.1",
          "timestamp" : TIMESTAMP }

def main():
    print(f"Lokari-{MODEL['VERSION']}")
    print(test())

if __name__ == '__main__':
    main()

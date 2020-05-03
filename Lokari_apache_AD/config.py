# Global parameters
VERSION = "test"
TRAINING_DATA = "training_dataset/good_access.log"

# Saving model & tokenizers is set in train.py or main.py
SAVE = True

# Tokenizer settings
URL_LENGTH = 64

# Model settings
EPOCHS = 2000


# Model monitor settings

# How many epochs tolerated without improvement?
# NOTE: when the EarlyStopping monitor stops, the loss values of the
# saved model can be read from  epochs trained minus patience.
# If the EarlyStopping doesn't trigger, last epoch is saved.
PATIENCE = 200
# Minimum loss improvement required
MIN_DELTA = 1e-3


# Anomaly detection settings:
# Higher threshold yields less anomalies
RMSD_THRESHOLD = 0.2


def save_config():
    # TODO: save these in a json format

    return


def load_config():
    # TODO: make it possible to reuse saved configs

    return

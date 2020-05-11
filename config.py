# Global parameters
VERSION = "test"
TRAINING_DATA = "datasets/private/1_access.log"
MONITORED_LOG = "datasets/public/monitoring_test.log"

# Saving model & tokenizers is set in train.py or main.py
SAVE = True

# Plot chart settings
LINE_WIDTH = 0.7

# Tokenizer settings

# How many characters from url are processed?
URL_LENGTH = 64

# Model settings
EPOCHS = 2000
# Autoencoder bottleneck layer size, lower values generalize more
BOTTLENECK = 12


# Model monitor settings

# How many epochs tolerated without improvement?
# NOTE: when the EarlyStopping monitor stops, the loss values of the
# saved model can be read from  epochs trained minus patience.
# If the EarlyStopping doesn't trigger, last epoch is saved.
PATIENCE = 20
# Minimum loss improvement required
MIN_DELTA = 1e-3


# Training data detection thresholds
RMSD_STATUS = 0.2
RMSD_BYTE = 0.2
RMSD_RTIME = 0.2
RMSD_METHOD = 0.2
RMSD_URL = 0.2


def save_to_json():
    # TODO: save these in a json format

    return


def load_json():
    # TODO: make it possible to reuse saved configs

    return

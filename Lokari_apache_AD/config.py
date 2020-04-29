# Global parameters
VERSION = "0.32-1"

# Saving model & tokenizers is set in train.py or main.py
SAVE = True

# Tokenizer settings
URL_LENGTH = 64

# Model settings
EPOCHS = 1000


# Model monitor settings

# How many epochs tolerated without improvement?
# NOTE: when the EarlyStopping monitor stops, the loss values of the
# saved model can be read from  epochs trained minus patience.
# If the EarlyStopping doesn't trigger, last epoch is saved.
PATIENCE = 100
# Minimum loss improvement required
MIN_DELTA = 1e-3

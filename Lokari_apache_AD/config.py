# Global parameters
VERSION = "test"

# Saving model & tokenizers is set in train.py or main.py
SAVE = True

# Tokenizer settings


# Model settings
EPOCHS = 50


# Model monitor settings

# How many epochs tolerated without improvement?
# NOTE: when the EarlyStopping monitor stops, the loss values of the
# saved model can be read from  epochs trained minus patience.
# If the EarlyStopping doesn't trigger, last epoch is saved.
PATIENCE = 300
# Minimum loss improvement required
MIN_DELTA = 1e-3

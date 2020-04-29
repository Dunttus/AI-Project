# Global parameters
VERSION = "0.31"

# Are we training or using the model? Set this to 0 to disable tokenizer saving
# functions in process.py. 1 enables model saving.
TRAINING = 0

# Tokenizer settings


# Model settings
EPOCHS = 2

# How many epochs tolerated without improvement?
# NOTE: when the EarlyStopping monitor stops, the loss values of the
# saved model can be read from  epochs trained minus patience.
# If the EarlyStopping doesn't trigger, last epoch is saved.
PATIENCE = 300
MIN_DELTA = 1e-3

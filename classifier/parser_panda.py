# Generate an class-evened dataset with pandas for classification
import pandas as pd
from classifier.ascii_decoder import datatype_check

DS_LOC = "../datasets/loglevels/"
#FILES = ["ubuntu_logs.json", "archelk_logs.json", "upcloudarch3_logs.json"]
FILES = ["failing_logs.json"]

LOG_COUNT = 2000
LOG_DATA = ['PRIORITY', 'MESSAGE']

# The new dataframe to add entries into
DATASET = pd.DataFrame(columns=LOG_DATA)

# Convenience function to check initial value counts
def count_lines_per_loglevel():
    for file in FILES:
        print("Reading file: " + file + "...")
        df = pd.read_json(DS_LOC + file, lines=True)
        print(df['PRIORITY'].value_counts())

# Looking at the data, we'll start small. Maximum of 3000 entries per level,
# 1000 from each file, randomized if there are more than 1000 in the category.
# We don't have data from zero level, just skipping it for now.

for file in FILES:

    print("Reading file: ", file)
    df = pd.read_json(DS_LOC + file, lines=True)
    df.MESSAGE = df.MESSAGE.apply(datatype_check)

    for i in range(1,8):

        print("Getting messages from log level ", i)
        part = df.loc[df['PRIORITY'] == i]

        if part['PRIORITY'].size > LOG_COUNT:
            part = part.sample(n=LOG_COUNT)

        DATASET = pd.concat([DATASET,part[LOG_DATA]])

print("\nGenerated dataframe value counts:")
print(DATASET['PRIORITY'].value_counts())

# Make a json file to examine the data...
DATASET.to_json(DS_LOC + "testing_decoder.json", orient="records", lines=True)

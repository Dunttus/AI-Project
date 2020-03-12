# Generate an class-evened dataset with pandas for classification
import pandas as pd

DS_LOC = "../datasets/loglevels/"
FILES = ["ubuntu_logs.json", "archelk_logs.json", "upcloudarch3_logs.json"]
TESTFILE = "ubuntu_logs_tail.json"
LOG_DATA = ['PRIORITY', 'MESSAGE']

# Convenience function to check initial value counts
def count_lines_per_loglevel():
    for file in FILES:
        print("Reading file: " + file + "...")
        df = pd.read_json(DS_LOC + file, lines=True)
        print(df['PRIORITY'].value_counts())

# Looking at the data, we'll start small. Maximum of 3000 entries per level,
# 1000 from each file, randomized if there are more than 1000 in the category.
# We don't have data from zero level, just skipping it for now.

df = pd.read_json(DS_LOC + FILES[0], lines=True)

for i in range(1,8):
    test = df.loc[df['PRIORITY'] == i]
    print("Log level " + str(i) + ": ", end ='')
    if test['PRIORITY'].size > 1000:
        # These entries have to be reduced
        print(">1000")
    else:
        # These entries go straight into the dataset
        print("<1000")


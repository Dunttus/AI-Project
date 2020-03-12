# Generate an class-evened dataset for classification with pandas
import pandas as pd

DS_LOC = "../datasets/loglevels/"
FILES = ["ubuntu_logs.json", "archelk_logs.json", "upcloudarch3_logs.json"]
TESTFILE = "ubuntu_logs_tail.json"

def count_lines_per_loglevel():
    for file in FILES:
        print("Reading file: " + file + "...")
        df = pd.read_json(DS_LOC + file, lines=True)
        print(df['PRIORITY'].value_counts())

count_lines_per_loglevel()


# Generate an class-evened dataset for classification with pandas
import pandas as pd

DS_LOC = "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/loglevels/"
FILES = ["ubuntu_logs.json", "archelk_logs.json", "upcloudarch3_logs.json"]
TESTFILE = "ubuntu_logs_tail.json"

df = pd.read_json(TESTFILE, lines=True)
print(df['PRIORITY'].value_counts())

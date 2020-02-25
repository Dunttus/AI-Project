import pandas as pd

# With a large file, this takes time to execute!
df = pd.read_json("ubuntu_logs_test", lines=True)
print(df[['PRIORITY','MESSAGE']])
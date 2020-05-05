import pandas as pd

print(f"Pandas data-analysis API version: {pd.__version__}")

# Series object
series1 = pd.Series(['This', 'is an example', 'Series object', '!', ])
print(series1)
series2 = pd.Series(['2', '3', '4', '5', '6'])
print(series2)

# Series combine into a DataFrame object
df = pd.DataFrame({ 'Text': series1, 'Numbers': series2})
print(df)

# Load a file into a DataFrame object:
# Multiple file formats are supported. Testing json first.
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-json-reader
# Example file can be created with journalctl:
# sudo journalctl -n 5 -o json --output-fields=PRIORITY,MESSAGE > pandatest.json
logs = pd.read_json("pandatest.json", lines=True)
print(logs.columns)
# This leaves only the wanted columns
parsed_logs = logs.drop(['__CURSOR','__MONOTONIC_TIMESTAMP', '_BOOT_ID', '__REALTIME_TIMESTAMP'], axis=1)
print(parsed_logs)

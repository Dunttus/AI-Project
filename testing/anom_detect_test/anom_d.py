# Testing autoencoder

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../../datasets/apache_access_log/access_log_testing.csv')
# We have column heads on the csv file already:
# 2 are missing! client identity, if determined, and userid, if authenticated
print(df.columns)
print(df)
# Identify the datatypes and attributes in each column for encoding them:

# clientip = IP address initiating the connection
# - how to categorize these?
# - known/unknown?
# - basically, distinguish a frequent visitor from a DDoS attack
# - exotic one-timers

# MISSING: client identity determined by identd on client's machine
# a hyphen (-) if missing

# MISSING: userid of the client if request was authenticated
# this is actually important!
# user actions keyed to times they do it etc.

# timestamp = time connection was made
# - time of the day only?
# - temporal data analysis (look into LSTM later)

# verb = HTTP request type
# - these are known, categorize (eg. one-hot-encode)

# request = the request itself, text and variables
# - typical requests done to page
# - this depends on the page alot!

# response = HTTP status code
#  - these are known, categorize

# bytes = size of the object requested
# - explain this more
# JSON format example for model data saving
import datetime as dt
import json
DATA = {
"version" : "v0.1",
"timestamp" : dt.datetime.now().isoformat(timespec='seconds'),
"parameters": {
    "test_set_size" : 0.2,
    "epochs" : 5590
    },
"scores": {
    "accuracy" : 90.0
    },
}

# Accessing items
print(DATA)
print(DATA['parameters'])
print(DATA['version'])
print(DATA['parameters']['epochs'])

# Write a nested dict into json:
with open("data_test.json","a") as f:
    json.dump(DATA, f)
    f.write('\n')

# JSON format example for model data saving
import datetime as dt
import json
DATA = {
"version" : "v0.1",
"timestamp" : dt.datetime.now().isoformat(),
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

# Model info
MODEL = {
    "VERSION" : "0.1",
    "timestamp" : dt.datetime.now().isoformat(timespec='seconds'),

}


# Model parameters
test_set_part = 0.4
epochs = 5042

# Moden eval metrics
accuracy = 9142.23

# Generate a dict structure from the above data:
param = {
    "test_set_part" : 0.2,
    "epochs" : 50
}
score = {
    "accuracy" : 91.23
}

# Access the parameters inside code:
print(param['epochs'])

MODEL['parameters'] = param
MODEL['score'] = score

# Write a nested dict into json:
with open("data_test.json","a") as f:
    json.dump(MODEL, f)
    f.write('\n')

# JSON format example for model data saving
import datetime as dt
DATA = {
"version" : "v0.1",
"timestamp" : dt.datetime.now().isoformat(timespec='minutes'),
"parameters": [
    {   "test_set_size" : 0.2,
        "epohcs" : 50
    }],
"scores": [
    {   "accuracy" : 90.0
    }],
}

print(DATA)
print(DATA['parameters'])

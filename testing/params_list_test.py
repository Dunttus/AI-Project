import datetime as dt
PARAM = {
    "VERSION" : "v0.1",
    "TIMESTAMP" : dt.datetime.now().isoformat(timespec='minutes'),
    "TEST_SET_SIZE" : 0.2,
    "EPOCHS" : 50
}

print(PARAM)
print(PARAM['TEST_SET_SIZE'])

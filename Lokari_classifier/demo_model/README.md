## Testing with new data

### Enviroment installation
```$ sudo apt install python3-pip``` \
```$ sudo pip3 install tensorflow``` \
```$ sudo pip3 install sklearn``` \
```$ sudo pip3 install pandas``` \

### Commands for the model
Fetch log files from journalctl into text file testdata.json \
```$ journalctl -o json -b > testdata.json``` \
Removing all logs with no PRIORITETY value \
```$ grep '"PRIORITY"' testdata.json > testdata2.json``` \
Run demo.py with testdata2.json log files \
```$ ./demo.py testdata2.json```

# Lokari log classifier

A machine learning program to distinguish different log levels from Linux logs.

Code refactoring and modularizing in progress...
```
main.py     main program  
evaluate.py evaluation code
models.py   keras machine learning model
nlp.py      natural language processing functions

```

## Testing with new data

### Enviroment installation
```$ sudo apt install python3-pip``` \
```$ sudo pip3 install tensorflow``` \
```$ sudo pip3 install sklearn``` \
```$ sudo pip3 install pandas``` \

### Commands for the model
Folder: /AI-Project/Lokari/demo_model \
Fetch log files from journalctl into text file testdata.json \
```$ journalctl -o json -b > testdata.json``` \
Removing all logs with no PRIORITETY value \
```$ grep '"PRIORITY"' testdata.json > testdata2.json``` \
Run demo.py with testdata2.json log files \
```$ ./demo.py testdata2.json``` \

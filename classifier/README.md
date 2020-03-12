# Multiclass classifier

Parser Panda:
- counts value distributions: lines per log level in the sample dataset
- wants to generate a more even dataset for training
```
size        file
702657664   archelk_logs.json
652395735   ubuntu_logs.json
734891684   upcloudarch3_logs.json
```
__Running the Parser Panda counting fuction:__
```
Reading file: ubuntu_logs.json...
5.0    73877
6.0    59276
4.0    43876
7.0     3779
2.0      545
3.0      484
1.0        9
Name: PRIORITY, dtype: int64
Reading file: archelk_logs.json...
4.0    253611
6.0    246534
5.0      4520
7.0       344
3.0        24
2.0         2
Name: PRIORITY, dtype: int64
Reading file: upcloudarch3_logs.json...
4.0    532264
6.0    284888
5.0     70313
7.0      2194
3.0        94
2.0        27
Name: PRIORITY, dtype: int64
```
__Parser Panda in action:__
```
Generated dataframe value counts:
6.0    3000
5.0    3000
4.0    3000
7.0    2344
3.0     602
2.0     574
1.0       9
Name: PRIORITY, dtype: int64
```
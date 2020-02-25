# Classifier testing and comparison

- Naive Bayes classifier

### Word counts and value distributions

Sample outputs from a testing phase on the data set (25. Feb 2020)

```
size        file
702657664   archelk_logs.json
652395735   ubuntu_logs.json
734891684   upcloudarch3_logs.json
```

```
ubuntu_logs.json:

[696424 rows x 2 columns]
Total words in the message data: 6296875
Value distribution in 'PRIORITY':
NaN    514578
5.0     73877
6.0     59276
4.0     43876
7.0      3779
2.0       545
3.0       484
1.0         9


archelk_logs.json:

[509852 rows x 2 columns]
Total words in the message data: 6264995
Value distribution in 'PRIORITY':
4.0    253611
6.0    246534
NaN      4817
5.0      4520
7.0       344
3.0        24
2.0         2


upcloudarch3_logs.json:

[962485 rows x 2 columns]
Total words in the message data: 12308352
Value distribution in 'PRIORITY':
4.0    532264
6.0    284888
NaN     72705
5.0     70313
7.0      2194
3.0        94
2.0        27
```
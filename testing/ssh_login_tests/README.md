# Console output

```
003eb4e3263d:python /opt/.pycharm_helpers/pydev/pydevconsole.py --mode=server --port=38789
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/joni/AI-Project', '/home/joni/AI-Project'])
PyDev console: starting.
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
>>> from __future__ import absolute_import, division, print_function, unicode_literals
... 
... import tensorflow as tf
... import pandas as pd
... import numpy as np
... from matplotlib import pyplot as plt
... 
2020-03-13 16:32:18.593583: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer.so.6
2020-03-13 16:32:18.594760: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libnvinfer_plugin.so.6
from __future__ import absolute_import, division, print_function, unicode_literals
... 
... import tensorflow as tf
... import pandas as pd
... import numpy as np
... from matplotlib import pyplot as plt
... 
from __future__ import absolute_import, division, print_function, unicode_literals
... 
... import tensorflow as tf
... import pandas as pd
... import numpy as np
... from matplotlib import pyplot as plt
... 
# test that GPU is working
... print(f"TensorFlow: {tf.__version__}")
... tf.config.list_physical_devices('GPU')
... 
TensorFlow: 2.1.0
2020-03-13 16:32:30.589421: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2020-03-13 16:32:30.613637: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:32:30.613934: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: GeForce GTX 1050 Ti computeCapability: 6.1
coreClock: 1.455GHz coreCount: 6 deviceMemorySize: 3.94GiB deviceMemoryBandwidth: 104.43GiB/s
2020-03-13 16:32:30.613963: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-03-13 16:32:30.613994: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2020-03-13 16:32:30.615593: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2020-03-13 16:32:30.615937: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2020-03-13 16:32:30.617177: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2020-03-13 16:32:30.617911: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2020-03-13 16:32:30.617947: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2020-03-13 16:32:30.618069: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:32:30.618421: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:32:30.618695: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
# Downloading .csv files from github to local computer
... TRAIN_DATASET_GOOD = \
...     "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_event_good.csv"
... TRAIN_DATASET_BAD = \
...     "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events_bad.csv"
... TEST_DATASET_GOOD = \
...     "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events_good.csv"
... TEST_DATASET_BAD = \
...     "https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events_bad.csv"
... 
... # Naming dataset's
... traing_file_path = tf.keras.utils.get_file("traing.csv", TRAIN_DATASET_GOOD)
... trainb_file_path = tf.keras.utils.get_file("trainb.csv", TRAIN_DATASET_BAD)
... testg_file_path = tf.keras.utils.get_file("testg.csv", TEST_DATASET_GOOD)
... testb_file_path = tf.keras.utils.get_file("testb.csv", TEST_DATASET_BAD)
... 
Downloading data from https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_event_good.csv
49152/46788 [===============================] - 0s 1us/step
Downloading data from https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/train_ssh_events_bad.csv
8192/2135 [===================================================================================================================] - 0s 0us/step
Downloading data from https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events_good.csv
16384/9925 [=================================================] - 0s 0us/step
Downloading data from https://raw.githubusercontent.com/Dunttus/AI-Project/master/datasets/ssh_login/test_ssh_events_bad.csv
8192/3626 [===================================================================] - 0s 0us/step
# Creating Pandas variable "dfTraingood"
... dfTraingood = pd.read_csv(TRAIN_DATASET_GOOD)
... 
... # Creating Pandas variable "dfTrainbad"
... dfTrainbad = pd.read_csv(TRAIN_DATASET_BAD)
... 
... # Creating Pandas variable "dfTestgood"
... dfTestgood = pd.read_csv(TEST_DATASET_GOOD)
... 
... # Creating Pandas variable "dfTestbad"
... dfTestbad = pd.read_csv(TEST_DATASET_BAD)
... 
# Testing to read pandas object BAD_DATASET first 5 lines
... dfTraingood.head()
                   @timestamp  ... event.outcome
0  Feb 1, 2020 @ 18:28:33.000  ...       failure
1  Feb 1, 2020 @ 18:28:26.000  ...       failure
2  Feb 1, 2020 @ 18:28:23.000  ...       failure
3  Feb 1, 2020 @ 18:28:19.000  ...       failure
4  Feb 1, 2020 @ 18:28:16.000  ...       failure
[5 rows x 4 columns]
# count number of TRAIN_DATASET_GOOD logs
... dfTraingood.groupby('event.outcome')['event.outcome'].count()
event.outcome
failure    999
Name: event.outcome, dtype: int64
# count number of TRAIN_DATASET_BAD logs
... dfTrainbad.groupby('event.outcome')['event.outcome'].count()
event.outcome
success    43
Name: event.outcome, dtype: int64
# count number of TEST_DATASET_BAD logs
... dfTestgood.groupby('event.outcome')['event.outcome'].count()
event.outcome
failure    196
success      2
Name: event.outcome, dtype: int64
# count number of TEST_DATASET_BAD logs
... dfTestbad.groupby('event.outcome')['event.outcome'].count()
event.outcome
success    72
Name: event.outcome, dtype: int64
# Add new column predict with values 0 as normal or 1 as not normal "labeling data"
... dfTraingood['predict'] = 0
... dfTrainbad['predict'] = 1
... 
# Combine dfTraingood and dfTrainbad into dfTraincombined
... dfTraincombined = dfTraingood.append(dfTrainbad)
... print(dfTraincombined)
... 
                     @timestamp user.name  ... event.outcome predict
0    Feb 1, 2020 @ 18:28:33.000      root  ...       failure       0
1    Feb 1, 2020 @ 18:28:26.000      root  ...       failure       0
2    Feb 1, 2020 @ 18:28:23.000      root  ...       failure       0
3    Feb 1, 2020 @ 18:28:19.000      root  ...       failure       0
4    Feb 1, 2020 @ 18:28:16.000      root  ...       failure       0
..                          ...       ...  ...           ...     ...
38  Jan 17, 2020 @ 09:42:03.000  memcache  ...       success       1
39  Jan 17, 2020 @ 09:42:01.000  memcache  ...       success       1
40  Jan 16, 2020 @ 10:29:04.000   mikhail  ...       success       1
41  Jan 16, 2020 @ 10:29:03.000   mikhail  ...       success       1
42  Jan 16, 2020 @ 07:34:53.000     ghost  ...       success       1
[1042 rows x 5 columns]
# count number of dfTraincombined logs
... dfTraincombined.groupby('event.outcome')['event.outcome'].count()
event.outcome
failure    999
success     43
Name: event.outcome, dtype: int64
# Re-naming column names of dfTraincombined
... dfTraincombined.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo',
...                         'event.outcome': 'event'}, axis='columns', inplace=True)
# Convert dfTraincombined data from object to numeric category values
... dfTraincombined['time'] = pd.Categorical(dfTraincombined['time'])
... dfTraincombined['time'] = dfTraincombined.time.cat.codes
... dfTraincombined['user'] = pd.Categorical(dfTraincombined['user'])
... dfTraincombined['user'] = dfTraincombined.user.cat.codes
... dfTraincombined['geo'] = pd.Categorical(dfTraincombined['geo'])
... dfTraincombined['geo'] = dfTraincombined.geo.cat.codes
... dfTraincombined['event'] = pd.Categorical(dfTraincombined['event'])
... dfTraincombined['event'] = dfTraincombined.event.cat.codes
... print(dfTraincombined)
... 
    time  user  geo  event  predict
0    890   125    4      0        0
1    889   125    4      0        0
2    888   125    4      0        0
3    887   125    4      0        0
4    886   125    4      0        0
..   ...   ...  ...    ...      ...
38   903    90   20      1        1
39   902    90   20      1        1
40   897    92   20      1        1
41   896    92   17      1        1
42   895    68   17      1        1
[1042 rows x 5 columns]
# List data types of data
... dfTraincombined.dtypes
time       int16
user       int16
geo         int8
event       int8
predict    int64
dtype: object
# target whole dataset dfTraincombined with value predict
... target = dfTraincombined.pop('predict')
# Creating input pipeline from dataset for Tensorflow
... dataset = tf.data.Dataset.from_tensor_slices((dfTraincombined.values, target.values))
2020-03-13 16:33:07.489021: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-03-13 16:33:07.514664: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3393155000 Hz
2020-03-13 16:33:07.515162: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5eda980 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-03-13 16:33:07.515186: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-03-13 16:33:07.572156: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:33:07.572531: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5f70a30 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2020-03-13 16:33:07.572548: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): GeForce GTX 1050 Ti, Compute Capability 6.1
2020-03-13 16:33:07.572715: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:33:07.572981: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1555] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: GeForce GTX 1050 Ti computeCapability: 6.1
coreClock: 1.455GHz coreCount: 6 deviceMemorySize: 3.94GiB deviceMemoryBandwidth: 104.43GiB/s
2020-03-13 16:33:07.573020: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-03-13 16:33:07.573032: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
2020-03-13 16:33:07.573049: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
2020-03-13 16:33:07.573061: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
2020-03-13 16:33:07.573070: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
2020-03-13 16:33:07.573082: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
2020-03-13 16:33:07.573091: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
2020-03-13 16:33:07.573152: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:33:07.573569: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:33:07.573837: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-13 16:33:07.573866: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.1
2020-03-13 16:33:07.754197: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-13 16:33:07.754241: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0 
2020-03-13 16:33:07.754248: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N 
2020-03-13 16:33:07.754550: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:33:07.754978: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-03-13 16:33:07.755264: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 3001 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1050 Ti, pci bus id: 0000:26:00.0, compute capability: 6.1)
dfTraincombined.head()
   time  user  geo  event
0   890   125    4      0
1   889   125    4      0
2   888   125    4      0
3   887   125    4      0
4   886   125    4      0
# shuffle dfc dataset with new object train_dataset
... train_dataset = dataset.shuffle(len(dfTraincombined)).batch(1)
# Making model
... def training_model():
...     model = tf.keras.Sequential([
...         tf.keras.layers.Dense(10, activation='relu'),
...         tf.keras.layers.Dense(3, activation='relu'),
...         tf.keras.layers.Dense(10, activation='relu'),
...         tf.keras.layers.Dense(1, activation='sigmoid')
...     ])
...     model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])
...     return model
... 
# Starts building model
... # Having more epochs increase accuracy of the model. Having too high value may decrease model reliability.
... # 1 epochs take about 10-min with gtx 1050TI
... model = training_model()
... model.fit(train_dataset, epochs=2, verbose=1)
... 
Train for 1042 steps
Epoch 1/2
2020-03-13 16:33:30.566072: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
1042/1042 [==============================] - 3s 3ms/step - loss: 0.7780 - accuracy: 0.8253
Epoch 2/2
1042/1042 [==============================] - 3s 3ms/step - loss: 0.6932 - accuracy: 0.9587
# Add new column predict with values 0 as normal or 1 as not normal "labeling data"
... dfTestgood['predict'] = 0
... dfTestbad['predict'] = 1
... 
# Combine dfTestgood and dfTestbad into dfTestcombined
... dfTestcombined = dfTestgood.append(dfTestbad)
... print(dfTestcombined)
... 
                     @timestamp     user.name  ... event.outcome predict
0   Feb 21, 2020 @ 20:02:55.000         steam  ...       failure       0
1   Feb 21, 2020 @ 20:02:53.000         steam  ...       failure       0
2   Feb 21, 2020 @ 20:02:46.000         lisha  ...       failure       0
3   Feb 21, 2020 @ 20:02:44.000         lisha  ...       failure       0
4   Feb 21, 2020 @ 20:02:41.000       maurice  ...       failure       0
..                          ...           ...  ...           ...     ...
67  Feb 21, 2020 @ 19:48:15.000  zhaoshaojing  ...       success       1
68  Feb 21, 2020 @ 19:48:14.000      postgres  ...       success       1
69  Feb 21, 2020 @ 19:48:12.000  zhaoshaojing  ...       success       1
70  Feb 21, 2020 @ 19:48:08.000       proftpd  ...       success       1
71  Feb 21, 2020 @ 19:48:06.000       proftpd  ...       success       1
[277 rows x 5 columns]
# Re-naming column names dfTestcombined
... dfTestcombined.rename({'@timestamp': 'time', 'user.name': 'user', 'source.geo.country_iso_code': 'geo',
...                        'event.outcome': 'event'}, axis='columns', inplace=True)
# Data types of dfTestcombined
... dfTestcombined.dtypes
time       object
user       object
geo        object
event      object
predict     int64
dtype: object
# Convert dfTestcombined data from object to numeric category values
... dfTestcombined['time'] = pd.Categorical(dfTestcombined['time'])
... dfTestcombined['time'] = dfTestcombined.time.cat.codes
... dfTestcombined['user'] = pd.Categorical(dfTestcombined['user'])
... dfTestcombined['user'] = dfTestcombined.user.cat.codes
... dfTestcombined['geo'] = pd.Categorical(dfTestcombined['geo'])
... dfTestcombined['geo'] = dfTestcombined.geo.cat.codes
... dfTestcombined['event'] = pd.Categorical(dfTestcombined['event'])
... dfTestcombined['event'] = dfTestcombined.event.cat.codes
... print(dfTestcombined)
... 
    time  user  geo  event  predict
0    236    74   13      0        0
1    235    74   13      0        0
2    234    46    5      0        0
3    233    46    5      0        0
4    232    49    3      0        0
..   ...   ...  ...    ...      ...
67     4    96   12      1        1
68     3    61    7      1        1
69     2    96   12      1        1
70     1    62    5      1        1
71     0    62    5      1        1
[277 rows x 5 columns]
# Data types of dfTestcombined
... dfTestcombined.dtypes
time       int16
user        int8
geo         int8
event       int8
predict    int64
dtype: object
# target whole dataset dfTestcombined with value predict
... target = dfTestcombined.pop('predict')
# Creating input pipeline from dataset for Tensorflow
... datasetTest = tf.data.Dataset.from_tensor_slices((dfTestcombined.values, target.values))
# shuffle dfTestcombined dataset with new object test_dataset
... test_dataset = datasetTest.shuffle(len(dfTestcombined)).batch(1)
# Evaluate model
... results = model.evaluate(test_dataset)
... print(results)
... 
277/277 [==============================] - 1s 2ms/step - loss: 0.6929 - accuracy: 0.7401
[0.6929077615806772, 0.7400722]
# Predictions from test dataset
... prediction = model.predict(dfTestcombined)
... print(prediction)
... 
[[2.77303656e-08]
 [3.08408978e-08]
 [5.86712368e-09]
 [6.52524346e-09]
 [3.05139345e-08]
 [3.39367041e-08]
 [1.32644037e-12]
 [1.47523378e-12]
 [6.86415551e-12]
 [7.63414158e-12]
 [9.63875941e-12]
 [1.07199466e-11]
 [2.09739983e-06]
 [1.60238915e-06]
 [2.59434455e-06]
 [1.98205134e-06]
 [3.20903791e-06]
 [2.43340956e-08]
 [7.08100561e-06]
 [2.70635141e-08]
 [7.87530280e-06]
 [4.41461907e-06]
 [7.06126002e-06]
 [7.06126002e-06]
 [5.46057800e-06]
 [1.16818133e-09]
 [9.71405279e-06]
 [9.71405279e-06]
 [7.51202606e-06]
 [9.12384567e-05]
 [8.96525671e-05]
 [5.34818367e-09]
 [4.07987172e-10]
 [6.61534560e-09]
 [4.88992700e-11]
 [5.04650988e-10]
 [5.43845455e-11]
 [3.73946929e-10]
 [1.19820375e-04]
 [4.15894402e-10]
 [1.31014065e-04]
 [1.00305463e-07]
 [1.11556368e-07]
 [1.10367102e-06]
 [1.20679465e-06]
 [4.19600298e-07]
 [4.58806454e-07]
 [1.46340735e-08]
 [1.04934575e-10]
 [1.62756812e-08]
 [1.16705826e-10]
 [4.47817977e-10]
 [4.98051045e-10]
 [1.72973614e-06]
 [1.50945277e-06]
 [9.47246463e-06]
 [1.03574248e-05]
 [1.34848904e-07]
 [5.83882093e-06]
 [5.09523079e-06]
 [1.66797619e-07]
 [5.23618482e-09]
 [5.82356474e-09]
 [1.10147816e-07]
 [4.89159990e-10]
 [5.44031431e-10]
 [2.17926981e-07]
 [4.16657002e-08]
 [4.63394620e-08]
 [2.20485017e-04]
 [2.41081521e-04]
 [3.00532447e-05]
 [2.63600232e-04]
 [3.34242250e-05]
 [2.66079337e-06]
 [2.32195066e-06]
 [3.40757511e-09]
 [3.78980580e-09]
 [3.88743327e-04]
 [3.81985534e-04]
 [1.23201637e-04]
 [1.18786261e-07]
 [3.10406108e-07]
 [1.47296727e-04]
 [1.46930361e-07]
 [2.36378426e-07]
 [6.01652369e-04]
 [4.25588560e-08]
 [5.80925553e-04]
 [9.60938178e-06]
 [5.80925553e-04]
 [5.80925553e-04]
 [5.26424628e-08]
 [1.18860908e-05]
 [5.51166129e-04]
 [5.51166129e-04]
 [5.41588175e-04]
 [5.31100202e-04]
 [5.08327270e-04]
 [5.82410621e-06]
 [6.36828327e-06]
 [4.65667166e-04]
 [4.45698272e-04]
 [1.76848073e-06]
 [2.36632332e-04]
 [3.90783418e-04]
 [3.90783418e-04]
 [2.69570912e-04]
 [3.74025374e-04]
 [3.57985497e-04]
 [1.62927099e-05]
 [2.98844941e-04]
 [1.78150422e-05]
 [5.90189757e-07]
 [5.15028546e-07]
 [2.27591721e-04]
 [4.86572631e-08]
 [4.00837393e-07]
 [4.24608331e-08]
 [4.45801703e-07]
 [6.88813673e-10]
 [6.01090844e-10]
 [2.98373493e-07]
 [2.60375089e-07]
 [6.91706603e-09]
 [3.44941498e-08]
 [6.03615291e-09]
 [3.83635275e-08]
 [2.25208666e-07]
 [4.47150200e-07]
 [4.97309202e-07]
 [1.26189152e-05]
 [4.64146906e-05]
 [5.16207911e-05]
 [3.78419500e-08]
 [3.30226442e-08]
 [1.71080792e-05]
 [1.49294237e-05]
 [1.30281578e-05]
 [1.71429638e-05]
 [1.90659030e-05]
 [3.17733575e-05]
 [2.77270774e-05]
 [2.41961352e-05]
 [2.11147581e-05]
 [1.08573200e-04]
 [8.71591965e-06]
 [9.69361008e-06]
 [1.23791033e-04]
 [1.37675379e-04]
 [5.66316558e-05]
 [6.29837887e-05]
 [3.30554784e-08]
 [2.96659255e-05]
 [1.93484334e-06]
 [5.41012196e-06]
 [4.72112697e-06]
 [1.47341518e-06]
 [1.55273358e-06]
 [1.65723541e-05]
 [1.12203099e-06]
 [1.58866660e-05]
 [9.00441535e-07]
 [7.45630018e-07]
 [6.50675247e-07]
 [3.73773696e-06]
 [4.15700788e-06]
 [4.95501695e-07]
 [5.22174560e-07]
 [6.08884193e-06]
 [3.77332299e-07]
 [5.96157179e-06]
 [1.87360114e-04]
 [1.63503675e-04]
 [2.87344704e-07]
 [2.50750816e-07]
 [2.09720252e-04]
 [1.90950857e-07]
 [2.59397057e-04]
 [3.20052152e-07]
 [2.82632328e-07]
 [6.73876048e-13]
 [5.95083878e-13]
 [1.17759482e-05]
 [1.02762842e-05]
 [3.98243201e-12]
 [3.51683136e-12]
 [2.21779994e-09]
 [2.74253883e-12]
 [2.42189363e-12]
 [5.56065860e-09]
 [4.91053154e-09]
 [5.12871386e-12]
 [4.52906202e-12]
 [1.51906970e-12]
 [4.03815386e-04]
 [7.02664815e-03]
 [7.67814508e-03]
 [1.45152118e-02]
 [1.61831211e-02]
 [9.43829713e-04]
 [9.20926713e-09]
 [1.33326561e-09]
 [5.56173976e-13]
 [4.87749181e-11]
 [4.71693810e-13]
 [4.13662438e-11]
 [1.33926312e-12]
 [1.18267809e-12]
 [7.08465133e-13]
 [6.25632196e-13]
 [2.53911770e-04]
 [2.82385736e-04]
 [8.30174424e-04]
 [6.21594381e-07]
 [1.33116424e-04]
 [2.30299105e-04]
 [3.04977056e-02]
 [2.84849084e-04]
 [5.31826970e-07]
 [2.35927179e-02]
 [4.69646011e-07]
 [2.67433315e-05]
 [2.61842724e-05]
 [6.49667653e-10]
 [5.73708248e-10]
 [5.06630959e-10]
 [4.47397980e-10]
 [3.95087962e-10]
 [2.00184854e-03]
 [3.48894746e-10]
 [3.08102377e-10]
 [2.72079942e-10]
 [2.49715638e-04]
 [2.12176748e-10]
 [1.94747394e-04]
 [1.54722240e-02]
 [9.29764668e-11]
 [1.90681852e-02]
 [1.13946907e-10]
 [7.06852166e-13]
 [6.70337749e-06]
 [6.15319753e-13]
 [6.79268669e-06]
 [7.84701401e-11]
 [1.82052420e-12]
 [1.47662167e-12]
 [5.17355707e-11]
 [1.45353796e-02]
 [1.61395855e-02]
 [3.40046711e-08]
 [3.00288896e-08]
 [4.10859320e-06]
 [4.09426184e-06]
 [1.82498204e-15]
 [1.48023994e-15]
 [3.68993394e-02]
 [3.27263214e-02]
 [1.47002480e-10]
 [1.19233484e-10]
 [2.61444630e-14]
 [2.39297226e-14]
 [2.82958081e-06]
 [1.05319597e-17]
 [9.63974117e-18]
 [2.20659786e-06]
 [1.23633590e-12]
 [1.03805755e-12]
 [9.03408858e-13]
 [8.92065877e-15]
 [6.15311838e-12]
 [8.45209794e-15]
 [1.61369330e-18]
 [5.52373642e-12]
 [1.44863127e-18]
 [4.12767693e-12]
 [3.91086902e-12]]
# First position result
... np.argmax(prediction[0])
0
# Loop results
... for i in range(277):
...     fullRange = np.argmax(prediction[i])
...     print(fullRange)
... 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
```

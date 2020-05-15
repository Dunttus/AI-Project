# Lokari - Web server log anomaly detector 
### Machine learning based monitoring application for anomalies in web server logs.

Machine learning project by Tuomo Kuure [(tqre)](https://tqre.wordpress.com/) and Joni Hakala [(Dunttus)](http://dunttus.com/).  
Supervising teacher: Tero Karvinen - http://terokarvinen.com  
[Haaga-Helia University of Applied Sciences](http://www.haaga-helia.fi/en/frontpage)  
Course: Monialaprojekti - Multisectoral project (ICT-infrastructures) PRO4TN004-3005.

#### Project blog: [https://ailogs.design.blog/](https://ailogs.design.blog/)
### Directories:
**/.idea** - PyCharm configuration files \
**/archives** - Project history \
**/archives/Lokari_classifier** - First demo model \
**/data_processing** - Data processing modules \
**/datasets** - Datasets used in training \
**/docker** - Project runtime container \
**/install** - Installation instructions \
**/saved_models** - Directory to save model data

### Files:
**config.py** - Main configuration file \
**main.py** - Log monitor \
**train.py** - Detector training

### Usage:
1. Configure logs to right format (see install)
2. Gather training material (logs)
3. Clone this repo and train the model
4. Analyze your training material with graphs from the training process
5. Tune the thresholds and start monitoring

### Requirements
* Python 3.6.9
* Tensorflow 2.1.0 plus a few other libraries
* Linux with Apache/Nginx web server
* GPU Support with Docker 19.03
  + tensorflow/tensorflow:latest-gpu-py3 (see our Dockerfile)
  + nvidia-container-toolkit
  + nvidia-container-runtime


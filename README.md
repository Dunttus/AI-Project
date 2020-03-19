# AI-Project: Anomaly detection with Tensorflow.

This repository is designed be cloned with PyCharm Pro. The runtime environment is containerized with Docker.  
First command line demo is available in /Lokari/demo_model

## Follow the project blog:
[https://ailogs.design.blog/](https://ailogs.design.blog/)  

### Directories:  
**/.idea** - PyCharm configuration files \
**/Lokari** - Lokari log classifier machine learning model construction code \
**/classifier** - First log classifier code snippets \
**/datasets** - datasets live here (big sets are .gitignored) \
**/docker** - Project runtime container \
**/log_parsing** - Journalctl JSON scripts and ElasticSearch database population \
**/memos** - Memorandums \
**/testing** - Testing or studying code bits

### Working environment:
* Ubuntu 18.04/Arch Linux
* PyCharm 2019.3 Professional Edition
  * docker plugin  
  * custom Dockerfile based on tensorflow:latest
    * Python 3.6.9
    * Tensorflow 2.1.0
* Docker 19.03  
* nvidia-container-toolkit 
* nvidia-container-runtime

## Sources
[Tero Karvinen](http://terokarvinen.com) & Harto Holmström 2020, Haaga-Helia University of Applied Sciences course monialaprojekti (ICT-infrastruktuurit) PRO4TN004-3005. 

# AI-Project: Anomaly detection with Tensorflow.

This repository is designed be cloned with PyCharm Pro. The runtime environment is containerized with Docker. See the project blog for details.

### Directories:  
**/.idea** - PyCharm configuration files \
**/classifier** - Log classifier code \
**/datasets** - datasets live here (big sets are .gitignored) \
**/docker** - Project runtime container \
**/log_parsing** - Journalctl JSON scripts and ElasticSearch database population \
**/memos** - Memorandums \
**/testing** - Testing or studying code bits

## Follow the project blog:
[https://ailogs.design.blog/](https://ailogs.design.blog/)  

### Working with:
* Ubuntu 18.04/Arch Linux
* PyCharm 2019.3 Professional Edition
  * docker plugin  
  * custom Dockerfile based on tensorflow:latest
* Docker 19.03  
* nvidia-container-toolkit and runtime
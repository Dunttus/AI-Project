# Help for setting-up
# Log format
Model to work correctly requires normal state of Apache2 server logs in right format. \
Log format sample:
```
"11/Apr/2020/10:13:18" "192.168.10.61" "200" "12" "157" "GET" "/index.html/?hello" "HTTP/1.1"
```
### Log format: Apache2 access.log formatting
Simplest way to use Apache2 logs in Machine learning model is to reformat logs directly from Apache2. Open settings file from /etc/apache2/apache2.conf, log formats for access.log and other_vhost_access.log are located on lines 212-213 change it to mach new format as show in picture below.
\
![Log formats](./img/install_pic_1.png)
\
A) /var/log/apache2/other_vhosts_access.log – These logs are used for virtual host page. </p> 
B) /var/log/apache2/access.log – These are for Apache2 default page logs.
\
Log formats:
```
LogFormat "\"%{%d/%b/%Y/%T}t\" \"%h\" \"%>s\" \"%B\" \"%D\" \"%m\" \"%U/%q\" \"%H\"" vhost_combined
LogFormat "\"%{%d/%b/%Y/%T}t\" \"%h\" \"%>s\" \"%B\" \"%D\" \"%m\" \"%U/%q\" \"%H\"" combined
```
Log tags explained:
```
%{%d/%b/%Y/%T}t = Time stamp
%h = IP address
%>s = Status code
%B = Bytes sent
%D = Request time taken
%m = Method
%U%q = Path and query
%H = Protocol
```

# Local installation

First Install Python3.
```
sudo apt-get install python3
```
This part might take a while since Tensorflow packets are quite big. \
Pip3 install Tensorflow, Pandas, Scikit-Learn and Matplotlib.
```
pip3 install tensorflow pandas scikit-learn matplotlib
```
Install git
```
sudo apt-get install git
```
Clone project folder.
```
git clone https://github.com/Dunttus/AI-Project.git
```
### Local: Make dataset
Manually combine all access.logs to 1 file or use combine_apachelogs.sh Bash script with AI-Project main folder as shown below.
```
cp -rp combine_apachelogs.sh ../
```
```
cd ..
```
```
bash ./combine_apachelogs.sh
```
File for model training "train_access.log" is now located in /AI-Project/datasets/training_dataset/ and should look similar to this test file https://github.com/Dunttus/AI-Project/blob/master/datasets/public/good_access.log \
\
**Skip to "Local: Train model" if you used combine_apachelogs.sh** \
If you wan't to use different folder folder structure you can change Bash script variables manually to absolute paths in DATASAVING FOLDER and ACCESS.LOG LOCATION or by making dataset manually with Linux commands.
```
#!/bin/bash
folderdata=DATASAVING FOLDER
folderlog=APACHE2 ACCESS.LOG LOCATION

cp $folderlog/access.log.* $folderdata
gunzip $folderdata/access.log.*
cat $folderdata/access.log.* > $folderdata/train_access.log
rm $folderdata/access.log.*
```
### Local: Train model
Using Tensorflow in GPU mode requires local Nvidia drivers and CUDA installation, else it will train model with CPU by default. CUDA supported GPU can be found in NVIDIAs site https://developer.nvidia.com/cuda-gpus. \
\
Next navigate to settings file in /AI-Project/config.py and edit TRAINING_DATA = "datasets/training_dataset/train_access.log" to mach your new log file.
Then just run /AI-Project/train.py with Python3
```
python3 ./train.py
```
### Local: Using trained model
After training your model to use it chance what log you want to monitor in /AI-Project/config.py file edit MONITORED_LOG = "/var/log/access.log". Start monitoring access.log by running main.py with Python3.
```
python3 ./main.py
```
Now machine learning model is monitoring your Apache2 log anomalies. Simplest way to put program to run in foreground is CTRL+Z and to return it just type command fg. Monitoring can be stopped with CTRL+C.
  
  
# Docker installation
### Docker: Latest version of Docker
Dockers latest version installation from [docker.com](https://docs.docker.com/engine/install/ubuntu/). \
If you have old docker installations “docker, docker-engine, docker.io, containerd and runc” they need to be uninstalled and Linux version info updated with “sudo apt-get update“.
\
First we need to allow apt to install packages via HTTPS (requires CURL):
```
sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common
```
Add Docker GPG-key to apt installation.
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Adds docker.com custom packages to apt’s package management.
```
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \ stable"
```
Updates Linux version information.
```
sudo apt-get update
```
Installs docker-ce docker-ce-cli ja containerd.io packages.
```
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```
Check version information of Docker.
```
docker --version
```
### Project container setup and files

Install git
```
sudo apt-get install git
```
Clone project folder.
```
git clone https://github.com/Dunttus/AI-Project.git
```

Navigate to folder with Dockerfile /AI-Project/docker/ and build image from Dockerfile.
```
sudo docker build -t lokari:test .
```

### Docker: Make dataset
We will make all preparations for files in local computer as we will import them to 1-time use Docker container in dynamical mode.
Manually combine all access.logs to 1 file or use combine_apachelogs.sh Bash script with AI-Project main folder as shown below.
```
cp -rp combine_apachelogs.sh ../
```
```
cd ..
```
```
sudo bash ./combine_apachelogs.sh
```
File for model training "train_access.log" is now located in /AI-Project/datasets/training_dataset/ and should look similar to this test file https://github.com/Dunttus/AI-Project/blob/master/datasets/public/good_access.log \
\
**Skip to "Local: Train model" if you used combine_apachelogs.sh** \
If you wan't to use different folder folder structure you can change Bash script variables manually to absolute paths in DATASAVING FOLDER and ACCESS.LOG LOCATION or by making dataset manually with Linux commands.
```
#!/bin/bash
folderdata=DATASAVING FOLDER
folderlog=APACHE2 ACCESS.LOG LOCATION

cp $folderlog/access.log.* $folderdata
gunzip $folderdata/access.log.*
cat $folderdata/access.log.* > $folderdata/train_access.log
rm $folderdata/access.log.*
```

### Docker: Training model
Navigate to settings file in local computer /AI-Project/config.py and edit TRAINING_DATA = "datasets/training_dataset/train_access.log" to mach your new log file.
Make sure config file is pointing at correct directories. \
Contrainer run train.py inside container, removed when exit or done, with local AI-Project and Apache2 log folders dynamically, replace USER in command to mach your directory structure:
```
sudo docker run -it --rm -v /home/USER/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ -w /AI-Project lokari:test python3 ./train.py
```
Stop container with CTRL+C.

### Docker: Using model
After training your model to use it chance what log you want to monitor in local computer file /AI-Project/config.py edit MONITORED_LOG = "/var/log/access.log". Start monitoring access.log by running main.py in container with Python3.
Contrainer run main.py inside container, removed when exit or done, with local AI-Project and Apache2 log folders dynamically, replace USER in command to mach your directory structure:
```
sudo docker run -it --rm -v /home/USER/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ -w /AI-Project lokari:test python3 ./main.py
```
Stop container with CTRL+C.

### Docker: Monitoring main.py container in foreground
Contrainer run main.py inside container, removed when exit or done, with local AI-Project and Apache2 log folders dynamically, replace USER in command to mach your directory structure:
```
sudo docker run -d --rm -v /home/USER/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ -w /AI-Project lokari:test python3 ./main.py
```

**WARNING COMMAND BELOW MAKES DYNAMICAL COPY OF LOCAL FOLDERS IN CONTAINER DO NOT EDIT ANYTHING INSIDE CONTAINER AS ITS RUN AS ROOT.** \
Docker command for debugging. Open docker container with Bash, removed when exit, copy local Github folder and Apache access.logs, replace USER in command to mach your directory structure:  
```
sudo docker run --rm -v /home/USER/AI-Project/:/AI-Project -v /var/log/apache2:/var/log/apache2/ -it lokari:test
```

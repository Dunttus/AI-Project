```
sudo docker build -t lokari:testpy .
```
```
sudo docker run -d -i --rm -v /home/USER/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ lokari:testpy
```
```
docker run -it --rm -v /home/USER/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ lokari:testpy
```

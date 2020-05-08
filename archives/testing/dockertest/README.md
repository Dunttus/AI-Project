Build
```
sudo docker build -t lokari:testpy .
```

Not working with current imports
```
docker run -it --rm -v /home/USER/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ lokari:testpy
```

Working directory /AI-Project to main.py to work + input mode
```
docker run -it --rm -v /home/joni/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ -w /AI-Project lokari:testpy
```

Working directory /AI-Project to main.py to work + foreground
```
docker run -d --rm -v /home/joni/AI-Project/:/AI-Project/ -v /var/log/apache2:/var/log/apache2/ -w /AI-Project lokari:testpy
```

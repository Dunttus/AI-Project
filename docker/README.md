# Project container setup and files

PyCharm recognizes this automatically. Set project interpreter point to
this container to have all the libraries in use.

The container image needs to be rebuilt if updates occur.

Build the container:  
$ docker build -t lokari:test .

Start the container in interactive mode:  
$ docker run --name lokaritest -it lokari:test

Docker container in Bash, with Github project folder and auto removed on exit:
docker run --rm -v /home/USERNAME/AI-Project/:/AI-Project -it lokari:test

## Environment
![Environment picture](./img/environment.PNG)

# Project container setup and files

Build the container:  
$ docker build -t lokari:test .

Start the container in interactive mode:  
$ docker run --name lokaritest -it lokari:test

...adding python packages for the remote interpreter

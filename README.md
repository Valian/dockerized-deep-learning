# Dockerized deep learning

This repository contains code to run already trained, dockerized Deep Convolutional Network. Article describing whole process can be found [here](https://rock-it.pl/how-to-reuse-keras-deep-neural-network/).

## Installing Docker

General installation instructions are
[on the Docker site](https://docs.docker.com/installation/), here are some quick links:

* [OSX](https://docs.docker.com/installation/mac/): [docker toolbox](https://www.docker.com/toolbox)
* [ubuntu](https://docs.docker.com/installation/ubuntulinux/)


## Running the container

We are using `Makefile` to simplify docker commands within make commands.

Firstly, insert images compatible with CIFAR10 dataset into `data` directory.

Next, build the container

    $ make build
    
and run classifier

    $ make predict

It will find all images under `/data` directory and classify them. Optionally, you can pass list of
images to classify (glob patterns supported):
    
    $ make classify IMAGES="airplane*.png deer4.png"
    
Raw commands can be found inside `Makefile`. Example without make:

    $ docker run -it --rm -v $PWD/data:/srv/data cifar python predict.py
    
## Licence

MIT

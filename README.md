# Dockerized image classifier

This repository contains code to run already trained, dockerized Deep Convolutional Network.

## Installing Docker

General installation instructions are
[on the Docker site](https://docs.docker.com/installation/), but we give some
quick links here:

* [OSX](https://docs.docker.com/installation/mac/): [docker toolbox](https://www.docker.com/toolbox)
* [ubuntu](https://docs.docker.com/installation/ubuntulinux/)


## Running the container

We are using `Makefile` to simplify docker commands within make commands.

Firstly, insert images into `images` directory.

Next, build the container

    $ make build
    
and run classifier

    $ make classify

It will find all images under `/images` directory and classify them. Optionally, you can pass list of
images to classify:
    
    $ make classify IMAGES="positive/142.jpg positive/144.jpg"
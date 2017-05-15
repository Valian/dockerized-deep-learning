help:
	@cat Makefile

DATA?=${PWD}/data
SRC?=${PWD}

build:
	docker build -t cifar .

predict:
	docker run -it --rm -v ${DATA}:/srv/data cifar python -W ignore predict.py $(IMAGES)

clear:
	rm model.h5 || echo "No previous model"

learn:
	docker run -it --rm -v ${SRC}:/srv cifar python -W ignore learn.py

bash:
	docker run -it --rm -v ${SRC}:/srv cifar /bin/bash

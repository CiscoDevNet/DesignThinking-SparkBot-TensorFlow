FROM python:2.7.13-jessie

RUN apt-get install -y git wget
RUN pip install tensorflow
RUN git clone --depth=1 https://github.com/tensorflow/models.git
RUN mkdir /tmp/imagenet && cd /tmp/imagenet && wget http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz
WORKDIR /models/tutorials/image/imagenet

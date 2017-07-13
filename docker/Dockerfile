FROM ubuntu:16.04

# ========== Anaconda ==========
# https://github.com/ContinuumIO/docker-images/blob/master/anaconda/Dockerfile
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion 

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget  --no-check-certificate --quiet https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

RUN apt-get install -y unzip curl grep sed dpkg && apt-get clean
RUN apt-get -y install git make cmake unzip zlib1g-dev libjpeg-dev xvfb \
    libav-tools xorg-dev libboost-all-dev libsdl2-dev swig
# ALE requires zlib
# MUJOCO requires graphics stuff (Why?)
RUN apt-get -y build-dep glfw
RUN apt-get -y install libxrandr2 libxinerama-dev libxi6 libxcursor-dev

ENV PATH /opt/conda/bin:$PATH

CMD mkdir /root/code
ADD environment.yml /root/code/environment.yml
RUN conda env create -f /root/code/environment.yml

RUN echo "source activate aibs" >> /root/.bashrc
ENV BASH_ENV /root/.bashrc
WORKDIR /root/code

# OpenAI Gym
RUN pip install rllab[all] baselines

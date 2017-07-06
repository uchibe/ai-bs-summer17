FROM ubuntu:14.04

#--------------------
# General setup
#--------------------

# Get the dependencies
RUN apt-get update \
    && apt-get install -y xorg-dev \
    libgl1-mesa-dev \
    xvfb \
    libxinerama1 \
    libxcursor1 \
    unzip \
    libglu1-mesa \
    libav-tools \
    python-numpy \
    python-dev \
    python-scipy \
    python-matplotlib \
    python-opengl \
    python-pyglet \
    python-setuptools \
    libboost-all-dev \
    zlib1g-dev \
    libsdl2-dev \
    libpq-dev \
    libjpeg-dev \
    cmake \
    curl \
    git \
    swig \
    wget \
    xpra \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && easy_install pip

#--------------------
# Install gym
#--------------------
RUN pip install --upgrade pip
RUN pip install 'gym[all]'


#--------------------
# Install ROS
#--------------------
# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list

# setup keys
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    ros-indigo-desktop-full \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init \
    && rosdep update

#
RUN echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc
ENV BASH_ENV ~/.bashrc

#--------------------
# Install Deep Learning
#--------------------
RUN pip install h5py
RUN apt-get update && apt-get install --no-install-recommends -y \
    gfortran \
    python-skimage

CMD mkdir /root/code
WORKDIR /root/code

# A Dockerfile for the gym-gazebo environment
FROM ubuntu:14.04

############################################
# General setup
############################################
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
    python-scipy \
    python-pyglet \
    python-setuptools \
    libpq-dev \
    libjpeg-dev \
    wget \
    curl \
    cmake \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && easy_install pip

############################################
# OpenAI Gym
############################################
RUN apt-get update \
    && apt-get install -y swig
RUN pip install gym[all]

############################################
# ROS
############################################
# setup environment
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# setup keys
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init \
    && rosdep update

# install ros packages
ENV ROS_DISTRO indigo
RUN apt-get update && apt-get install -y \
    ros-indigo-desktop-full \
    && rm -rf /var/lib/apt/lists/*

############################################
# Gazebo
############################################
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

RUN wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -

RUN apt-get update
RUN apt-get purge gazebo2 -y
RUN apt-get install gazebo7 libgazebo7-dev -y

# setup environment
EXPOSE 11345

# Install additional dependencies
RUN apt-get install -y ros-indigo-cv-bridge
RUN apt-get install -y ros-indigo-robot-state-publisher

############################################
# Theano and Keras
############################################
RUN pip install h5py
RUN apt-get install gfortran -y
RUN pip install Theano keras
ENV KERAS_BACKEND=theano


############################################
# Gym-Gazebo
############################################
RUN apt-get update \
    && apt-get install -y git \
    mercurial \
    libsdl-image1.2-dev \
    libspnav-dev \
    libtbb-dev \
    libtbb2 \
    libusb-dev libftdi-dev \
    pyqt4-dev-tools \
    python-vcstool \
    ros-indigo-bfl \
    python-pip \
    g++ \
    ccache \
    realpath \
    libopencv-dev \
    libtool \
    automake autoconf \
    libexpat1-dev \
    ros-indigo-mavlink \
    ros-indigo-octomap-msgs \
    ros-indigo-joy \
    ros-indigo-geodesy \
    ros-indigo-octomap-ros \
    ros-indigo-control-toolbox \
    ros-indigo-pluginlib \
    ros-indigo-trajectory-msgs \
    ros-indigo-control-msgs \
    ros-indigo-std-srvs \
    ros-indigo-nodelet \
    ros-indigo-urdf \
    ros-indigo-rviz \
    ros-indigo-kdl-conversions \
    ros-indigo-eigen-conversions \
    ros-indigo-tf2-sensor-msgs \
    ros-indigo-pcl-ros \
    gawk \
    libtinyxml2-dev
RUN easy_install numpy
#RUN easy_install --upgrade numpy
#RUN pip install --upgrade matplotlib
RUN pip2 install pymavlink MAVProxy catkin_pkg --upgrade

# Install Sophus
WORKDIR /tmp
RUN git clone --depth 1 https://github.com/stonier/sophus -b indigo \
    && mkdir -p sophus/build \
    && cd sophus/build \
    && cmake .. \
    && make \
    && make install

# Install APM/Ardupilot
WORKDIR /tmp
RUN mkdir apm \
    && cd apm \
    && git clone --depth 1 https://github.com/erlerobot/ardupilot.git -b gazebo_udp \
    && git clone --depth 1 https://github.com/tridge/jsbsim.git \
    && cd jsbsim \
    && ./autogen.sh --enable-libraries \
    && make -j2 \
    && make install

RUN git clone --depth 1 https://github.com/erlerobot/gym-gazebo.git \
    && cd gym-gazebo \
    && pip install -e .

# Install dependencies
RUN apt-get install libbluetooth-dev libcwiid1 libcwiid-dev lswm wmgui wminput -y
ADD docker/gazebo.repos /tmp/gazebo.repos
RUN adduser docker
ENV HOME /home/docker
RUN echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc
ENV BASH_ENV /opt/ros/indigo/setup.bash
RUN /bin/bash -c "mkdir -p /home/docker/catkin_ws/src \
    && cd /home/docker/catkin_ws/src \
    && catkin_init_workspace \
    && cd .. \
    && catkin_make"
WORKDIR /home/docker/catkin_ws/src
RUN vcs import < /tmp/gazebo.repos
RUN /bin/bash -c "cd /home/docker/catkin_ws \
    && catkin_make --pkg mav_msgs \
    && source devel/setup.bash \
    && catkin_make -j 1"

# 
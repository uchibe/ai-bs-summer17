#!/bin/bash

#docker build --force-rm=true -t aibs/cpu:1.0 -f docker/Dockerfile .
#docker run -it --init --net=host --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
#  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/code:rw \
#  aibs/cpu:1.0 /bin/bash

#docker build --force-rm=true -t aibs/ros_cpu:1.0 -f docker/rs_Dockerfile .
docker run -it --init --net=host --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/code:rw \
  aibs/ros_cpu:1.0 /bin/bash

#docker run -it --init --net=host --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
#  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/code:rw \
#  erlerobotics/gym-gazebo:latest /bin/bash


#nvidia-docker build --force-rm=true -t aibs/gpu:1.0 -f docker/gpu_Dockerfile .
#nvidia-docker run -it --init --net=host --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
#  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/code:rw \
#  aibs/gpu:1.0 /bin/bash

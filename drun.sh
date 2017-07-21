#!/bin/bash

export PROJECT_NAME="ai-bs-summer17"

#docker build --force-rm=true -t uchibe/cpu:1.0 -f docker/Dockerfile .
#docker run -it --init --net=host --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
#  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/ai-bs-summer17:rw \
#  uchibe/cpu:1.0 /bin/bash

#docker build --force-rm=true -t uchibe/aibs_ros_cpu:1.0 -f docker/Dockerfile .
#       --user=$(id -u):$(id -g) \
#       --workdir="/home/$USER" \
#      --volume="/etc/group:/etc/group:ro" \
#       --volume="/etc/passwd:/etc/passwd:ro" \
#       --volume="/etc/shadow:/etc/shadow:ro" \
#       --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
docker run -it --init --net=host --env="DISPLAY" \
       --env="QT_X11_NO_MITSHM=1" \
       --volume="${PWD}:/home/$USER/$PROJECT_NAME" \
       --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
       --volume="/etc/machine-id:/etc/machine-id:ro" \
       --volume="/var/run/dbus:/var/run/dbus" \
       --volume="/home/$USER/.Xauthority:/home/$USER/.Xauthority" \
       uchibe/aibs_ros_cpu:1.0 /bin/bash

#docker run -it --init --net=host --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
#  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/ai-bs-summer17:rw \
#  erlerobotics/gym-gazebo:latest /bin/bash


#nvidia-docker build --force-rm=true -t uchibe/gpu:1.0 -f docker/gpu_Dockerfile .
#nvidia-docker run -it --init --net=host --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
#  -v ~/.Xauthority:/root/.Xauthority -v ${PWD}:/root/ai-bs-summer17:rw \
#  uchibe/gpu:1.0 /bin/bash

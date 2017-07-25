#!/usr/bin/env bash
# This script is based on https://github.com/jbohren/rosdocked

# Check args
if [ "$#" -ne 1 ]; then
    echo "Usage: ./build.sh PROJECT"
    exit 1
fi

if [ $1 = "indigo_cpu" ]; then
    IMAGE_NAME="uchibe/indigo_cpu:1.0"
elif [ $1 = "kinetic_cpu" ]; then
    IMAGE_NAME="uchibe/kinetic_cpu:1.0"
elif [ $1 = "roboschool_cpu" ]; then
    IMAGE_NAME="uchibe/roboschool_cpu:1.0"
else
    echo "Invalid PROJECT"
    exit 1
fi

# Get the script's path
pushd `dirname $0` > /dev/null
SCRIPT_PATH=`pwd`
popd > /dev/null

PROJECT_NAME="ai-bs-summer17"

# Run the container with shared X11
#     -v $HOME/.Xauthority:$HOME/.Xauthority" \
#     --user=$(id -u):$(id -g) \
docker run --init --net=host \
     --env="DISPLAY" \
     --env="QT_X11_NO_MITSHM=1" \
     --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
     --volume="/etc/machine-id:/etc/machine-id:ro" \
     --volume="/var/run/dbus:/var/run/dbus" \
     -v ${HOME}/.Xauthority:/root/.Xauthority \
     -v ${PWD}:/root/$PROJECT_NAME \
     -it $IMAGE_NAME /bin/bash

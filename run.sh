#!/usr/bin/env bash
# This script is based on https://github.com/jbohren/rosdocked

# Check args
if [ "$#" -ne 1 ]; then
    echo "Usage: ./run.sh PROJECT"
    exit 1
fi

if [ $1 = "ros_cpu" ]; then
    DOCKER_COMMAND="docker"
    IMAGE_NAME="uchibe/ros_cpu"
    NAME="ros_cpu"
elif [ $1 = "roboschool_cpu" ]; then
    DOCKER_COMMAND="docker"
    IMAGE_NAME="uchibe/roboschool_cpu"
    NAME="roboschool_cpu"
elif [ $1 = "roboschool_gpu" ]; then
    DOCKER_COMMAND="nvidia-docker"
    IMAGE_NAME="uchibe/roboschool_gpu"
    NAME="roboschool_gpu"
else
    echo "Invalid PROJECT"
    exit 1
fi

# Get the script's path
pushd `dirname $0` > /dev/null
SCRIPT_PATH=`pwd`
popd > /dev/null

PROJECT_NAME="ai-bs-summer17"

# Run the container
#
# At first, you should do
# $ xhost+
# 
#
#
# If you use the Intel driver, you need to expose the /dev/dri
# to the docker container.
#
# See also http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration
#
$DOCKER_COMMAND run --init --net=host \
     --env="DISPLAY" \
     --env="QT_X11_NO_MITSHM=1" \
     --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
     --volume="/etc/machine-id:/etc/machine-id:ro" \
     --volume="/var/run/dbus:/var/run/dbus" \
     --device="/dev/dri:/dev/dri" \
     -v ${HOME}/.Xauthority:/root/.Xauthority \
     -v /tmp/.gazebo/:/root/.gazebo/ \
     -v ${PWD}:/root/$PROJECT_NAME \
     --name $NAME -it $IMAGE_NAME bash

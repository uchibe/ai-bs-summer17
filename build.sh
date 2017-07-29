#!/usr/bin/env bash
# This script is based on https://github.com/jbohren/rosdocked

# Check args
if [ "$#" -ne 1 ]; then
    echo "Usage: ./build.sh PROJECT"
    exit 1
fi

if [ $1 = "ros_cpu" ]; then
    DOCKER_COMMAND="docker"
    IMAGE_NAME="uchibe/ros_cpu"
    DOCKER_FILE="docker/kinetic_Dockerfile"
elif [ $1 = "roboschool_cpu" ]; then
    DOCKER_COMMAND="docker"
    IMAGE_NAME="uchibe/roboschool_cpu"
    DOCKER_FILE="docker/rs_Dockerfile"
elif [ $1 = "roboschool_gpu" ]; then
    DOCKER_COMMAND="nvidia-docker"
    IMAGE_NAME="uchibe/roboschool_gpu"
    DOCKER_FILE="docker/rs_gpu_Dockerfile"
else
    echo "Invalid PROJECT"
    exit 1
fi

# Get the script's path
pushd `dirname $0` > /dev/null
SCRIPT_PATH=`pwd`
popd > /dev/null

# Build the docker image
# --build-arg user=$USER \
# --build-arg uid=$UID \
# --build-arg home=$HOME \
# --build-arg workspace=$SCRIPT_PATH \
$DOCKER_COMMAND build --force-rm=true \
     -t $IMAGE_NAME -f $DOCKER_FILE .

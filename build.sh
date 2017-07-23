#!/usr/bin/env bash
# This script is based on https://github.com/jbohren/rosdocked

# Check args
if [ "$#" -ne 1 ]; then
    echo "Usage: ./build.sh PROJECT"
    exit 1
fi

if [ $1 = "ros_cpu" ]; then
    IMAGE_NAME="uchibe/aibs_ros_cpu:1.0"
    DOCKER_FILE="docker/Dockerfile"
elif [ $1 = "roboschool_cpu" ]; then
    IMAGE_NAME="uchibe/aibs_roboschool_cpu:1.0"
    DOCKER_FILE="docker/rs_Dockerfile"
else
    echo "Invalid PROJECT"
    exit 1
fi

# Get the script's path
pushd `dirname $0` > /dev/null
SCRIPT_PATH=`pwd`
popd > /dev/null

echo $SCRIPT_PATH
echo $IMAGE_NAME
echo $DOCKER_FILE

# Build the docker image
# --build-arg user=$USER \
# --build-arg uid=$UID \
# --build-arg home=$HOME \
# --build-arg workspace=$SCRIPT_PATH \
docker build --force-rm=true \
     -t $IMAGE_NAME -f $DOCKER_FILE .

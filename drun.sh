#!/bin/bash

#docker build -t aibs/cpu:1.0 -f docker/Dockerfile .
docker run -it --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  aibs/cpu:1.0 /bin/bash

#docker run -it --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v ${PWD}:/root/code:rw \
#  ai/cpu:1.0 /bin/bash


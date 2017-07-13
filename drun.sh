#!/bin/bash

#docker build --force-rm=true -t aibs/cpu:1.0 -f docker/Dockerfile .
docker run -it --init --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v /etc/machine-id:/etc/machine-id:ro -v /var/run/dbus:/var/run/dbus \
  -v ${PWD}:/root/code:rw \
  aibs/cpu:1.0 /bin/bash

#docker run -it --env="DISPLAY" \
#  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
#  -v ${PWD}:/root/code:rw \
#  ai/cpu:1.0 /bin/bash


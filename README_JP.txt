提供されたDockerコンテナを使う
docker pull erlerobotics/gym-gazebo:latest

docker run -it --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  erlerobotics/gym-gazebo

xvfb-run -s "-screen 0 1400x900x24" bash

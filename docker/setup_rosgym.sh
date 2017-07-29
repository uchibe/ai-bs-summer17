source /opt/ros/${ROS_DISTRO}/setup.bash
source /usr/share/gazebo/setup.sh

MY_CATKIN_WS_DIR=${HOME}/catkin_ws
source ${MY_CATKIN_WS_DIR}/devel/setup.bash

MY_PYTHON_PACKAGE_DIR=${MY_CATKIN_WS_DIR}/src/myturtle_gazebo
export PYTHONPATH=$MY_PYTHON_PACKAGE_DIR:$PYTHONPATH

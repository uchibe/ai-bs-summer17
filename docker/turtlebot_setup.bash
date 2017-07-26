#!/usr/bin/env bash
# set environmental variables

export GAZEBO_MODEL_PATH=/opt/gym-gazebo/gym_gazebo/envs/assets/models

export GYM_GAZEBO_WORLD_PATH=/opt/gym-gazebo/gym_gazebo/envs/assets/worlds
export GYM_GAZEBO_WORLD_MAZE=${GYM_GAZEBO_WORLD_PATH}/maze.world
export GYM_GAZEBO_WORLD_CIRCUIT=${GYM_GAZEBO_WORLD_PATH}/circuit.world
export GYM_GAZEBO_WORLD_CIRCUIT2=${GYM_GAZEBO_WORLD_PATH}/circuit2.world
export GYM_GAZEBO_WORLD_CIRCUIT2C=${GYM_GAZEBO_WORLD_PATH}/circuit2c.world
export GYM_GAZEBO_WORLD_ROUND=${GYM_GAZEBO_WORLD_PATH}/round.world

# Exports
source ~/catkin_ws/devel/setup.bash
export TURTLEBOT_GAZEBO_MAP_FILE=`rospack find turtlebot_gazebo`/maps/playground.yaml
export TURTLEBOT_GAZEBO_WORLD_FILE=`rospack find turtlebot_gazebo`/worlds/playground.world

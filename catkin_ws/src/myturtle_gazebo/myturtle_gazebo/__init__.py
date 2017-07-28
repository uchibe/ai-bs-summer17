import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gazebo
# ----------------------------------------

# Turtlebot envs

register(
    id='Circuit2TurtlebotLidar-v0',
    entry_point='myturtle_gazebo.envs:Circuit2TurtlebotLidarEnv',
    # More arguments here
)

register(
    id='Circuit2cTurtlebotCameraNn-v0',
    entry_point='myturtle_gazebo.envs:Circuit2cTurtlebotCameraNnEnv', 
    # More arguments here
)

register(
    id='SimplemazeTurtlebotCameraNn-v0',
    entry_point='myturtle_gazebo.envs:SimplemazeTurtlebotCameraNnEnv', 
    # More arguments here
)

register(
    id='SimplemazeTurtlebotCameraCvNn-v0',
    entry_point='myturtle_gazebo.envs:SimplemazeTurtlebotCameraCvNnEnv', 
    # More arguments here
)

register(
    id='SimplemazeTurtlebotCameraCvNnMp-v0',
    entry_point='myturtle_gazebo.envs:SimplemazeTurtlebotCameraCvNnEnvMp', 
    # More arguments here
)
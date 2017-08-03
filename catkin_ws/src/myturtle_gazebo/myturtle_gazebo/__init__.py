import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gazebo
# ----------------------------------------

# Turtlebot envs

register(
    id='SimplemazeTurtlebotCameraCvNn-v0',
    entry_point='myturtle_gazebo.envs:SimplemazeTurtlebotCameraCvNnEnv', 
    # More arguments here
)


"""
Docs on how to do the markdown formatting:
http://docutils.sourceforge.net/docs/user/rst/quickref.html

Tool for previewing the markdown:
http://rst.ninjs.org/
"""

import os

from gym.scoreboard.registration import registry, add_task, add_group

# Discover API key from the environment. (You should never have to
# change api_base / web_base.)
'''api_key = os.environ.get('OPENAI_GYM_API_KEY')
api_base = os.environ.get('OPENAI_GYM_API_BASE', 'https://gym-api.openai.com')
web_base = os.environ.get('OPENAI_GYM_WEB_BASE', 'https://gym.openai.com')'''

# The following controls how various tasks appear on the
# scoreboard. These registrations can differ from what's registered in
# this repository.

# groups

add_group(
    id='gazebo',
    name='Gazebo',
    description='TODO.'
)


add_task(
    id='Circuit2TurtlebotLidar-v0',
    group='gazebo',
    summary='Obstacle avoidance in a Circuit 2.',
)

add_task(
    id='Circuit2cTurtlebotCameraNn-v0',
    group='gazebo',
    summary='Obstacle avoidance in a Circuit 2.c',
)

add_task(
    id='SimplemazeTurtlebotCameraNn-v0',
    group='gazebo',
    summary='Obstacle avoidance in a Simplemaze',
)

add_task(
    id='SimplemazeTurtlebotCameraCvNn-v0',
    group='gazebo',
    summary='Approaching a target in a Simplemaze',
)

add_task(
    id='SimplemazeTurtlebotCameraCvNnMp-v0',
    group='gazebo',
    summary='Approaching a target in a Simplemaze using maxpain',
)

registry.finalize()

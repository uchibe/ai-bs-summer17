# Roboschool
[OpenAI Roboschool](https://github.com/openai/roboschool) tries to replicate Gym [MuJoCo](http://www.mujoco.org/) environments. Note that student licenses of MuJoCo are now free.

Pretrained model
```sh
python3 $ROBOSCHOOL_PATH/agent_zoo/RoboschoolHumanoidFlagrun_v1_2017jul.py
```

```sh
python3 $ROBOSCHOOL_PATH/agent_zoo/demo_race2.py
```

```sh
python3 train_a3c_gym.py 4 --env RoboschoolInvertedPendulum-v1
```

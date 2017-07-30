# Roboschool
[OpenAI Roboschool](https://github.com/openai/roboschool) tries to replicate Gym [MuJoCo](http://www.mujoco.org/) environments. Note that student licenses of MuJoCo are now free.

```sh
uchibe@x260:ai-bs-summer17$ ./run roboschool_cpu
root@x260:~# cd ai-bs-summer17/roboschool
```
Note that uchibe and x260 are my username and hostname, respectively.

Pretrained model
```sh
root@x260:roboschool# python3 $ROBOSCHOOL_PATH/agent_zoo/RoboschoolHumanoidFlagrun_v1_2017jul.py
```

```sh
root@x260:roboschool# python3 $ROBOSCHOOL_PATH/agent_zoo/demo_race2.py
```

```sh
root@x260:roboschool# python3 train_a3c_gym.py 8 --env RoboschoolInvertedPendulum-v1 --arch LSTMGaussian --t-max 50
root@x260:roboschool# python3 train_ddpg_gym.py
```

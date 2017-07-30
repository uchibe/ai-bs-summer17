# AI-BS Summer School 2017
[AI-BS Summer School 2017](http://www.brain-ai.jp/jp/summer_school2017/)  is to provide opportunities for young researchers to meet each other and learn recent studies in the field of Artificial Intelligence and Brain Science. In particular, this project gives you to enjoy deep reinforcement learning for robot control. 

## ROS and OpenAI Gym
```sh
~$ git clone https://github.com/uchibe/ai-bs-summer17.git
$ cd ai-bs-summer17
ai-bs-summer17$ ./run ros_cpu
```

## Roboschool

Pretrained model
```sh
python3 $ROBOSCHOOL_PATH/agent_zoo/RoboschoolHumanoidFlagrun_v1_2017jul.py
```

```sh
python3 $ROBOSCHOOL_PATH/agent_zoo/demo_race2.py
```

### Baselines
[OpenAI Baselines](https://blog.openai.com/openai-baselines-dqn/) is a set of implementations of reinforcement algorithms. In the container, use python3 to run the sample prorams as follows: 
```sh
$ python3 -m baselines.deepq.experiments.train_cartpole
```
Load the model saved in cartpole_model.pkl and visualize the learned policy
```
python3 -m baselines.deepq.experiments.enjoy_cartpole
```
```
python3 -m baselines.deepq.experiments.train_pong
```
```
python3 -m baselines.deepq.experiments.enjoy_pong
```

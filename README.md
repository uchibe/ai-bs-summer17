# ai-bs-summer17
AI-BS Summer School 2017

# Train model and save the results to cartpole_model.pkl
python3 -m baselines.deepq.experiments.train_cartpole

# Load the model saved in cartpole_model.pkl and visualize the learned policy
python3 -m baselines.deepq.experiments.enjoy_cartpole

python3 -m baselines.deepq.experiments.train_pong

python3 -m baselines.deepq.experiments.enjoy_pong

python3 $ROBOSCHOOL_PATH/agent_zoo/RoboschoolHumanoidFlagrun_v0_2017may.py
python3 $ROBOSCHOOL_PATH/agent_zoo/demo_race2.py

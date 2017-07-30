uchibe@host:ai-bs-summer17$ ./run.sh ros_cpu
root@host:~# 
root@host:~# roslaunch myturtle_gazebo myturtle_simplemaze_brick.launch

root@host:~# roslaunch myturtle_gazebo myturtle_simplemaze_brick.launch gui:=true

If you installed gazebo version 7.8.1 to the host computer, you can see the screen as follows:
uchibe@host:ai-bs-summer17$ gzclient

uchibe@host:ai-bs-summer17$ docker exec -it ros_cpu bash
root@host:~# gzclient

uchibe@host:ai-bs-summer17$ docker exec -it ros_cpu bash
root@host:~# cd catkin_ws/src/myturtle_gazebo/scripts
root@host:scripts# python test_simplemaze_cvenv.py

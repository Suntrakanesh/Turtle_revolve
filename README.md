# Turtle_revolve

Turtle sim revolve is the basic exercise in **ROS**. Every beginners should practise this code to understand the basic concept of **ROS**. This repository helps to do such a exercise, and our target is to revolve the turtle in circular path. For that, we need to build our catkin workspace as well as necessary folders. 

## The complete instruction of pre-requirements as follows :

1. First, create a package named `pkg_task0` , within your catkin workspace. Once done, compile and source the packages.
``` cd ~/catkin_ws
catkin build
source devel/setup.bash
```
2. Within this package, you should have a `scripts` folder inside which you'll create a python script, named `node_turtle_revolve.py`. It is available in this repository you can download on your system.

3. Run this command to make as executable file 
`chmod +x ~/catkin_ws/src/pkg_task0/scripts/node_turtle_revolve.py`

4. Before executing make sure that `roscore` is running along with `turtlesim_node`. You can either run them in separate terminals or simply create a `task0.launch` file inside the `~/catkin_ws/src/pkg_task0/launch/ folder`. Launch file can run multiple nodes unlike a python/cpp script. Run the launch file, enter,
`roslaunch pkg_task0 task0.launch`


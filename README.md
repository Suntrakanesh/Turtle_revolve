# Turtle_revolve

Turtle sim revolve is the basic exercise in **ROS**. Every beginners should practise this code to understand the basic concept of **ROS**. This repository helps to do such a exercise, and our target is to revolve the turtle in circular path. For that, we need to build our catkin workspace as well as necessary folders. 

## The complete instruction of pre-requirements as follows :

- First, create a package named `pkg_task0` , within your catkin workspace. Once done, compile and source the packages.
 ``` cd ~/catkin_ws
catkin build
source devel/setup.bash
 ```
- Within this package, you should have a `scripts` folder inside which you'll create a python script, named `node_turtle_revolve.py`. It is available in this repository you can download on your system.

- Run this command to make as executable file<br/>
```chmod +x ~/catkin_ws/src/pkg_task0/scripts/node_turtle_revolve.py```

- Before executing make sure that `roscore` is running along with `turtlesim_node`. You can either run them in separate terminals or simply create a `task0.launch` file inside the `~/catkin_ws/src/pkg_task0/launch/ folder`. Launch file can run multiple nodes unlike a python/cpp script. Run the launch file, enter,<br/>
`roslaunch pkg_task0 task0.launch`

## Recording Logs

- ROS allows us to record a log of the messages that occurred in a given time period. This is like recording a data stream. The ROS utility which does this is called rosbag, and the command to capture the data is `rosbag record`.

- Create a folder called bag_files in your package as a save destination for the bag files.

- You can run the `rosbag record` command separately on the command line. But to not loose any data you will have to start recording precisely at the same moment your turtle starts moving. Hence it is a much more preferable option to include the rosbag recording in your launch file itself. We have included rosbag recording in the launch file. You can find it in the name of `task0.launch`.

- Use this command to launch the entire package<br/>
`roslaunch pkg_task0 task0.launch record:=true rec_name:=my_turtle.bag`

- Thus using these parameters along with your launch file will record a bag file of appropriate duration.

- After the recording duration, the message: `[rosbag_record_turtle-4] process has finished cleanly`

- Verify that your bag file is properly recorded by using the rosbag info command followed by the absolute or relative path of the file. To do so, enter the following command<br/>
`roscd pkg_task0/bag_files`<br/>
`rosbag info my_turtle.bag`

- You can use the `rosbag play` command to see the messages you've recorded in the same order and rate. You can verify this by running the `turtlesim_node` and playing your bag file.

## Output 

![Output](https://user-images.githubusercontent.com/64604283/96679826-0847ac80-1392-11eb-97b2-2b48a92711cb.jpeg)

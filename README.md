The whole code is tested on ubuntu 22.04 and ros2 humble version
download moveit2_tutorials and moveit_task_constructor
```shell
git clone https://github.com/ros-planning/moveit2_tutorials.git
```
```shell
git clone https://github.com/ros-planning/moveit_task_constructor.git
```
colcon the relavant packages
```shell
sudo apt install ros-humble-moveit
sudo apt install ros-humble-moveit-ros-perception
colcon build --packages-select moveit_task_constructor_core
colcon build --packages-select moveit2_tutorials
rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

# constrain_test
In this pository I tested three different possible ways to run the planning constrain
## 1. the ros2 run with setup.py and setup.cfg [failed]
this method is based on 
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
the code is in version 91bfdd2c5587abdeb0d0be4182a56303544139ad

## 2. the ros2 launch with python file 
this method is based on 
https://github.com/ros-planning/moveit2_tutorials/tree/main/doc/examples/move_group_python_interface
the code is in version 

## 3. the ros2 launch with c++ file
this method is based on moveit2_tutorials on rolling
https://github.com/ros-planning/moveit2_tutorials
can be launched successfully, however still have problem on planning, on version d35adac61c20827f643f05133905a8a758bad4ed

How to execute
```shell
ros2 launch moveit2_tutorials demo.launch.py
```
open another terminal
```shell
ros2 launch moveit2_tutorials ompl_constrained_planning.launch.py
```
## Final Version
```shell
ros2 launch moveit2_tutorials ompl_constrained_planning.launch.py
```
[Screencast from 01-12-2023 09:48:30 PM.webm](https://user-images.githubusercontent.com/48436877/212227127-96127be6-26f6-4706-9fb7-9784dd5d80fc.webm)

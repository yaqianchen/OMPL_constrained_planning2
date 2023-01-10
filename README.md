The whole code is tested on ubuntu 22.04 and ros2 humble version
download moveit2_tutorials and moveit_task_constructor
```shell
git clone https://github.com/ros-planning/moveit2_tutorials.git
```
```shell
git clone https://github.com/ros-planning/moveit_task_constructor.git
```


# constrain_test
In this pository I tested three different possible ways to run the planning constrain
## 1. the ros2 run with setup.py and setup.cfg [failed]
this method is based on 
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html
the code is in version 91bfdd2c5587abdeb0d0be4182a56303544139ad

## 2. the ros2 launch with python file 
this method is based on 
https://moveit.picknik.ai/humble/doc/examples/move_group_interface/move_group_interface_tutorial.html
the code is in version 

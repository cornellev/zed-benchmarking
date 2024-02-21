# zed-benchmarking
A catkin workspace containing various packages relating to running the ZED camera

### TODO: add rtabmap as a submodule dependency 

## Installing

```
git clone --recursive https://github.com/cornellev/zed-benchmarking.git`
```

Or, to update submodules (if you forgot to clone recursively):

```
cd <submodule>
git submodule update --init --recursive
```

Following installation, open the root of the project and enter:

```
catkin_make # builds all packages, generates build/ and devel/
source devel/setup.sh # or .bash, .zsh
```

For rtabmap, use: `sudo apt install ros-$ROS_DISTRO-rtabmap-ros`
Then, `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/ros/noetic/lib/x86_64-linux-gnu`.
In the future, use https://github.com/introlab/rtabmap_ros#installation to add as a submodule


## Resources

https://www.stereolabs.com/docs/ros/zed-node
http://wiki.ros.org/rtabmap_ros/Tutorials

## Requirements

* ZED SDK installed (CUDA required) *will not build without*

## Running

Always run the following from the root directory before continuing
```
source devel/setup.sh # or .bash, .zsh
```

Run ZED-provided Camera + RViz code:
```
roslaunch zed_display_rviz display_zed.launch
```

Run custom ZED package:
*(NEEDS LAUNCH FILE)*
```
roslaunch zed_wrapper zed.launch # starts running the camera, publishes expected zed topics
chmod +x src/zed-camera/src/camerae_processor.py
rosrun zed-camera camera_processor.py
rviz # can add topics to rviz
```

## Recording Data

Record pose, odometry, and transformation tree from ZED camera:
```
rosbag record /tf /tf_static /zed/zed_node/pose /zed/zed_node/odom
```

To playback:
```
roscore
rosbag play <bagfile..bag>
rviz
```

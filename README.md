# zed-benchmarking
A catkin workspace containing various packages relating to running the ZED camera

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

## Requirements

* ZED SDK installed (CUDA required) *will not build without*

## Running

Run ZED-provided Camera + RViz code:
```
roslaunch zed_display_rviz display_zed.launch
```
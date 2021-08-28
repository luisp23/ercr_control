# ercr_control
This package provide ROS nodes used to control the USV robot used in the Ecolymer River Cleanup Robot project.

--- 

## joystick_control
This package is used to control the ERCR robot with a joystick.

### Installing joystick_control

Install the ROS Noetic joystick drivers and joystick node. 
```bash
sudo apt-get install ros-noetic-joy
```

Plug in the joystick into your computer. Verify that the computer sees the joystick by verifying that it is listed in the input devices folder. It should be listed as "js0". 
```bash
ls /dev/input
```

Test out the joystick with the following command. Ensure that the data values are changing as you used the joystick.
```bash 
sudo jstest /dev/input/js0
```

Allow ROS to access the joystick: 
```bash 
sudo chmod a+rw /dev/input/jsX
```

### Using joystic_control

--- 
 
 ## pid_control
This package uses a PID controller to control the ERCR robot with a joystick.

 ### Installation

Installing the `robot_localization` package with the following:

 ```bash 
 sudo apt-get install ros-noetic-robot-localization
```
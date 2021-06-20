# joystick_control
This package is used to control the ERCR robot with a joystick.

## Installing the joystick drivers

Install the ROS Noetic joystick drivers and joystick node. 
```bash
sudo apt-get install ros-noetic-joy
```

Plug in the joystick into your computer. Verify that the computer sees the joystick by verifying that it is listed in the input devices folder. It should be lister as "js0". 
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

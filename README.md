# Lancer_Lumineer_ROV_Main

# ROV Control System

## Overview
This repository contains the code for a Remotely Operated Vehicle (ROV) control system, utilizing Pygame for the graphical user interface (GUI) and serial communication for hardware interaction. The project is designed to control an ROV through a user-friendly interface, allowing for joystick-based navigation, real-time video feedback, and customizable control widgets.

# Files Description
## ROV_final.py
The main script for the ROV control system. It initializes the GUI, processes user inputs, and communicates with the ROV hardware via serial connection.
---
# Key Features:
Pygame GUI: A custom GUI setup that includes a main view area and a sidebar for additional controls and information.

Joystick Control: Interprets joystick inputs for ROV movement, using mathematical calculations to translate joystick position into commands.

Serial Communication: Sends commands to the ROV's Arduino controller, allowing for real-time control of the vehicle.

Image Capture: Utilizes Pygame's camera module for capturing images, which can be used for navigation or documentation. (Needs to be configured)

## widgets2.py
Defines custom widget classes for the Pygame GUI, enhancing the interactivity and functionality of the ROV control system's interface.
---
# Toggleable Widget:
A key component for the GUI, allowing users to toggle settings or controls on and off with visual feedback.
# Getting Started
To run the ROV control system, ensure you have Python installed along with the Pygame library and the PySerial module for serial communication. Clone this repository, and run ROV_final.py to start the control interface.
---
# Prerequisites
Python 3.x
Pygame
PySerial
---
# Installation
Clone the repository to your local machine.
Install the required libraries using pip:
```python
pip install pygame pyserial
```
Navigate to the cloned repository's directory and run ROV_final.py: 
```python
python ROV_final.py
```

# Contributing
Contributions to the ROV control system are welcome. Please feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to adjust the content to better match your project's specifics or personal preferences.

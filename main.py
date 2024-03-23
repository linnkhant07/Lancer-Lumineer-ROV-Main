import pygame.camera
import json
import time
import pygame
import math  # needed for joystick
import widgets.widgets2 as widgets # needed to make widgets function properly
import serial  # needed to talk with Arduino
import os  # for creating the picture folder
from gui import GUI
import controller as controller


pygame.init()  # Initializes the pygame modules

#gui object
gui = GUI()
screen = gui.screen



sideBarWidth = 300

#-------------------------------------------------------
# camera setup
camera_width = 640
camera_height = 400
pygame.camera.init()  # Initializes the camera modules from the pygame library : Added 5/8/23

# initialize two cameras (loading the camera modules)
# Note: Camera indices typically begin with 0 (built in camera or first connected camera), then 1, 2, 3, etc..
cam1 = pygame.camera.Camera(0, (camera_width, camera_height))  # Main camera (adjust camera index for your unique PC setup)
# cam2 = pygame.camera.Camera(2, (camera_width, camera_height)) # Disabled to avoid servo claw jitter
cameraSurface = pygame.Surface((camera_width, camera_height*2), pygame.SRCALPHA)

transparency = 0
cameraSurface.fill((0, 0, 0, transparency))

# start the cameras (turn on cameras)
cam1.start()
# cam2.start() # Disabled to avoid sersvo claw jitter
#-------------------------------------------------------


#SET UP GUIS HERE--------

# Logo Image setup
# loading the image
# image = pygame.image.load("images/My project-1.png") # Can comment this line of code out if you do not have a logo file within same directory

# Scale the image
# scaledImage = pygame.transform.scale(image, (240, 200)) # Can comment this line of code out if you do not have a logo file within same directory

# open serial com to Arduino !!!!!!!!!!!!
#ser = serial.Serial(port='COM6', baudrate=9600, timeout=.1, dsrdtr=True) # Can comment this out if Arduino board is not connected to USB serial port.
# dsrdtr=True stops Arduino Mega from auto resetting

trigger_button = [False, False]  # Initialize False Boolean values for Left Button and Right Button
# trigger_button = [(LeftButton State) = False, (RightButton State) = False].
# This is so that the trigger buttons do not increment/decrement the clawValue unless triggered by user.

# x_y_button = [False, False] # for D-pad controls

# Initialize min/max and clawValues
max_value = 80  # After some tests with the claw, 0-80 is the ideal safe operating range for the claw (0 = fully closed, 80 = fully opened.)
min_value = 0
clawValue = 0
# Initialize joystick
joystick = None
if pygame.joystick.get_count() == 0:
    print('No joystick Detected')
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()  # initialize joystick
# Set the variable to control image capture
capture_count = 0
# Main Event Loop
#while the joystick exists
while pygame.joystick.get_count() == 1:
    
    commands = controller.handle_input(cam1, min_value, max_value, joystick, gui.onStatus, trigger_button, clawValue, gui.mLeftSlider, gui.mRightSlider, gui.zSlider)

    MESSAGE = json.dumps(commands)  # puts python dictionary in Json format
    ser.write(bytes(MESSAGE, 'utf-8'))  # byte format sent to arduino
    ser.flush()

    try:
        data = ser.readline().decode("utf-8")  # decode into byte from Arduino
        dict_json = json.loads(data)  # data from arduino in dictionary form

        temp_display.value = dict_json['volt']  # assign temp to dispaly
        th_up_display.value = dict_json['sig_up_1']  # vertical thruster value from Arduino
        th_left_display.value = dict_json['sig_lf']  # vertical thruster value from Arduino
        th_right_display.value = dict_json['sig_rt']  # vertical thruster value from Arduino
        claw_display.value = dict_json['claw']  # claw value from Arduino

        ser.flush()

    except Exception as e:
        print(e)

    pass
    

    

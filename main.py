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
'''
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
    
    commands = controller.handle_input(cam1, min_value, max_value, joystick, onStatus, trigger_button, clawValue, mLeftSlider, mRightSlider, zSlider)

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
    # Draw Stuff (Rendering the data as a display for the GUI)
    dHeight = onStatus.get_height() # get the height of the toggleable widget
    guiScreen.blit(onStatus.render(), (0, 0)) # blitting the running status
    guiScreen.blit(mLeftSlider.render(), (0, 9 * dHeight)) # blitting thruster values
    guiScreen.blit(mRightSlider.render(), (100, 9 * dHeight)) # blitting thruster values
    guiScreen.blit(zSlider.render(), (200, 9 * dHeight))  # blitting thruster values

    guiScreen.blit(temp_display.render(), (0, dHeight))  # blitting temperature values# pick a font you have and set its size
    guiScreen.blit(th_up_display.render(), (0, 2 * dHeight)) # blitting thruster values
    guiScreen.blit(th_left_display.render(), (0, 3 * dHeight)) # blitting thruster values
    guiScreen.blit(th_right_display.render(), (0, 4 * dHeight)) # blitting thruster values
    guiScreen.blit(claw_display.render(), (0, 5 * dHeight))  # display the claw value on the screen

    # Capture images from the camera (cameras 1 and 2)
    img1 = cam1.get_image()
    # img2 = cam2.get_image() # Camera 2 disabled to avoid servo claw jitter. 

    # Rendering camera display images onto the GUI menu
    cameraSurface.blit(img1, (0, 0))  # surface for camera 1
    # cameraSurface.blit(img2, (0, 400))  # surface for camera 2

    # Rendering more labeling and display elements onto Pygame window.
    screen.blit(cameraSurface, (460, 0))  # 2 cameras
    screen.blit(guiScreen, (0, 140))  # all the gui
    # screen.blit(scaledImage, (10, -60))  # discord logo
# Rending the text for the user controls onto the GUI window as defined in the beginning of the code.
    screen.blit(leftText, (15, 290))
    screen.blit(rightText, (115, 290))
    screen.blit(ZAxisText, (215, 290))
    screen.blit(Controls, (720, 390))
    screen.blit(left_button, (650, 425))
    screen.blit(right_button, (650, 450))
    screen.blit(button_A, (650, 470))
    screen.blit(LF_Joy_Up, (650, 495))
    screen.blit(LF_Joy_Down, (650, 520))
    screen.blit(LF_Joy_Left, (650, 550))
    screen.blit(LF_Joy_Right, (650, 570))
    screen.blit(RG_Joy_Up, (650, 600))
    screen.blit(RG_Joy_Down, (650, 620))

    pygame.display.flip()  # update screen for all rectangular images
'''
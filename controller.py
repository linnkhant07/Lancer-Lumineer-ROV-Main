import pygame
import json
import math
import serial

class Controller:
    def __init__(self, gui):
        self.gui = gui
        

    def handle_input(self,cam1, min_value, max_value, joystick, onStatus, trigger_button):
        # Get input from joystick and keyboard
        # Get input from joystick and keyboard
        pygame.event.pump()
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cam1.stop()
                # cam2.stop() # Disabled to avoid servo claw jitter
                pygame.quit()
                quit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # Button A; Button ID: 0 used for toggling max thruster status On/Off
                    onStatus.toggle()

            if event.type == pygame.JOYBUTTONDOWN:  # Using JoyButtonDown method (trigger button is pressed or x/y buttons are pressed)
                if event.button == 4:  # Left Button on Controller
                    trigger_button[0] = True
                elif event.button == 5:  # Right Button on Controller
                    trigger_button[1] = True

            if event.type == pygame.JOYBUTTONUP:  # Using JoyButtonUp method (trigger button is released or x/y buttons are released)
                if event.button == 4:  # If Left Trigger Button is released, then set Boolean value back to False
                    trigger_button[0] = False
                elif event.button == 5:  # If Right Trigger Button is released, then set Boolean value back to False
                    trigger_button[1] = False
            # Originally for task 2.1 Coral Head 3D modeling via Underwater Photogrammetry. (Completely unused in the end)
            if event.type == pygame.JOYBUTTONDOWN:  # for taking pictures
                if event.button == 1:
                    capture_count += 1
                    img_filename = f'ROV_3D/capture_{capture_count}.jpg'
                    img_surface = cam1.get_image()
                    pygame.image.save(img_surface, img_filename)
                    print(f"Image captured and saved as {img_filename}")

            # Optional: Rebinded forward/reverse thruster movement to D-pad (ran out of time to fully test this feature)
            # if event.type == pygame.JOYHATMOTION:
            #     hat_state = joystick.get_hat(0) # Index 0 means the first available d-pad on the controller
            #     if hat_state == (0, 1):  # D-pad pointing up
            #         x_y_button[0] = True
            #     elif hat_state == (0, -1):
            #         x_y_button[1] = True
            #     else:
            #         x_y_button = [False, False]

        # Incrementing/Decrementing the Main Claw Values
        if trigger_button[0] == True:
            if self.gui.clawValue >= max_value:
                self.gui.clawValue = max_value
            else:
                self.gui.clawValue += 5  # After some testing, increment and decrement value of 5 is the most optimal.
        elif trigger_button[1] == True:
            if self.gui.clawValue <= min_value:
                self.gui.clawValue = min_value
            else:
                self.gui.clawValue -= 5
        # Sets the self.gui.clawValue to the value the moment the button is released.
        elif trigger_button[0] == False:
            self.gui.clawValue = self.gui.clawValue
        elif trigger_button[1] == False:
            self.gui.clawValue = self.gui.clawValue

    # Commands to send ROV
        commands = {}  # define python dictionary
        if joystick is not None:
            x = joystick.get_axis(1)  # left joystick -1 is left to +1 is right (left thruster)
            y = joystick.get_axis(0)  # left joystick -1 is up +1 is down (right thruster)
            z = joystick.get_axis(3)  # right joystick x-axis, used for vertical

        if abs(x) < .5:  # define a dead zone
            x = 0
        if abs(y) < .5:  # define a dead zone
            y = 0
        if abs(z) < .2:  # define a dead zone
            z = 0
        # When the status is toggled to "On" by pressing Button A on the controller:
        # Limits thrust for SURGE direction (forward/backward).
        if onStatus.state:
            x = x * 1.414  # gives value of 1 for full thrust forward and backwards
            y = y * 1.414  # gives value of 1 for full thrust forward and backwards

        # rotate x and y-axis of joystick 45 degrees
        x_new = (x * math.cos(math.pi / -4)) - (y * math.sin(math.pi / -4))  # horizontal left
        y_new = (x * math.sin(math.pi / -4)) + (y * math.cos(math.pi / -4))  # horizontal right

        # limits joystick values to +/- 1
        if x_new > 1:
            x_new = 1.0
        if y_new > 1:
            y_new = 1.0
        if x_new < -1:
            x_new = -1.0
        if y_new < -1:
            y_new = -1.0

        # add to dictionary
        # Cubing the values gives more control with lower power
        # These are the commands being sent to the Arduino Mega Board
        commands['tleft'] = x_new ** 3
        commands['tright'] = y_new ** 3
        commands['tup'] = z ** 3
        commands['claw'] = self.gui.clawValue  # send the claw value

        # Optional rebinding of Forward/Reverse to D-pad on the Xbox controller.
        # if x_y_button[0] == True and joystick is not None:
        #     commands['tleft'] = 0.5 ** 3
        #     commands['tright'] = 0.5 ** 3
        # if x_y_button[1] == True and joystick is not None:
        #     commands['tleft'] == -0.5 ** 3
        #     commands['tright'] == -0.5 ** 3
        # if x_y_button[0] == False and x_y_button[1] == False and joystick is None:
        #     commands['tleft'] = 0
        #     commands['tright'] = 0

        #need to return these to update in gui
        self.gui.mLeftSlider.value = - commands['tleft']  # assign thruster values to a display
        self.gui.mRightSlider.value = commands['tright']
        self.gui.zSlider.value = - commands['tup']


        return commands
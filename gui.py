import pygame
import os
import widgets.widgets2 as widgets

class GUI:
    def __init__(self):
        self.setup()

    def setup(self):
        # Initialize Pygame window and GUI elements
        self.sideBarWidth = 300
        self.size = width, height = 900 + self.sideBarWidth, 800  # size of GUI
        pygame.display.set_caption('ROV Control')
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((16, 43, 87))

        # setup displays in GUI
        self.guiScreen = pygame.Surface((80 + self.sideBarWidth, 800), pygame.SRCALPHA)
        self.guiTransparency = 0
        self.guiScreen.fill((0, 0, 0, self.guiTransparency))

        # Define and initialize GUI elements
        self.onStatus = widgets.toggleable("Running", self.sideBarWidth)
        self.zSlider = widgets.sliderdisplay("Z", 100, 320)
        
        self.mLeftSlider = widgets.sliderdisplay("LeftSlider", 100, 320)
        self.mRightSlider = widgets.sliderdisplay("RightSlider", 100, 320)

        self.temp_display = widgets.display("Temp (C)", self.sideBarWidth)
        self.th_up_display = widgets.display("Servo Up", self.sideBarWidth)
        self.th_left_display = widgets.display("Servo Left", self.sideBarWidth)
        self.th_right_display = widgets.display("Servo Right", self.sideBarWidth)
        self.claw_display = widgets.display("Main Claw Value", self.sideBarWidth)

        self.font = pygame.font.SysFont("monospace", 16)
        self.leftText = self.font.render("Left", True, (255, 255, 255))
        self.rightText = self.font.render("Right", True, (255, 255, 255))
        self.ZAxisText = self.font.render("Z-axis", True, (255, 255, 255))

        self.Controls = self.font.render("User Controls: ", True, (255, 255, 255)) 
        self.left_button = self.font.render("LB: Close Claw", True, (255, 255, 255))
        self.right_button = self.font.render("RB: Open Claw", True, (255, 255, 255))
        self.button_A = self.font.render("A: Toggle Max Thrust", True, (255, 255, 255))
        self.LF_Joy_Up = self.font.render("Left Joy Up: Forward", True, (255, 255, 255))
        self.LF_Joy_Down = self.font.render("Left Joy Down: Reverse", True, (255, 255, 255))
        self.LF_Joy_Left = self.font.render("Left Joy Left: Turn Left", True, (255, 255, 255))
        self.LF_Joy_Right = self.font.render("Left Joy Right: Turn Right", True, (255, 255, 255))
        self.RG_Joy_Up = self.font.render("Right Joy Up: Ascend", True, (255, 255, 255))
        self.RG_Joy_Down = self.font.render("Right Joy Down: Descend", True, (255, 255, 255))

    def render(self, cam1, cameraSurface):
       

        # Draw Stuff (Rendering the data as a display for the GUI)
        dHeight = self.onStatus.get_height() # get the height of the toggleable widget
        self.guiScreen.blit(self.onStatus.render(), (0, 0)) # blitting the running status
        self.guiScreen.blit(self.mLeftSlider.render(), (0, 9 * dHeight)) # blitting thruster values
        self.guiScreen.blit(self.mRightSlider.render(), (100, 9 * dHeight)) # blitting thruster values
        self.guiScreen.blit(self.zSlider.render(), (200, 9 * dHeight))  # blitting thruster values

        self.guiScreen.blit(self.temp_display.render(), (0, dHeight))  # blitting temperature values# pick a font you have and set its size
        self.guiScreen.blit(self.th_up_display.render(), (0, 2 * dHeight)) # blitting thruster values
        self.guiScreen.blit(self.th_left_display.render(), (0, 3 * dHeight)) # blitting thruster values
        self.guiScreen.blit(self.th_right_display.render(), (0, 4 * dHeight)) # blitting thruster values
        self.guiScreen.blit(self.claw_display.render(), (0, 5 * dHeight))  # display the claw value on the screen

        # Capture images from the camera (cameras 1 and 2)
        img1 = cam1.get_image()
        # img2 = cam2.get_image() # Camera 2 disabled to avoid servo claw jitter. 

        # Rendering camera display images onto the GUI menu
        cameraSurface.blit(img1, (0, 0))  # surface for camera 1
        # cameraSurface.blit(img2, (0, 400))  # surface for camera 2

        # Rendering more labeling and display elements onto Pygame window.
        self.screen.blit(cameraSurface, (460, 0))  # 2 cameras
        self.screen.blit(self.guiScreen, (0, 140))  # all the gui
        # self.screen.blit(scaledImage, (10, -60))  # discord logo
    # Rending the text for the user controls onto the GUI window as defined in the beginning of the code.
        self.screen.blit(self.leftText, (15, 290))
        self.screen.blit(self.rightText, (115, 290))
        self.screen.blit(self.ZAxisText, (215, 290))
        self.screen.blit(self.Controls, (720, 390))
        self.screen.blit(self.left_button, (650, 425))
        self.screen.blit(self.right_button, (650, 450))
        self.screen.blit(self.button_A, (650, 470))
        self.screen.blit(self.LF_Joy_Up, (650, 495))
        self.screen.blit(self.LF_Joy_Down, (650, 520))
        self.screen.blit(self.LF_Joy_Left, (650, 550))
        self.screen.blit(self.LF_Joy_Right, (650, 570))
        self.screen.blit(self.RG_Joy_Up, (650, 600))
        self.screen.blit(self.RG_Joy_Down, (650, 620))

        pygame.display.flip()  # update screen for all rectangular images

    


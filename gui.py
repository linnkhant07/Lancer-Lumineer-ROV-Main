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

        return self.screen

    def render(self):
        # Render GUI elements onto Pygame window
        self.screen.blit(self.onStatus.render(), (0, 0))
        self.screen.blit(self.zSlider.render(), (100, 320))
        # Render other GUI elements similarly

    def handle_input(self):
        # Handle user input events
        pass


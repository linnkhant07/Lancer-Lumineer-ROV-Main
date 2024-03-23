import pygame
import os

# Define GUI-related functions and classes here
def setup_screen():
    pass

def setup_gui_elements():
    pass

def main_setup_gui():
    
    # Initialize Pygame window and GUI elements
    # GUI window setup
    sideBarWidth = 300
    size = width, height = 900 + sideBarWidth, 800  # size of GUI
    pygame.display.set_caption('ROV Control')
    screen = pygame.display.set_mode(size)
    screen.fill((16, 43, 87))

    # Define the name of the output folder
    folder_name = "ROV_3D"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return screen

    

def render_gui():
    # Render GUI elements onto Pygame window
    pass
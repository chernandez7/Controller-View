'''
Program to display input from a controller and visualize it as any other controller.
'''

import pygame
from Controllers import GBA

# Constants
WIDTH = 676
HEIGHT = 405
BACKGROUND_COLOR = 255, 0, 255

def main():
    '''
    Initialization of program
    '''

    canvas_size = WIDTH, HEIGHT
    canvas = pygame.display.set_mode(canvas_size)
    canvas.fill(BACKGROUND_COLOR)
    pygame.display.set_caption("GBA Controller")


    # Initialize the joysticks
    pygame.joystick.init()

    controller = GBA.GBA(canvas)

    clock = pygame.time.Clock()

    # Initialize Controllers
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        buttons = joystick.get_numbuttons()
        hats = joystick.get_numhats()

    done = True
    # Main draw loop
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=False

        # Update 10 times per second
        clock.tick(60)

        controller.UpdateState(joystick, buttons, hats)
        controller.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()

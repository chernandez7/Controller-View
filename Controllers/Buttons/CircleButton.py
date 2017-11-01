'''
Wrapper for pygame circle
'''

import pygame

class CircleButton(object):
    '''
    Circle Button
    '''

    def __init__(self, canvas, color, coords, radius):
        '''
        Initialization
        '''
        self.canvas = canvas
        self.color = color
        self.coords = coords
        self.radius = radius

    def draw(self):
        '''
        Draws all of the buttons
        '''

        pygame.draw.circle(self.canvas, self.color, self.coords, self.radius)


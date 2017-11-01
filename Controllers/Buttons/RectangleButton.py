'''
Wrapper for pygame rect
'''

import pygame

class RectangleButton(object):
    '''
    Rectangle Button
    '''

    def __init__(self, canvas, color, coords, width):
        '''
        Initialization
        '''
        self.canvas = canvas
        self.color = color
        self.coords = coords
        self.width = width

    def draw(self):
        '''
        Draws all of the buttons
        '''

        pygame.draw.rect(self.canvas, self.color, self.coords, self.width)
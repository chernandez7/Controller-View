'''
Class GBA
https://www.pygame.org/docs/ref/joystick.html
'''
from Controllers.Buttons import CircleButton, RectangleButton

GRAY = 100, 100, 100
YELLOW = 255, 255, 0

class GBA(object):
    '''
    Game Boy Advance Controller
    '''

    def __init__(self, canvas):
        '''
        Initialization
        '''
        self.canvas = canvas

        # Inactive
        self.a_button = CircleButton.CircleButton(canvas, GRAY, [615, 155], 20)
        self.b_button = CircleButton.CircleButton(canvas, GRAY, [557, 176], 20)

        self.l_button = RectangleButton.RectangleButton(canvas, GRAY, [40, 40, 80, 20], 20)
        self.r_button = RectangleButton.RectangleButton(canvas, GRAY, [540, 40, 80, 20], 20)

        self.start_button = CircleButton.CircleButton(canvas, GRAY, [151, 257], 10)
        self.select_button = CircleButton.CircleButton(canvas, GRAY, [151, 294], 10)

        self.up_button = RectangleButton.RectangleButton(canvas, GRAY, [95, 120, 28, 30], 10)
        self.down_button = RectangleButton.RectangleButton(canvas, GRAY, [95, 180, 30, 30], 10)
        self.left_button = RectangleButton.RectangleButton(canvas, GRAY, [65, 150, 30, 30], 10)
        self.right_button = RectangleButton.RectangleButton(canvas, GRAY, [125, 150, 30, 30], 10)

        # Active
        self.a_button_active = CircleButton.CircleButton(canvas, YELLOW, [615, 155], 20)
        self.b_button_active = CircleButton.CircleButton(canvas, YELLOW, [557, 176], 20)

        self.l_button_active = RectangleButton.RectangleButton(canvas, YELLOW, [40, 40, 80, 20], 20)
        self.r_button_active = RectangleButton.RectangleButton(canvas, YELLOW, [540, 40, 80, 20], 20)

        self.start_button_active = CircleButton.CircleButton(canvas, YELLOW, [151, 257], 10)
        self.select_button_active = CircleButton.CircleButton(canvas, YELLOW, [151, 294], 10)

        self.up_button_active = RectangleButton.RectangleButton(canvas, YELLOW, [95, 120, 28, 30], 10)
        self.down_button_active = RectangleButton.RectangleButton(canvas, YELLOW, [95, 180, 30, 30], 10)
        self.left_button_active = RectangleButton.RectangleButton(canvas, YELLOW, [65, 150, 30, 30], 10)
        self.right_button_active = RectangleButton.RectangleButton(canvas, YELLOW, [125, 150, 30, 30], 10)

        self.state = ButtonState()

    def draw(self):
        '''
        Draws all of the buttons
        '''
        # A
        if self.state.a_state:
            self.a_button_active.draw()
        else:
            self.a_button.draw()
        # B
        if self.state.b_state:
            self.b_button_active.draw()
        else:
            self.b_button.draw()
        # L
        if self.state.l_state:
            self.l_button_active.draw()
        else:
            self.l_button.draw()
        # R
        if self.state.r_state:
            self.r_button_active.draw()
        else:
            self.r_button.draw()
        # Start
        if self.state.start_state:
            self.start_button_active.draw()
        else:
            self.start_button.draw()
        # Select
        if self.state.select_state:
            self.select_button_active.draw()
        else:
            self.select_button.draw()
        # Up
        if self.state.up_state:
            self.up_button_active.draw()
        else:
            self.up_button.draw()
        # Down
        if self.state.down_state:
            self.down_button_active.draw()
        else:
            self.down_button.draw()
        # Left
        if self.state.left_state:
            self.left_button_active.draw()
        else:
            self.left_button.draw()
        # Right
        if self.state.right_state:
            self.right_button_active.draw()
        else:
            self.right_button.draw()

    def UpdateState(self, joystick, buttons, hats):
        '''
        Goes through every button and checks if it's active
        '''
        for i in range(buttons):
            button = joystick.get_button(i)
            if i == 0: # X
                if button == 1:
                    self.state.a_state = True
                    print "X Pressed"
                else:
                    self.state.a_state = False
            if i == 2: # Square
                if button == 1:
                    self.state.b_state = True
                    print "Square Pressed"
                else:
                    self.state.b_state = False
            if i == 4: # L
                if button == 1:
                    self.state.l_state = True
                    print "L Pressed"
                else:
                    self.state.l_state = False
            if i == 5: # R
                if button == 1:
                    self.state.r_state = True
                    print "R Pressed"
                else:
                    self.state.r_state = False
            if i == 6: # Select
                if button == 1:
                    self.state.select_state = True
                    print "Select Pressed"
                else:
                    self.state.select_state = False
            if i == 7: # Start
                if button == 1:
                    self.state.start_state = True
                    print "Start Pressed"
                else:
                    self.state.start_state = False

        for j in range(hats):
            hat = joystick.get_hat(j)

            if hat == (1, 0): # Right
                self.state.right_state = True
                print "right"
            elif hat == (-1, 0): # Left
                self.state.left_state = True
                print "left"
            elif hat == (0, 1): # Up
                self.state.up_state = True
                print "Up"
            elif hat == (0, -1): # Down
                self.state.down_state = True
                print "down"
            else:
                self.state.right_state = False
                self.state.left_state = False
                self.state.up_state = False
                self.state.down_state = False

class ButtonState():
    '''
    Whether buttons are on or not
    '''
    def __init__(self):
        '''
        All start as false
        '''
        self.a_state = False
        self.b_state = False

        self.select_state = False
        self.start_state = False

        self.l_state = False
        self.r_state = False

        self.up_state = False
        self.down_state = False
        self.left_state = False
        self.right_state = False


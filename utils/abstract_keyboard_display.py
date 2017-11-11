'''A simple graphics display for the key color data.
'''

from graphics import *
#from webcolors import *
from abstract_keyboard import *

class AbstractKeyboardDisplay:

    def __init__(self, abstract_keyboard):
        height = 200
        width = 500
        self.abs_key = abstract_keyboard
        self.size = 20
        self.win = GraphWin('Abstract Keyboard viewer', width, height)

    def display(self):
        for x in range(0,self.abs_key.length - 1):
            for y in range(0,self.abs_key.width - 1):
                key = Rectangle(Point(50+self.size*x,50+ self.size*y), Point(50+self.size*x+self.size, 50+self.size*y+self.size))
                #key.setFill('midnightblue')
                key.setFill('#%02x%02x%02x' % (self.abs_key.keys[y][x].colors.r, self.abs_key.keys[y][x].colors.g, self.abs_key.keys[y][x].colors.b))
                key.draw(self.win)

    def wait_user_interaction(self):
        message = Text(Point(self.win.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(self.win)
        self.win.getMouse()
        self.win.close()
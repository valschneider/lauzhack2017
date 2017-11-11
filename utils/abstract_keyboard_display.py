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

def main():
    # init a the absract keyboard with data
    abs_key = AbstractKeyboard()
    for x in xrange(abs_key.length):
        for y in xrange(abs_key.width):
            abs_key.keys[y][x].colors = Colors(x*256/abs_key.length,y*256/abs_key.width,(x+y)*2)

    # create a disply with the abstract display
    disp = AbstractKeyboardDisplay(abs_key)
    disp.display()
    disp.wait_user_interaction()


def blop():
    win = GraphWin('Abstract Keyboard viewer', width, height) # give title and dimensions

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

main()
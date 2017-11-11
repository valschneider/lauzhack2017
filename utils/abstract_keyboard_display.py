'''A simple graphics display for the key color data.
'''

from graphics import *

class AbstractKeyboardDisplay:

    def __init__(self):
        height = 200
        width = 500
        self.size = 20
        self.win = GraphWin('Abstract Keyboard viewer', width, height)

    def display(self):
        for x in range(0,21):
            for y in range(0,5):
                key = Rectangle(Point(50+self.size*x,50+ self.size*y), Point(50+self.size*x+self.size, 50+self.size*y+self.size))
                #rgb_to_name((0, 0, 0))
                key.setFill('midnightblue')
                key.draw(self.win)

    def wait_user_interaction(self):
        message = Text(Point(self.win.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(self.win)
        self.win.getMouse()
        self.win.close()

def main():
    disp = AbstractKeyboardDisplay()
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
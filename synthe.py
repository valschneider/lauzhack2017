from utils.abstract_keyboard import *
from utils.abstract_keyboard_display import *

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

main()
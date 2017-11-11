import os
import sys

basepath = os.path.dirname(os.path.abspath(__file__))
basepath = os.path.abspath(os.path.join(basepath, os.pardir))

sys.path.append(basepath)
from utils import PhysicalKeyboard
from utils import Colours

kbd = PhysicalKeyboard()

for idx, row in kbd.layout["rows"].iteritems():
    for key in row:
        if (idx % 3) == 0:
            kbd.set_key_colour(kbd.keys[key]["keycode"], Colours(100, 0, 0))
        elif (idx + 1 % 3) == 0:
            kbd.set_key_colour(kbd.keys[key]["keycode"], Colours(0, 100, 0))
        elif (idx + 2 % 3) == 0:
            kbd.set_key_colour(kbd.keys[key]["keycode"], Colours(0, 0, 100))

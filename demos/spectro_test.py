import os
import sys

basepath = os.path.dirname(os.path.abspath(__file__))
basepath = os.path.abspath(os.path.join(basepath, os.pardir))

sys.path.append(basepath)
from utils import PhysicalKeyboard
from spectro import Spectro

kbd = PhysicalKeyboard()

spectro = Spectro(kbd)
for i in xrange(len(spectro.freqs)):
    spectro.freqs[i] = 15 * i

spectro.update_phys_kbd()

raw_input("Press ENTER to end test")

#!/usr/bin/env python

import time
import random
import string
import sys
import os

basepath = os.path.dirname(os.path.abspath(__file__))
basepath = os.path.abspath(os.path.join(basepath, os.pardir))

sys.path.append(basepath)

from utils.abstract_keyboard import Colours
from utils import PhysicalKeyboard

kbd = PhysicalKeyboard()
MAX_LEN = len(kbd.layout["rows"][0])

def generate_sequence():
    seq = ''.join(random.choice(string.ascii_lowercase) for _ in xrange(MAX_LEN))
    return seq

def start_sequence(seq, n, delay):
    if n <= len(seq):
        kbd.set_all_colour(Colours(0,0,0))
        for x in xrange(n):
            kbd.set_key_colour(seq[x].upper(), Colours(0, 100, 0))
            if x > 0:
                kbd.set_key_colour(seq[x-1].upper(), Colours(100, 0, 0))
            time.sleep(delay)
            kbd.set_all_colour(Colours(0,0,0))
            
# game logic
print("welcome to the Follow Me game !")
seq = generate_sequence()
loose = False
# Lower initial delay to let the user know where to look
delay = 2.

kbd.set_all_colour(Colours(0,0,0))

for score in xrange(MAX_LEN) :

    for i in xrange(score + 1):
        kbd.set_key_colour(seq[i].upper(), Colours(0, 100, 100))
        if i > 0:
            kbd.set_key_colour(seq[i-1].upper(), Colours(100, 0, 0))
        if i > 1:
            kbd.set_key_colour(seq[i-2].upper(), Colours(0, 0, 0))
            
        time.sleep(delay)
        
    for i in xrange(score - 1, score + 1):
        kbd.set_key_colour(seq[i].upper(), Colours(0, 0, 0))
        
    user_input = raw_input("please repeat the sequence\n")

    if user_input == seq[0:score+1]:
        print("nice !")
        kbd.set_key_colour(kbd.layout["rows"][0][score], Colours(0, 100, 0))
        delay = 0.6
    else:
        kbd.set_all_colour(Colours(100,0,0))
        time.sleep(1)
        print("hum...sorry...")
        print("right sequence was :")
        print(seq[0:score+1])
        break
        
if score == MAX_LEN - 1:
    kbd.set_all_colour(Colours(0,100,0))
    time.sleep(1)

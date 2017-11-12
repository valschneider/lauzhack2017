#!/usr/bin/env python

import time
import random
import string
import pyaudio 
import wave
import numpy
import subprocess
import threading
import os
import sys

basepath = os.path.dirname(os.path.abspath(__file__))
basepath = os.path.abspath(os.path.join(basepath, os.pardir))

sys.path.append(basepath)
from utils import PhysicalKeyboard
from utils import Colours

kbd = PhysicalKeyboard()

music_loop = [[False for x in xrange(8)] for y in xrange(4)]

def welcome():
    print("welcome to the synthe demo !")
    print("1) bell")
    print("2) snare")
    print("3) crash cymbal")
    print("4) drum")
    print("enter to start the loop")

def setup():
    global coord_to_key
    global key_to_coord
    coord_to_key = []
    key_to_coord = {}

    for idx, row in kbd.layout["rows"].iteritems():
        if idx > 0 and idx < 5:
            coord_to_key.append([])
            for key in row[1:]:
                if len(coord_to_key[idx - 1]) < 8:
                    coord_to_key[idx - 1].append(key)
                    key_to_coord[key] = ((idx - 1), len(coord_to_key[idx - 1]) - 1)

def char_to_key(char):
    if char == "0":
        return "ZERO"
    elif char == "1":
        return "ONE"
    elif char == "2":
        return "TWO"
    if char == "3":
        return "THREE"
    elif char == "4":
        return "FOUR"
    elif char == "5":
        return "FIVE"
    if char == "6":
        return "SIX"
    elif char == "7":
        return "SEVEN"
    elif char == "8":
        return "EIGHT"
    elif char == "9":
        return "NINE"
    else:
        return char.upper()

def user_input():
    melodie_keys = raw_input("please enter the melody :")
    #melodie_keys = "ujhg"
    for char in melodie_keys:
        coord = key_to_coord[char_to_key(char)]
        music_loop[coord[0]][coord[1]] = True

def update_display(mesure):
    kbd.set_all_colour(Colours(0, 0, 0))

    for i in range(4):
        for j in range(8):
            if music_loop[i][j] and j >= mesure:
                # Because reasons
                time.sleep(0.03)
                if i == 0:
                    kbd.set_key_colour(coord_to_key[0][j-mesure], Colours(100, 0, 0))
                elif i == 1:
                    kbd.set_key_colour(coord_to_key[1][j-mesure], Colours(50, 100, 0))
                elif i == 2:
                    kbd.set_key_colour(coord_to_key[2][j-mesure], Colours(0, 50, 100))
                else:
                    kbd.set_key_colour(coord_to_key[3][j-mesure], Colours(0, 0, 100))


def audio_subprocess(mesure):
    update_display(mesure)
    time.sleep(0.5)

    with open(os.devnull, 'w') as FNULL:
        if music_loop[0][mesure] == True:
            subprocess.Popen(["ffplay", "-nodisp", "-autoexit", os.path.join(basepath, "audio/snare.wav")], stdout=FNULL, stderr=subprocess.STDOUT)
        if music_loop[1][mesure] == True:
            subprocess.Popen(["ffplay", "-nodisp", "-autoexit", os.path.join(basepath, "audio/bass_drum.wav")], stdout=FNULL, stderr=subprocess.STDOUT)
        if music_loop[2][mesure] == True:
            subprocess.Popen(["ffplay", "-nodisp", "-autoexit", os.path.join(basepath, "audio/crash_cymbal.wav")], stdout=FNULL, stderr=subprocess.STDOUT)
        if music_loop[3][mesure] == True:
            subprocess.Popen(["ffplay", "-nodisp", "-autoexit", os.path.join(basepath, "audio/bell.wav")], stdout=FNULL, stderr=subprocess.STDOUT)

def main():
    # game logic
    welcome()
    setup()
    user_input()
    for i in xrange(8):
        audio_subprocess(i)

main()

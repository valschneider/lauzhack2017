import time
import random
import string
from utils.abstract_keyboard import *
from utils.abstract_keyboard_display import *
from utils import PhysicalKeyboard

kbd = PhysicalKeyboard()
#ak = AbstractKeyboard()
#kbd = AbstractKeyboardDisplay(ak)

def generate_sequence():
    seq = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    print(seq)
    return seq

def start_sequence(seq, n,delay):
    if n <= len(seq):
        kbd.set_all_colour(Colours(0,0,0))
        for x in xrange(n):
            print seq[x]
            kbd.set_key_colour(seq[x].upper(), Colours(0, 100, 0))
            if x > 0:
                kbd.set_key_colour(seq[x-1].upper(), Colours(100, 0, 0))
            time.sleep(delay)
            kbd.set_all_colour(Colours(0,0,0))

def welcome():
    print("welcome to the Follow Me game !")

def main():
    # game logic
    welcome()
    seq = generate_sequence()
    loose = False
    seq_number = 1

    while True:
        start_sequence(seq, seq_number, 1)
        user_input = raw_input("please repeat the sequence :")
        print(user_input)
        if user_input == seq[0:seq_number]:
            print("nice ! can you follow :")
            seq_number = seq_number+1
        else:
            print("hum...sorry...")
            print("right sequence was :")
            print(seq[0:seq_number])
            break;

main()
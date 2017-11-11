import time
import random
import string
from utils.abstract_keyboard import *
from utils.abstract_keyboard_display import *

def generate_sequence():
    seq = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    print(seq)
    return seq

def start_sequence(seq, n,delay):
    if n <= len(seq):
        for x in xrange(n):
            print seq[x]
            time.sleep(delay)

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
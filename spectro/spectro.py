from pylab import *
from scipy.io import wavfile

from time import sleep

from utils import Colours

class Spectro(object):
    def __init__(self, phys_kbd, harmonics=6):
        self.freqs = [0 for i in xrange(harmonics)]
        self.phys_kbd = phys_kbd

    def play(self, sound_file):
        sampling_rate, data = wavfile.read(sound_file)
        data = data / (2.**15)
        data = abs(data)
        data = data * 300

        sound_duration = data.shape[0] / sampling_rate

        prev = 0
        now = 0
        wait_time = 1./30

        while now < data.shape[0]:
            sleep(wait_time)
            now += int(wait_time * sampling_rate)
            res = data[prev:now].mean()
            print res
            for i in xrange(len(self.freqs)):
                self.freqs[i] = int(res)
            self.update_phys_kbd()
            prev = now

    def update_phys_kbd(self):
        #self.phys_kbd.set_all_colour(Colours(0, 0, 0))
        for row, freq in enumerate(self.freqs):
            keys = self.phys_kbd.layout["rows"][row]

            keys_to_lit = min(freq / 10, len(keys))
            for key in keys[0:keys_to_lit]:
                self.phys_kbd.set_key_colour(key, Colours(0, 100, 100))
            for key in keys[keys_to_lit:]:
                self.phys_kbd.set_key_colour(key, Colours(0, 0, 0))

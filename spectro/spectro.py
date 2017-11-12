from pylab import *
from scipy.io import wavfile
import subprocess

from time import sleep, time

from utils import Colours

class Spectro(object):
    def __init__(self, phys_kbd, harmonics=6):
        self.freqs = [0 for i in xrange(harmonics)]
        self.phys_kbd = phys_kbd

    def play(self, sound_file):
        sampling_rate, data = wavfile.read(sound_file)
        data = data / (2.**15)
        data = abs(data)
        data = data * 500

        sound_duration = data.shape[0] / sampling_rate

        start = time()
        prev = 0.0
        now = 0.0

        # 30Hz refresh rate for smoothy display
        wait_time = 1./30
        subprocess.Popen(["ffplay", "-nodisp", "-autoexit", sound_file])

        while now < sound_duration:
            # This is ugly as fuck but it works
            sleep(wait_time)
            now = time() - start

            res = data[int(prev * sampling_rate):int(now * sampling_rate)].mean()

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

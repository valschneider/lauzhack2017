from pylab import *
from scipy.io import wavfile
import subprocess

from time import sleep, time

from utils import Colours

red = Colours(100, 0, 0)
yellow = Colours(100, 100, 0)
green = Colours(0, 100, 0)
cyan = Colours(0, 100, 100)
blue = Colours(0, 0, 100)
purple = Colours(100, 0, 100)

class Spectro(object):
    def __init__(self, phys_kbd, harmonics=6):
        self.freqs = [0 for i in xrange(harmonics)]
        self.phys_kbd = phys_kbd

    def get_master_volume(self):
        volume = int(subprocess.check_output('adjust_get_current_system_volume_vista_plus'))
        return volume

    def play(self, sound_file):
        sampling_rate, data = wavfile.read(sound_file)
        data = data / (2.**15)
        data = abs(data)
        # In average, more than half the keyboard is list
        data = data * (50. / data.mean())
        #data = data * 500

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

            ratio = self.get_master_volume() / 15.

            res = data[int(prev * sampling_rate):int(now * sampling_rate)].mean() * ratio

            for i in xrange(len(self.freqs)):
                self.freqs[i] = int(res)

            self.update_phys_kbd()
            prev = now

    def update_phys_kbd(self):
        for row, freq in enumerate(self.freqs):
            keys = self.phys_kbd.layout["rows"][row]

            keys_to_lit = min(freq / 10, len(keys))
            for idx, key in enumerate(keys[0:keys_to_lit]):
                depth = (100 * idx) / len(keys)
                if depth <= 20:
                    colour = blue
                elif depth <= 40:
                    colour = cyan
                elif depth <= 60:
                    colour = green
                elif depth <= 80:
                    colour = yellow
                elif depth <= 100:
                    colour = red

                self.phys_kbd.set_key_colour(key, colour)
            for key in keys[keys_to_lit:]:
                self.phys_kbd.set_key_colour(key, Colours(0, 0, 0))

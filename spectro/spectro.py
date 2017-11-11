from utils import Colours

class Spectro(object):
    def __init__(self, phys_kbd, harmonics=6):
        self.freqs = [0 for i in xrange(harmonics)]
        self.phys_kbd = phys_kbd

    def update_phys_kbd(self):
        self.phys_kbd.set_all_colour(Colours(0, 0, 0))
        from time import sleep
        sleep(5)
        for row, freq in enumerate(self.freqs):
            keys = self.phys_kbd.layout["rows"][row]

            keys_to_lit = min(freq / 10, len(keys))
            print keys_to_lit
            for key in keys[0:keys_to_lit]:
                print key
                self.phys_kbd.set_key_colour(key, Colours(0, 100, 100))

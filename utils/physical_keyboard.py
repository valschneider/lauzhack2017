import json
import sys
import os
from importlib import import_module
from abstract_keyboard import KeyData

basepath = os.path.dirname(os.path.abspath(__file__))
basepath = os.path.join(basepath, os.pardir)

logi_dir = os.path.join(basepath, "logiPy")
sys.path.append(logi_dir)
import logipy.logi_led
from logipy.logi_led import logi_led_set_lighting_for_key_with_hid_code

class PhysicalKeyboard(object):
    def __init__(self, model="g810"):
        layout_dir = os.path.join(basepath, "layouts")
        layout_file = os.path.join(layout_dir, model + ".json")

        with open(layout_file, 'r') as fh:
            layout = json.load(fh)

        self.keys = {}
        for key, data in layout["keys"].iteritems():
            # Load keycodes from logiPy
            self.keys[key] = {
                "data" : KeyData(),
                "keycode" : getattr(logipy.logi_led, key),
                "rows" : data["rows"]
            }

        logi_led.logi_led_init()
        time.sleep(1)

    def set_key_colour(self, keycode):
        logi_led_set_lighting_for_key_with_hid_code(keycode, 100, 0, 0)

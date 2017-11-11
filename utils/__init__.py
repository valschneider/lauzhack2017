from abstract_keyboard import KeyData, AbstractKeyboard

import os
import sys
from glob import glob
from importlib import import_module

logi_dir = os.path.dirname(os.path.abspath(__file__))
logi_dir = os.path.abspath(
    os.path.join(
        os.path.join(logi_dir, os.pardir),
        "logiPy"
    )
)

sys.path.append(logi_dir)

import logipy.logi_led

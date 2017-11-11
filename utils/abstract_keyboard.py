from collections import namedtuple

Colours = namedtuple('Colours', ['r', 'g', 'b'])

class KeyData(object):
    def __init__(self):
        self.colours = Colours(0, 0, 0)

class AbstractKeyboard(object):
    def __init__(self, width=6, length=22):
        self.width = width
        self.length = length

        self.keys = [[KeyData() for j in xrange(length)] for i in xrange(width)]

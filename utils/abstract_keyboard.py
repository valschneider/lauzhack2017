from collections import namedtuple

Colors = namedtuple('Colors', ['r', 'g', 'b'])

class KeyData(object):
    def __init__(self):
        self.colors = Colors(0, 0, 0)

class AbstractKeyboard(object):
    def __init__(self, width=6, length=22):
        self.width = width
        self.length = length

        self.keys = [[KeyData() for j in xrange(length)] for i in xrange(width)]

    def clear(self):
   		for x in xrange(self.length):
			for y in xrange(self.width):
				self.keys[y][x].colors = Colors(0,0,0)

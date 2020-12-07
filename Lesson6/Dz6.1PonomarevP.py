from itertools import cycle
from time import sleep


class TrafficLight:

    _color = ['red', 'yellow', 'green']

    def __init__(self, c=1):
        self.c = c*3

    def running(self):
        for e1 in cycle(self._color):
            if self.c == 0:
                break
            if e1 == 'red':
                print('Now is', e1)
                sleep(1)
            elif e1 == 'yellow':
                print('Now is', e1)
                sleep(2)
            elif e1 == 'green':
                print('Now is', e1)
                sleep(1)
            self.c -= 1


light = int(input('Enter number of cycles: '))
my_light = TrafficLight(light)
my_light.running()

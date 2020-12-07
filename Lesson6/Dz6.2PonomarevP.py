class Road:

    def __init__(self, length, width, height):
        self._my_length, self._my_width, self._my_height = length, width, height

    def volume(self):
        return self._my_length * self._my_width * self._my_height * 20


asphalt = input('Enter length, width, and height separated by a space: ')
true_length, true_width, true_height = map(int, asphalt.split())
my_road = Road(true_length, true_width, true_height)
print('You need kg of asphalt: ', my_road.volume())

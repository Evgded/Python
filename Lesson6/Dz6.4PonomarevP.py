class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            print("Siren sound!")
        print(f"Car {self.name} is ready to go!")

    def stop(self):
        print(f"Car {self.name} has successfully stopped. Hope you've enjoyed your ride!")

    def turn(self, direction):
        print(f"Car {self.name} has turned {direction}.")

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")


class TownCar(Car):

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")
        if self.speed > 60:
            print("Slow down!")


class SportCar(Car):

    def drift(self):
        print(f"Car {self.name} eron-don-don!")


class WorkCar(Car):

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")
        if self.speed > 40:
            print("Slow down!")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)

    def siren(self):
        print('Please stop and go out of your car!')


my_car = input('What car you want(TownCar = t, SportCar = s, WorkCar = w, PoliceCar = p: ')
my_speed = int(input('What speed you want: '))
my_color = input('What color you want: ')
my_name = input('What name you want: ')
if my_car == 't':
    t_c = TownCar(my_speed, my_color, my_name)
    t_c.go()
    t_c.turn('Right')
    t_c.show_speed()
    t_c.stop()
elif my_car == 's':
    s_c = SportCar(my_speed, my_color, my_name)
    s_c.go()
    s_c.turn('Left')
    s_c.show_speed()
    s_c.drift()
    s_c.stop()
elif my_car == 'w':
    w_c = WorkCar(my_speed, my_color, my_name)
    w_c.go()
    w_c.turn('Right')
    w_c.show_speed()
    w_c.stop()
elif my_car == 'p':
    p_c = PoliceCar(my_speed, my_color, my_name)
    p_c.go()
    p_c.turn('Left')
    p_c.show_speed()
    p_c.siren()
    p_c.stop()
else:
    print('Wrong data!')

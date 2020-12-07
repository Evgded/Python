class Stationery:

    def __init__(self, title):
        self.my_title = title

    def draw(self):
        print('Запуск отрисовки названия:', self.my_title)


class Pen(Stationery):

    def draw(self):
        print(f'Ээй уухнем {self.my_title}!')


class Pencil(Stationery):

    def draw(self):
        print(f'ЭЭЭЭэээй ууухнеммм {self.my_title}!')


class Handle(Stationery):

    def draw(self):
        print(f'Иии ещеее раз {self.my_title} ээй ууухнемм!!')


my_stationery = Stationery('Синий!')
my_pen = Pen('Оранжевый!')
my_pencil = Pencil('Красный!')
my_handle = Handle('Фиолетовый!')
my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()

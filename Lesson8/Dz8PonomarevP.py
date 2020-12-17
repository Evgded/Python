from random import sample, shuffle
from os import system


class Card:

    pool = [el for el in range(1, 91)]

    def __init__(self):
        shuffle(Card.pool)
        str_1 = Card.pool[:6]
        str_2 = Card.pool[6:11]
        str_3 = Card.pool[11:16]
        self.lst = [Card.place(str_1), Card.place(str_2), Card.place(str_3)]

    @staticmethod
    def place(nums):
        nums.sort()
        str_0 = ['  ' for _ in range(9)]
        index_str = sample([el for el in range(9)], 5)
        index_str.sort()
        for i, e1 in enumerate(index_str):
            str_0[e1] = nums[i]
        return str_0

    def is_in(self, m):

        turn = False

        for i, e1 in enumerate(self.lst):
            for j, num in enumerate(e1):
                if num == m:
                    turn = True
                    break
        return turn

    def cross_out(self, n):
        for i, e1 in enumerate(self.lst):
            for j, num in enumerate(e1):
                if num == n:
                    self.lst[i][j] = '--'
                    break
        return self.lst

    def is_win(self):

        win = True

        for i, e1 in enumerate(self.lst):
            win = True
            for j, num in enumerate(e1):
                if str(num).isdigit():
                    win = False
                    break
            if not win:
                break
        return win


class UserCard(Card):

    def __str__(self):
        card = '\n'.join([' '.join([str(num) for num in el]) for el in self.lst])
        return f'----- Ваша карточка ------\n{card}\n--------------------------'


class ComputerCard(Card):

    def __str__(self):
        card = '\n'.join([' '.join([str(num) for num in el]) for el in self.lst])
        return f'-- Карточка компьютера ---\n{card}\n--------------------------'


class Game:

    def __init__(self, me, comp):
        self.me = me
        self.comp = comp
        self.all_barrels = Card.pool
        shuffle(self.all_barrels)
        self.new_barrel = 0
        pass

    def play(self):
        turn = 1
        while True:
            system('cls')
            if self.comp.is_win() and self.me.is_win():
                print('Ничья!')
                break
            if self.comp.is_win():
                print('Вы проиграли компьютеру...')
                break
            if self.me.is_win():
                print('Поздравляю, вы выиграли игру!')
                break
            self.new_barrel = self.all_barrels.pop()
            fist_string = f'Новый бочонок: {self.new_barrel}(Осталось {90 - turn})'
            turn += 1
            print(fist_string, '\n', self.me, '\n', self.comp)
            last_string = input('Хотите зачеркнуть номер? (y/n)')
            self.comp.cross_out(self.new_barrel)
            if self.me.is_in(self.new_barrel) and last_string == 'y':
                self.me.cross_out(self.new_barrel)
            elif not self.me.is_in(self.new_barrel) and last_string == 'y':
                print('You wrong and lose!')
                break
            elif self.me.is_in(self.new_barrel) and last_string == 'n':
                print('You wrong and lose!')
                break
            elif not self.me.is_in(self.new_barrel) and last_string == 'n':
                continue
            else:
                print('You wrong and lose!')
                break


a = UserCard()
c = ComputerCard()
my_game = Game(a, c)
my_game.play()

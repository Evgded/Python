class Cell:
    def __init__(self, item):
        self.item = item

    def __add__(self, other):
        return self.item + other.item

    def __sub__(self, other):
        if self.item >= other.item:
            return self.item - other.item
        else:
            return 'Subtraction impossible'

    def __mul__(self, other):
        return self.item * other.item

    def __truediv__(self, other):
        return self.item // other.item

    def make_order(self, row):
        line = '*' * row
        examples = self.item // row
        remains = self.item % row
        out = []
        while examples > 0:
            out.append(line + '\\n')
            examples -= 1
        return ''.join(out) + '*' * remains


my_cell_1 = Cell(15)
my_cell_2 = Cell(17)
print(my_cell_1 + my_cell_2)
print(my_cell_1 - my_cell_2)
print(my_cell_1 * my_cell_2)
print(my_cell_1 / my_cell_2)
print(my_cell_1.make_order(7))

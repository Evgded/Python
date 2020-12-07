class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.my_name, self.my_surname, self.my_position = name, surname, position
        self._my_income = {'wage': wage, 'bonus': bonus}

    def my_name(self):
        print('Name is: ', self.my_name, self.my_surname)

    def my_salary(self):
        print('Salary is: ', self._my_income.get('wage') + self._my_income.get('bonus'))


class Position(Worker):

    def get_full_name(self):
        return self.my_position + ' ' + self.my_name + ' ' + self.my_surname

    def get_total_income(self):
        return self._my_income.get('wage') + self._my_income.get('bonus')


first_person = Position('Иван', 'Иванов', 'Токарь', 50000, 30000)
second_person = Position('Петр', 'Сидоров', 'Фрезеровщик', 40000, 20000)

print('First person is: ', first_person.get_full_name())
print('His salary is: ', first_person.get_total_income())
print('Name 1: ', first_person.my_surname)
print('His wage: ', first_person._my_income.get('wage'))
print('Second person is: ', second_person.get_full_name())
print('His salary is: ', second_person.get_total_income())
print('Surname: ', second_person.my_surname)

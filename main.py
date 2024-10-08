# Задача 1: Класс для работы с книгами

# Описание: Создайте класс Book, который будет содержать информацию о книге 
# (название, автор, год издания). Создайте методы для отображения информации 
# о книге и для изменения года издания.

# Условия:

#  • Создайте конструктор, который будет принимать название, автора и год.
#  • Добавьте метод get_info(), который будет выводить информацию о книге.
#  • Добавьте метод для изменения года издания.


class Book:
    
    def __init__(self, name: str, author: str, year: int ):
        self._name: str = name
        self._authot: str = author
        self._year: int = year

    def get_info(self):
        print(f' название: {self._name }, автор: {self._authot}, Год издания: {self._year}')

    def ch_year(self, new_year):
        self._year = new_year

b = Book('Война и Мир', 'Л.Н. Толстой',1827)
b.get_info()
b.ch_year(1822)
b.get_info()


# Задача 2: Класс для банковского счета

# Описание: Создайте класс BankAccount, который будет моделировать банковский счёт. В классе должны быть методы для пополнения счёта, снятия денег и вывода текущего баланса.

# Условия:

#  • Конструктор должен принимать начальный баланс.
#  • Метод deposit(amount) для пополнения счёта.
#  • Метод withdraw(amount) для снятия средств (не должно быть возможности уйти в минус).
#  • Метод get_balance() для отображения текущего баланса.

class BankAccount:
    def __init__(self, account: int):
        self.__account: int = account


    def deposit(self,amount: int):
        self.__account += amount

    def withdraw(self, amount: int):
        if amount > self.__account:
            raise ValueError('Недостаточно средств.')
        else:
            self.__account -= amount

    def get_balance(self):
        print(f'Баланс счета: {self.__account}')


BA = BankAccount(1000000)

BA.deposit(100000)
try:
    BA.withdraw(200000)
except ValueError as e:
    print(e, 'Попробуйте с другой суммой')

BA.get_balance()

try:
    BA.withdraw(1000001)
except ValueError as e:
    print(e,'Попробуйте с другой суммой')



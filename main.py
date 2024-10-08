# Задача 1: Класс для работы с книгами

# Описание: Создайте класс Book, который будет содержать информацию о книге 
# (название, автор, год издания). Создайте методы для отображения информации 
# о книге и для изменения года издания.

# Условия:

#  • Создайте конструктор, который будет принимать название, автора и год.
#  • Добавьте метод get_info(), который будет выводить информацию о книге.
#  • Добавьте метод для изменения года издания.


from abc import abstractmethod
import math


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


# Задача 3: Наследование

# Описание: Создайте класс Person, который будет хранить информацию о человеке (имя и возраст), 
# и класс Student, который наследуется от Person. В классе Student должны быть добавлены поля 
# для хранения учебного заведения и среднего балла.

# Условия:

#  • Конструктор класса Person должен принимать имя и возраст.
#  • Конструктор класса Student должен дополнительно принимать учебное заведение и средний балл.
#  • Добавьте методы для отображения информации о студенте.


class Person:
    def __init__(self,name: str, age: int):
        self._name: str = name
        self._age: int = age

    def __str__(self) -> str:
        return (f'ИМЯ: {self._name}, возраст: {self._age}')

class Student(Person):
    def __init__(self, name: str, age: int, institution: str, score: float):
        super().__init__(name, age)
        self.__institution: str = institution
        self.__score: float = score

    def __str__(self) -> str:
        return super().__str__() + f' Учится в {self.__institution}, средний балл {self.__score}'
    

s = Student('Иванов',21,'СФУ',4.2)

print(s)


# Задача 4: Полиморфизм

# Описание: Создайте классы Rectangle и Circle. Оба класса должны иметь метод get_area(), 
# который возвращает площадь фигуры. Реализуйте механизм полиморфизма, который позволяет 
# вызвать метод get_area() для объекта любого класса.

# Условия:

#  • Класс Rectangle должен принимать длину и ширину, а класс Circle — радиус.
#  • Метод get_area() должен возвращать площадь фигуры.

class Figure:
    @abstractmethod
    def get_area(self) -> float:
        raise NotImplementedError('get_area нужно переопределить')
        


class Rectangle(Figure):
    def __init__(self, length: int, width: int):
        self.__length: int = length
        self.__widht: int = width

    def get_area(self):
        return self.__widht * self.__length


    

class Circle(Figure):
    def __init__(self, radius: int):
        self.__radius: int = radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius


r = Rectangle(100,10)
print(r.get_area())

c = Circle(10)
print(c.get_area())
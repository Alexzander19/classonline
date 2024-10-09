# Задача 5: Магические методы

# Описание: Создайте класс ComplexNumber, который будет представлять комплексное число 
# и реализуйте сложение и вычитание комплексных чисел, используя магические методы add() и sub().

# Условия:

#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.

from __future__ import annotations
import math

class ComplexNumber:
    def __init__(self, re: float, im: float):
        self.__re: float = re
        self.__im: float = im

    def __str__(self):
        im = self.__im
        if im < 0:
            im = im * -1
        return f'{self.__re} {'-' if self.__im < 0 else '+'} {im }i' 

    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        re = self.__re + other.__re
        im = self.__im + other.__im

        return ComplexNumber(re,im)
    
    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        re = self.__re - other.__re
        im = self.__im - other.__im

        return ComplexNumber(re,im)
    
cn1 = ComplexNumber(3,-2)
cn2 = ComplexNumber(2,1)

cn3 = cn1 + cn2
print(cn3)

print(cn2 - cn1)



# Задача 6: Инкапсуляция

# Описание: Создайте класс Car, который содержит информацию о марке автомобиля, максимальной 
# скорости и текущей скорости. Инкапсулируйте переменные с текущей скоростью, чтобы нельзя было 
# напрямую её изменять.

# Условия:

#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя, чтобы скорость не 
#      превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.

class Car:
    def __init__(self, mark: str, max_speed: int):
        self._mark: str = mark # Одно подчеркивание ничего не меняет это лишь предупреждает, что не нужно трогать
        self.max_speed: int = max_speed
        self.__current_speed: int = 0 # Два подчеркивания приводит к  NameMAngling, имя переменной изменяется на _Car__current_speed 

    def __str__(self):
        return f'Марка: {self._mark}, максимальная скорость: {self.max_speed}'
    
    #@current_speed.setter  МЫ В КЛАССЕ ПИСАЛИ ПОДОБНОЕ. ЧТО ЭТО ДАЕТ? ЭТО НУЖНО В ЭТОМ ЗАДАНИ?
    def increase(self):
        if self.__current_speed + 5 <= self.max_speed:
            self.__current_speed +=5
        else:
            raise ValueError('МАКСИМАЛЬНАЯ СКОРОКСТЬ НЕ ДОЛЖНА ПРЕВЫШАТЬ max_speed')

    def decrease(self):
        if self.__current_speed - 5 >= 0:
            self.__current_speed -= 5
        else:
            raise ValueError('СКОРОСТЬ НЕ МОЖЕТ БЫТЬ МЕНЬШЕ 0')

    def get_speed(self):
        return self.__current_speed


bmw = Car('BMW',250)

for i in range(0,100):
    try:
        bmw.increase()
    except ValueError as e:
        print(e)
        break


print(bmw.get_speed())

for i in range(0,10):
    try:
        bmw.decrease()
    except ValueError as e:
        print(e)
        break  

print(bmw.get_speed())

# bmw.__current_speed = 300  здесь создается новая переменная

# print(bmw.__current_speed)

print(dir(bmw))







# Задача 7: Абстрактные классы

# Описание: Создайте абстрактный класс Shape, который имеет абстрактный метод get_area(). 
# Затем создайте классы Square и Triangle, которые наследуются от этого абстрактного класса и 
# реализуют свои версии метода get_area().

# Условия:

#  • Класс Square должен принимать длину стороны, а класс Triangle — основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.

# Каждая из этих задач поможет вам лучше понять принципы ООП, такие как инкапсуляция, наследование, 
# полиморфизм и абстракция.
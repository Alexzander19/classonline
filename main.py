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
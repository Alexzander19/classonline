class Item:
	def __init__(self, id: int, name: str, taken: bool = False):
		if 0 < id <= 1000:
			self.__id: int = id
		else:
			raise ValueError('id должно быть от 1 до 1000')
		self._name: str = name
		self.__taken: bool = taken

	@property
	def id(self) -> int:
		return self.__id

	def is_taken(self):
		return self.__taken


	def take(self):
		# def change_status(self):
	# 	self.__taken = not self.__taken
		if not self.__taken:
			self.__taken = not self.__taken
		else:
			raise Exception(f'Предмет {self.id} уже взяли')

	def bring_back(self):
		
		if self.is_taken():
			self.__taken = not self.__taken
		else:
			raise Exception(f'Предмет {self.id} на месте, что вы пытаетесь вернуть?')

	# def __str__(self):
	# 	pass
		# return '\n'.join([str(item) for item in self.__items])





class Book(Item):
	def __init__(self, id: int, name: str, author: str):
		super().__init__(id, name)
		self.__author: str = author

	def __str__(self):
		return (f'{self.id}: (Книга) {self.__author} - '
						f'{self._name} ({"Не доступен" if self.is_taken() else "Доступен"})')


class Magazine(Item):
	def __init__(self, id: int, name: str, publisher: str):
		super().__init__(id, name)
		self.__publisher: str = publisher

	def __str__(self):
		return (f'{self.id}: (Журнал) {self.__publisher} - '
						f'{self._name} ({"Не доступен" if self.is_taken() else "Доступен"})')


# def find(self, id: int) -> :
# 	# 	for item in self.__items:
# 	# 		if item.id == id:
# 	# 			return item
# 		# raise Exception(f'Предмет с id {id} не найден')
def find(items: list[Item], id: int) -> Item:
	for item in items:
		if item.id == id:
			return item
	raise Exception(f'Предмет с id {id} не найден')
	

def global_take(items: list[Item], id: int):
	find(items,id).take()
	
def global_bring_back(items: list[Item],id: int):
	find(items,id).bring_back()



# class Library:
# 	def __init__(self):
# 		self.__items: list[Book | Magazine] = []

library: list[Item] =[]

# def add(self, item: Item):
	# 	self.__items.append(item)
	
try:
    library.append(Book(1, 'Договориться можно обо всем', 'Гэвин Кеннади'))
    library.append(Book(2, 'Финансист', 'Теодор Дрейзер'))
    library.append(Magazine(3, 'Топ 100 миллионеров', 'Forbes'))
    library.append(Magazine(-2, 'Топ 100 лузеров', 'На районе'))
    library.append(Book(4, 'ФЛОРИСТ', 'Теодор Дроуер'))
except ValueError as e:
	print(e)


for item in library:
    print(item)
	

# library.take(1)

global_take(library, 1)

print('--------------')
# print(library)
for item in library:
    print(item)

print('--------------')
# library.take(2)

global_take(library, 2)



for item in library:
    print(item)


print('--------------')
# library.bring_back(3)
global_bring_back(library,2)

for item in library:
    print(item)

print('--------------')
try:
    global_bring_back(library,2)
except Exception as e:
	print(e)


# print('--------------')
# print(library)

# print('--------------')
# library.bring_back(3)

# print('--------------')
# print(library)



	

		
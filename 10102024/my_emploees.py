# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника,
# удаление сотрудника, поиск сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.
from __future__ import annotations
from abc import abstractmethod
from datetime import date


file_name: str = 'empl.txt'

class Emploeer:
    def __init__(self, id: int):
        self.__id: int = id
        self._name: str = ''
        self._surname: str = ''
        self._birthday: str = ''

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self._name

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def birthday(self) -> str:
        return self._birthday


    def __str__(self):
        return f'{self.id}: {self.name} {self.surname} {self.birthday}'

    @staticmethod
    def check_date(input_date: str) -> str:
        if False:
            raise ValueError('Некорректный формат даты')
        # приводим введенную строку к формату класс date
        return str(input_date)
    

    @staticmethod
    def check_name(input_name: str) -> str:
        if False:
            raise ValueError('Некорректный формат имени или фамилии')
        return input_name

    def add(self, name: str, surname: str, birthday: str):

        try:
            true_name: str = self.check_name(name)
            true_surname: str = self.check_name(surname)
            true_birthday: str = self.check_date(birthday)
        except ValueError as er:
            print(er)

        self._birthday = true_birthday
        self._surname = true_surname
        self._name = true_name

    def change(self, name: str , surname :str , birthday: str ):
        try:
            if name != '':
                true_name: str = self.check_name(name)

            if surname != '':
                true_surname: str = self.check_name(surname)

            if birthday != '':
                true_birthday: str = self.check_date(birthday)

        except ValueError as er:
            print(er)
        if name != "":
            self._name = true_name  
        if surname != '':
            self._surname = true_surname
        if birthday != '':
            self._birthday = true_birthday

    def input_new(self):
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        birthday = input('Введите дату рождения: ')

        self.add(name,surname,birthday)

    def input_change(self):
        c_name = input('Введите новое имя (Enter - пропустить): ')
        c_surname = input('Введите новую фамилию (Enter - пропустить): ')
        c_birthday = input('Введите новую дату рождения (Enter - пропустить): ')

        change_str = ''
        if c_name != '':
            change_str += f'{self.name} на {c_name}'
        if c_surname != '':
            change_str += f', {self.surname} на {c_surname}'
        if c_birthday != '':
            change_str += f', {self.birthday} на {c_birthday} '

        if change_str != '':
            yes_change = input(f'Вы хотите изменить: {change_str}? (Y - подтвердить): ' )

        if yes_change == 'Y':
            self.change(c_name,c_surname,c_birthday)
        
        
            

class Office:
    def __init__(self):
        self._emploeers: list[Emploeer] = []

    def next_id(self) -> int:
        max_id: int = 0
        for i in self._emploeers:
            if max_id < i.id:
                max_id = i.id
        return max_id + 1 # индексация начнется с 1
    
    def add(self) -> bool:
        emploeer = Emploeer(self.next_id())
        emploeer.input_new()
        self._emploeers.append(emploeer)
        return 1
    
    def find(self,to_find: int | str) -> Emploeer | None:


        try:
            typed_find: int = int(to_find)
        except:
            typed_find: str = str(to_find)

        if isinstance(typed_find, int):
            for emploeer in self._emploeers:
                if emploeer.id == typed_find:
                    return emploeer
        elif isinstance(typed_find,str):
            for emploeer in self._emploeers:
                if emploeer.surname == typed_find:
                    return emploeer
        else:
            pass
        return None

    def print_all(self) -> int:
        for emploeer in self._emploeers:
            print(emploeer)
        return 1

        
    
    def change(self):
        who = input('Напишите ID или Фамилию сотрудника, данные о котором нужно изменить: ')

        emploeer_to_change = self.find(who)

        if emploeer_to_change != None:
            emploeer_to_change.input_change()
        else:
            print('Такого сотрудника не найдено')

    def delete(self):
        who = input('Напишите ID или фамилию сотрудника, которого нужно удалить: ')

        emploeer_to_delete = self.find(who)

        if emploeer_to_delete != None:
            if input(f' Удалить {emploeer_to_delete.name} {emploeer_to_delete.surname} {emploeer_to_delete.birthday}?') == 'Y':
                self._emploeers.remove(emploeer_to_delete)
        else:
            print('Такого сотрудника не найдено')

    def save_in_file(self,file_name: str):

        with open(file_name,'w',encoding='utf-8') as f:
            count = 0
            
            for emploeer in self._emploeers:
                string = ''
                string = string + str(emploeer.id) + ' ' +emploeer.name + ' ' + emploeer.surname + ' ' + emploeer.birthday
                if count > 0:
                    f.write('\n') # Чтобы не добавлять переход на новую строку в конце файла
                f.write(string)
                count += 1
            print(f'Записано: {count} строк.')
        return 0
    
    @staticmethod
    def load_from_file(file_name: str) -> Office:

        office = Office()

        try:
            with open(file_name,'r',encoding='utf-8') as f:
               
                lines :list[str] = f.read().split('\n')
                # print(lines)

                for line in lines:
                    # print(line)
                    words: list[str] = line.split() # разделение по пробелу( по умолчанию)
                    # print(words)
                    emploeer = Emploeer(int(words[0]))
                    emploeer.add(words[1],words[2],words[3])
                    office._emploeers.append(emploeer)
                         
        except:
            print('Ошибка чтения файла данных.') 
        return office




    
    def menu(self):

        menu_list = {
            1: ['1 добавить сотрудника', self.add ],
            2: ['2 редактировать сотрудника', self.change],
            3: ['3 удалить сотрудника',self.delete],
            4: ['4 Вывести инфо обо всех',self.print_all],
            5: ['5 Сохранить', lambda : self.save_in_file(file_name) + 1],
            6: ['6 Сохранить и выйти',lambda : self.save_in_file(file_name)],
            7: ['7 Выйти без сохранения', lambda: 0]
                
        }
        
        print('Здраствуйте, это система "Мой офис"!')
       

        choose: int = 1

        while choose != 0:

            print('******************************************')
            for i in range(1, len(menu_list)+1):

                print(menu_list[i][0])

            print('******************************************')
            choose =  input('Выберите нужное действие: ')
            try:
                choose = menu_list[int(choose)][1]()
                
            except:
                print('Такого пункта нет. Попробуйте снова.') # Есть недостаток без типа ошибки - туда попадают любые и ничего о них не сообщается
            

   

of = Office.load_from_file(file_name)
of.menu()



    
# em = Emploeer(1)
# em.add('Иван', 'Иванов','08.11.1984')

# em.input_change()
# print(em)





    

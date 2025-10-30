class Person:
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def get_info(self) -> tuple[str, str]:
        return (self.name, self.role)

    def __str__(self) -> str:
        pass



class Student(Person):

    def __init__(self, name: str, course: int):
        super().__init__(name=name, role='студент')
        self.course = course
        
    def __str__(self) -> str:
        return f'Роль: {self.role}, Имя {self.name}, Курс: {self.course}.'

   
class Teacher(Person):

    def __init__(self, name: str, position: str):
        super().__init__(name=name, role='преподаватель')
        self.position = position
    
    def __str__(self) -> str:
        return f'Роль: {self.role}, Имя {self.name}, Позиция: {self.position}.'


class Discipline:

    def __init__(self, teacher: Teacher, students: list[Student], name: str):
        self.teacher = teacher
        self.students = students
        self.name = name

    def __str__(self) -> str:
        students = [s.get_info()[0] for s in self.students]
        return f'Дисциплина: "{self.name}". Преподаватель: {self.teacher.get_info()[0]}. Студенты: ({", ".join(students)})"'
    

def main():
    all_objects = []
    menu = '''
    1. Создание нового объекта "Discipline".
    2. Вывод объектов.
    3. Вывод конктреного объекта.
    0. Завершение работы прграммы.
    '''

    while True:
        print(menu)
        menu_item = int(input("Введите номер команды: ").strip())

        if not (0 <= menu_item <= 4):
            print("Вы ввели неверную команду, попробуйте ещё раз.")
            continue
        
        match menu_item:
            case 0:
                print("Программа завершила свою работу.")
                break

            case 1:
                teacher = input("Введите ФИО преподавателя и его должность через запятую: ").strip().split(', ')
                discipline = input("Введите Дисциплину: ").strip()
                students = input("ФИО студентов и их курс через запятую: ").strip().split(', ')

                if len(students) == 0:
                    print("Должен быть указан хотя бы один студент. Попробуйте ещё раз.")
                    continue
                
                students = [Student(s[0:-2], int(s[-1])) for s in students]
                teacher = Teacher(teacher[0], teacher[1])
                discipline = Discipline(teacher, students, discipline)
                all_objects.append(discipline)

                print("Объект успешно создан!")
                continue

            case 2:
                if len(all_objects) == 0:
                    print('Нет ниодного созданного объекта. Поробуйте для начала ввести команду 1.')
                    continue
                
                print("Вывод содержимого всех объектов.")
                for obj in all_objects:
                    print(obj)
                
                continue

            case 3:
                inx = int(input("Введите индекс интересующего объекта: ").strip())

                if not(0 <= inx <= len(all_objects)):
                    print("Индекс выходит за допустимы диапазон. Попробуйте ещё раз.")
                    continue
                    
                print(f'Название дисциплины: {all_objects[inx].name}')
                print(f'Участники:')
                print(f'{all_objects[inx].teacher.__str__()}')
                for s in all_objects[inx].students:
                    print(s.__str__())
                
                continue
                
if __name__ == "__main__":
    main()
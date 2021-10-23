"""
"Нужно описать при помощи классов следующие сущности.
Студент - имеет имя, возраст, пол, номер класса в котором обучается,
название специальности на которую обучается;
Преподаватель - имеет имя, возраст, пол, наименование преподаваемого предмета, стаж работы;

И студент и преподаватель имеют метод think, в результате которого можно получить
случайное число и метод speak(t), который увеличивает t на 10.
В случае преподавателя метод speak увеличивает t на 10,
 а так же прибавляет стаж работы преподавателя.  Так же студент имеет метод sum(a,b),
 который складывает 2 числа.
Преподаватель имеет метод answer(v) -> в результате которого возвращает
v возведенное в 10ю степень."
"""

from random import randint


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def think():
        return randint(1, 100)

    def speak(self, t):
        return t + 10


class Student(Person):

    def __init__(self, name, age, gender, num_class):
        super().__init__(name, age, gender)
        self.num_class = num_class

    @staticmethod
    def sum(a, b):
        return a + b


class Teacher(Person):
    def __init__(self, name, age, gender, name_class, experience):
        super().__init__(name, age, gender)
        self.name_class = name_class
        self.experience = experience

    def speak(self, t):
        self.experience += 1
        return super().speak(t)

    @staticmethod
    def answer(v):
        return v**10


if __name__ == "__main__":
    first_teacher = Teacher("Sofia", 34, "F", "Сhemistry", 5)
    randint_num = first_teacher.think()
    print("randint_num", randint_num)
    print(first_teacher.name, first_teacher.experience)
    print(first_teacher.speak(randint_num))
    print(first_teacher.name, first_teacher.experience)
    print(first_teacher.think())

# teachers_and_sdudents.py
import random
class person():
    """Модель простого человека"""
def __init__(self, name, age, gender):
        """Инициализирует атрибуты имя, возраст,пол."""
        self.name = name
        self.age = age
        self.gender = gender
        
def think(self):
    """Человек умеет думать."""
# простой человек не очень умеет думать, т.к. возвращает случайное число от 1 до 1000
    return random.randint(1,1000)

def speak(self,t):
    """Человек умеет говорить: умножает t на 10"""
    return t*10

class student(person):
    """Модель студента"""
def __init__(self, klassnumber, special):
    """Инициализирует атрибуты студента: номер класса,в котором учится студент, название специальности."""
    self.klassnumber = klassnumber
    self.special = special

def sum(a,b):
    """Студент очень быстро складывает 2 любых числа"""
    return a+b

class teacher(person):
    """Модель преподавателя"""
def __init__(self, subject, work):
    """Инициализирует атрибуты преподавателя: предмет, стаж работы."""
    self.subject = subject
    self.work = work
    
def answer(v):
    """Преподаватель очень быстро возводит любое число в 10-степень"""    
    return v**10

def speak(self,t):
    """Преподаватель говорит намного сложнее, чем простой человек"""
# Переопределяем метод из родительского класса
# В случае преподавателя метод speak увеличивает t на 10, а так же прибавляет стаж работы преподавателя
    return t+10+self.work

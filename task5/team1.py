from random import randint

class Human:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def think(self):
		return randint(0, 100)

	def speak(self, t):
		return t + 10

class Student(Human):
	def __init__(self, name, age, sex, group, speciality):
		super().__init__(name, age, sex)
		self.group = group
		self.speciality = speciality
	
	def sum(self, a, b):
		return a + b

class Teacher(Human):
	def __init__(self, name, age, sex, subject, experience):
		super().__init__(name, age, sex)
		self.subject = subject
		self.experience = experience

	def speak(self, t):
		return super().speak(t) + self.experience

	def answer(self, v):
		return v ** 10

s = Student('A', 18, 'M', 431, 'CS')
print(s.__dict__)
print(s.speak(0))
print(s.think())
print(s.sum(192, -22))

print()

t = Teacher('B', 35, 'F', 'python', 15)
print(t.__dict__)
print(t.speak(0))
print(t.think())
print(t.answer(2))
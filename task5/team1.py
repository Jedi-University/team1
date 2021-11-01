from random import randint

class Human:
	name = None
	age = None
	sex = None

	#def __init__(self, *args):
	#	self.name = args[0]
	#	self.age = args[1]
	#	self.sex = args[2]

	def think(self):
		return randint(0, 100)

	def speak(self, t):
		return t + 10

class Student(Human):
	group = None
	speciality = None

	def __init__(self, *args):
		self.name = args[0]
		self.age = args[1]
		self.sex = args[2]
		#super().__init__(args[:2])
		self.group = args[3]
		self.speciality = args[4]
	
	def sum(self, a, b):
		return a + b

class Teacher(Human):
	subject = None
	experience = None

	def __init__(self, *args):
		self.name = args[0]
		self.age = args[1]
		self.sex = args[2]
		#super().__init__(args[:2])
		self.subject = args[3]
		self.experience = args[4]

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
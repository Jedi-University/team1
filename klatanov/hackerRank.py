def hello_world():
	print("Hello, World!")

def if_else(n):
	if n % 2 != 0 or (n % 2 == 0 and n in range(6, 21)):
		print("Weird")
	elif (n % 2 == 0 and n in range(2, 6)) or (n % 2 == 0 and n > 20):
		print("Not Weird")

def arithmetic_operators(a, b):
	print(a + b)
	print(a - b)
	print(a * b)

def division(a, b):
	print(a // b)
	print(a / b)

def loops(n):
    for i in range(0, n):
        print(i ** 2)

#write-a-function
def is_leap(year):
    leap = False
    if year % 4 == 0 or (year % 100 == 0 and year % 400 != 0):
        leap = True
    return leap
#year = int(input())
#print(is_leap(year))

def print(n):
	for i in range(n):
		print(i + 1, end='')
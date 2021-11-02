#Результат:
#["xa", "xb", "xc"]
#task3.1
#f = func("a", "b", "c")
#print(f("x"))

#Результат:
#[1,2,3,4,5,6,0,0,0,0,"a", "b", "c"]
print('task3.2:')
l = [[1,2,3,4,5,6], [0,0,0,0], ["a", "b", "c"]]
for i in range(3):
	l.extend(l[i])
l = l[3:]		
print(l)
print()

#Результат:
#"100h - 200z"
print('task3.3:')
def a(x,y):
	print(f'{x} - {y}')
	
def caller(func, c, j):
	return lambda x,y: func(c+x, j+y)
f = caller(a, '100', '200')
f('h', 'z')
from functools import reduce 

#       1. дан следующий код

#f = func(""a"", ""b"", ""c"")
#print(f(""x""))
# Результат должен быть^ [""xa"", ""xb"", ""xc""]


f=lambda j: [j+"a", j+"b", j+"c"]
print(f("x"))

#       2. дан лист листов

#l = [[1,2,3,4,5,6], [0,0,0,0], [""a"", ""b"", ""c""]]
#Необходимо написать код который превратит его в простой лист 
#[1,2,3,4,5,6,0,0,0,0,""a"", ""b"", ""c""]
#для решения данной задачи нельзя использовать доп массива
# Результат должен быть^ [""xa"", ""xb"", ""xc""]

l = [[1,2,3,4,5,6], [0,0,0,0], ["a", "b", "c"]]
print(reduce(lambda x,y:x+y,l))

#       3. написать реализацию метода caller
#Результат: "100h - 200z"

def a(x,y):
    print(f"{x} - {y}")
    
f = lambda x,y:a('100'+x,'200'+y)
f("h", "z")


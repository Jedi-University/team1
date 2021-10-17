# метод super_range, получить из объекта  длину для итерирования используя логику генератора , не создаёт массив
# генерирует значение каждый раз при вызове

# def super_range(i):
#   pass

# for x in super_range(100):
#   print(x)

def super_range(n):
    i=-1
    while i<n-1:
        i+=1
        yield i
        
l= int(input('Input generator number: '))
if l>0:
    for x in super_range(l):
        print(x)
else :
    print('Input positiv number!')


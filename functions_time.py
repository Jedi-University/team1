#Сделать декоратор который может считать время выполнения функции
#и выводить его в консоль, нужно сделать возможным передать min=True/False,
#что позволят выводить время в минутах в случае True
# и в секундах в случае False
def timing(func):
    import time
    def wrapper(*args):
# определяем функцию-обертку
        begintime = time.time()
        print(begintime)
        func(*args)
        endtime = time.time()
        print(endtime)
        durationtime=endtime-begintime
        edizm='секунд'
        if min:
            durationtime=durationtime/60
            edizm='минут'
        print('Время выполнения ('+ edizm+'):'+'{}'.format(durationtime))
    return wrapper

@timing
def exponentiation(x,y):
    print(str(x)+' в степени '+str(y)+' равно ', x**y)


min=True
x1=25
y1=10
exponentiation(x1,y1)



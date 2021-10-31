#Сделать декоратор который может считать время выполнения функции
#и выводить его в консоль, нужно сделать возможным передать min=True/False,
#что позволят выводить время в минутах в случае True
# и в секундах в случае False
def timing(min):
#min- определяет единицу измерения (True- в минутах, False - в секундах)
    def actual_timing(func):
        import time
        def wrapper(*args,**kwargs):
# определяем функцию-обертку
            begintime = time.time()
            func(*args)
            endtime = time.time()
            print(begintime)
            print(endtime)
            durationtime=endtime-begintime
            edizm='секунд'
            if min:
                durationtime=durationtime/60
                edizm='минут'
            print('Время выполнения ('+ edizm+'):'+'{}'.format(durationtime))
        return wrapper
    return actual_timing

@timing(False)
#True- в минутах, False - в секундах
def exponentiation(x,y):
#возводит x в степень y
    print(str(x)+' в степени '+str(y)+' равно ', x**y)

x1=25
y1=10
exponentiation(x1,y1)



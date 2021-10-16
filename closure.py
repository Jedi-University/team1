"""
Практика
 с контекстом

1. дан следующий код
f = func(""a"", ""b"", ""c"")
print(f(""x""))
Результат должен быть
[""xa"", ""xb"", ""xc""]

2. дан лист листов
l = [[1,2,3,4,5,6], [0,0,0,0], [""a"", ""b"", ""c""]]
Необходимо написать код который превратит его в простой лист
[1,2,3,4,5,6,0,0,0,0,""a"", ""b"", ""c""]
для решения данной задачи нельзя использовать доп массива
"
"""

from functools import reduce


# Task № 1
def func(*args: str):
    def inner_func(value: str) -> list[str]:
        return [f"{value}{item}" for item in args]
    return inner_func


# Task № 2
def func_spread(lists):
    return reduce(lambda el_prev, el: el_prev + el, lists)


# Task 3
def a(x, y):
    print(f"{x} - {y}")


def caller(func, x, j):
    def inner(c, e):
        func(x+c, j+e)
    return inner


if __name__ == "__main__":
    # Run first task
    f = func("a", "b", "c")
    print(f("x"))

    # Run second task
    lists = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0], ["a", "b", "c"]]
    print(func_spread(lists))

    # Run third task
    f = caller(a, "100", "200")
    f("h", "z")

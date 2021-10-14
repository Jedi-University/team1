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


# Task № 1
def func(*args: str):
    def inner_func(value: str) -> list[str]:
        return [f"{value}{item}" for item in args]
    return inner_func


# Task № 2
def func_spread():
    lists = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0], ["a", "b", "c"]]
    print(lists)
    print(id(lists))

    def inner_func():
        length_list = len(lists)
        for inx in range(length_list):
            lists.extend(lists[inx])
        del lists[:length_list]
        print(lists)
        print(id(lists))
    return inner_func


if __name__ == "__main__":
    # Run first task
    f = func("a", "b", "c")
    print(f("x"))

    # Run second task
    list_spread = func_spread()
    list_spread()

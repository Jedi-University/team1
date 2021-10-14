"""
Метод super_range, получить из объекта  длину для
итерирования используя логику генератора , не создаёт массив
генерирует значение каждый раз при вызове

def super_range(i):
  pass
for x in super_range(100):
  print(x)
"""


def super_range(*args):
    """Return function range"""

    for arg in args:
        if not isinstance(arg, int):
            return print("Введите число")

    count_args = len(args)

    if count_args == 1:
        start = 0
        while start < args[0]:
            start += 1
            yield start - 1
    elif count_args == 2:
        start = args[0]
        end = args[1]
        while start < end:
            start += 1
            yield start - 1
    elif count_args == 3:
        start = args[0]
        end = args[1]
        step = args[2]
        while start < end:
            start += step
            yield start - step


if __name__ == "__main__":

    for item in super_range(1, 100, 5):
        print(item)

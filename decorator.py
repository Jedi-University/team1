"""
Сделать параметрезированый декоратор
"""
import time
import requests


def timing(func):
    def inner(*args, **kwargs):
        print("Start timing.")
        start_time = time.time()
        func(*args, **kwargs)
        print("Stop timing.")
        print(f"Time ran the function {func}: {round(time.time() - start_time, 2)} sec.")
    return inner


def timing_with_param(quatity_iter=1):
    def wrapper(func):
        def inner_func(*args, **kwargs):
            print("Начало замера времени.")
            start_time = time.time()
            for i in range(quatity_iter):
                func(*args, **kwargs)
            print("Конец замера времени.")
            print(f"Время выполнение функции {func}: {round(time.time() - start_time, 2)}")

        return inner_func
    return wrapper


@timing_with_param(5)
def main(*args, **kwargs):
    print(args, kwargs)


@timing_with_param(2)
def req_api(url):
    answer = requests.get(url)
    print(answer.status_code)


if __name__ == "__main__":
    main("Hello")

    req_api("https://github.com")

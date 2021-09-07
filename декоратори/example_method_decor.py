from datetime import datetime
import time


def elapsed(func):
    def wrapper(a, b, delay=0):
        start = datetime.now()
        func(a, b, delay)
        end = datetime.now()
        elapsed = (end - start).total_seconds() * 1000
        print(f'>> функция {func.__name__} время выполнения (ms): {elapsed}')

    return wrapper


@elapsed
def add_with_delay(a, b, delay=0):
    print('сложить', a, b, delay)
    time.sleep(delay)
    return a + b


print('старт программы')
add_with_delay(10, 20)
add_with_delay(10, 20, 1)
print('конец программы')

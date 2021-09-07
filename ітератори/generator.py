# В процессе вызова генератора функция будет приостанавливать и
# сохранять всю текущую информацию о работе каждый раз, когда она сталкивается с yield,
# возвращать значение yield и продолжать работу с текущей позиции при следующем выполнении метода next ().
import sys


def fibonacci(n):  # генераторная функция-Фибоначчи
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f - итератор, сгенерированный генератором

while True:
    try:
        print(next(f))
    except StopIteration:
        print('exit')
        sys.exit()

def decorator(func):
    '''Декоратор'''

    def decorated():
        '''Функция Decorated'''
        func()

    return decorated


@decorator
def wrapped():
    '''Оборачиваемая функция'''
    print('функция wrapped')


print('старт программы...')
print(wrapped.__name__)
print(wrapped.__doc__)
print('конец программы')
# ___________out__________
# старт программы...
# decorated
# Функция Decorated
# конец программы

from functools import wraps


def decorator(func):
    '''Декоратор'''

    @wraps(func)
    def decorated():
        '''Функция Decorated'''
        func()

    return decorated


@decorator
def wrapped():
    '''Оборачиваемая функция'''
    print('функция wrapped')


print('старт программы...')
print(wrapped.__name__)
print(wrapped.__doc__)
print('конец программы')
# _______________out______________
# старт программы...
# wrapped
# Оборачиваемая функция
# конец программы

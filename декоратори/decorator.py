def decorator_1(func):
    print('декоратор 1')

    def wrapper():
        print('перед функцией')
        func()

    return wrapper


def decorator_2(func):
    print('декоратор 2')

    def wrapper():
        print('перед функцией')
        func()

    return wrapper

# equal a = decorator_1(decorator_2(wrapped))
@decorator_1
@decorator_2
def basic_1():
    print('basic_1')


@decorator_1
def basic_2():
    print('basic_2')


print('>> старт')
basic_1()
basic_2()
print('>> конец')

# вихід
# декоратор 2
# декоратор 1
# декоратор 1
# >> старт
# перед функцией
# перед функцией
# basic_1
# перед функцией
# basic_2
# >> конец

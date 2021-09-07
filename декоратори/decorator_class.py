# Добавив метод __call__ в класс, его можно превратить в вызываемый объект.
# А поскольку декоратор — это всего лишь функция, то есть, вызываемый объект,
# класс можно превратить в декоратор с помощью функции __call__.

class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self):
        print('> перед вызовом класса...', self.func.__name__)
        self.func()
        print('> после вызова класса')


@Decorator
def wrapped():
    print('функция wrapped')


print('>> старт')
wrapped()
print('>> конец')

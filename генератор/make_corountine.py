# співпрограма яка ініціює запуск генератора-калькулятора
def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen

    return wrap


# генератор який приймає два числа, додає їх та повертає значення, разом з тим зберігає значення
# у списку. Повертає усі збережені значення якщо перший аргумент 'h'
@coroutine
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print
            history
            continue
        result = x + y
        print
        result
        history.append(result)

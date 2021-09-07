import logging


def logger(func):
    log = logging.getLogger(__name__)

    def wrapper(a, b):
        log.info("Вызов функции ", func.__name__)
        ret = func(a, b)
        log.info("Вызвана функция ", func.__name__)
        return ret

    return wrapper


@logger
def add(a, b):
    print('a + b:', a + b)
    return a + b


print('>> старт')
add(10, 20)
add(20, 30)
print('>> конец')

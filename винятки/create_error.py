import sys


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


# Пользовательское исключение
class InputError(Error):
    """Exception raised for errors in the input.
   Attributes:
       expression -- input expression in which the error occurred
       message -- explanation of the error
   """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


try:
    print('code start running...')
    # raise InputError('input()', 'input error')
    # ValueError
    # int('a')
    # TypeError
    s = 1 + 'a'
    dit = {'name': 'john'}
    # KeyError
    print(dit['1'])
except InputError as ex:
    print("InputError:", ex.message)
except TypeError as ex:
    print('TypeError:', ex.args)
    pass
except (KeyError, IndexError) as ex:
    # """Поддерживает обработку нескольких исключений одновременно, заключая скобки в кортежи"""
    print(sys.exc_info())
except:
    # """Поймать другое неуказанное исключение"""
    print("Unexpected error:", sys.exc_info()[0])
    # Повышение используется, чтобы вызвать исключение
    raise RuntimeError('RuntimeError')
else:
    """Когда нет исключения, выполняется условие else"""
    print('"else" предложение ...')
finally:
    """В любом случае, без исключения, наконец"""
    print('finally, ending')

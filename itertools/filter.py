# Створіть ітератор, який фільтрує елементи з ітерабельних,
# повертаючи лише ті, для яких є предикат True.
# Якщо предикат є None, поверніть істинні елементи.
# Приблизно еквівалентно:
from itertools import filterfalse
from itertools import dropwhile
from itertools import takewhile


def ifilter(predicate, iterable):
    # ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
    if predicate is None:
        predicate = bool
    for x in iterable:
        if predicate(x):
            yield x


data = list(filterfalse(lambda i: i == 0, [1, 2, 3, 0, 4, 5, 1]))
print(data)
# [1, 2, 3, 4, 5, 1]

data = list(dropwhile(lambda i: i != 0, [1, 2, 3, 0, 4, 5, 1]))
print(data)
# [0, 4, 5, 1]

data = list(takewhile(lambda i: i != 0, [1, 2, 3, 0, 4, 5, 1]))
print(data)
# [1, 2, 3]

# Створіть ітератор, який повертає послідовні ключі та групи з ітератора .
# Ключ є функцією обчислення значення ключа для кожного елемента.
# Якщо ключ не вказано або є None, за замовчуванням використовується функція ідентифікації
# та повертається елемент без змін.
# Як правило, ітерабельність потрібно вже відсортувати за тією ж ключовою функцією.

from itertools import groupby

data = [1, ]
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))  # Store group iterator as a list
    uniquekeys.append(k)


class groupby(object):
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def next(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)  # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))

    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            self.currvalue = next(self.it)  # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)

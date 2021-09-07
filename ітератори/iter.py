# Итераторы могут быть пройдены циклом for:
li = [1, 2, 3]
it = iter(li)
for val in it:
    print(val)

# Итераторы также могут использовать функцию next () для доступа к следующему значению элемента:
import sys

li = [1, 2, 3, 4]
it = iter(li)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


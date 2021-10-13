# Лямбда - это просто выражение, и тело функции намного проще, чем def.
# Тело лямбды - это выражение, а не блок кода.
# Только ограниченная логика может быть заключена в лямбда-выражения.
# Лямбда-функция имеет собственное пространство имен
# и не может получить доступ к параметрам вне своего списка параметров
# или в глобальном пространстве имен. Хотя лямбда-функции, похоже, пишут только одну строку,
# они не эквивалентны встроенным функциям C или C ++.
# Цель последнего - повысить эффективность запуска небольших функций без использования стековой памяти.

# Синтаксический формат
# lambda [arg1 [,arg2,.....argn]]:expression

# this will return sum of two elements
s = (lambda x, y: x + y)(2, 3)

# out will be list where each element is multiplied by 2
o = list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))

# each element in list strs will be filtered by len, if len > 3 than this element will be add to new list
strs = ['apple', 'and', 'a', 'donut']
f = list(filter(lambda s: len(s) > 3, strs))

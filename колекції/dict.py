dis = {'a': 1, 'b': [1, 2, 3]}
print(dis['b'][2])

# змінити словник
dis = {'a': 1, 'b': [1, 2, 3], 9: {'name': 'hello'}}
dis[9]['name'] = 999
print(dis)
# {'a': 1, 9: {'name': 999}, 'b': [1, 2, 3]}

# видалити словник
dis = {'a': 1, 'b': [1, 2, 3], 9: {'name': 'hello'}}
del dis[9]['name']
print(dis)
# {'a': 1, 9: {}, 'b': [1, 2, 3]}

del dis # удалить словарь
# print(dis)
# NameError dis in not found

dic1 = {'a': 'a'}
dic2 = {9: 9, 'a': 'b'}
dic1.update(dic2)
print(dic1)
# {'a': 'b', 9: 9}

# Конструктори словника
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

dis = {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

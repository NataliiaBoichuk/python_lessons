import pickle

# Модуль pickle реализует сериализацию и десериализацию данных в Python.
# pickle поддерживает любой тип данных, включая встроенные типы данных,
# функции, классы, объекты и многое другое.

# Записать объект данных в файл после сериализации
# pickle.dump(obj, file, protocol=None, fix_imports=True)

# Чтение содержимого из файла и десериализация
# pickle.load(file, fix_imports=True, encoding='ASCII', errors='strict')

# Возвращает инкапсулированный объект как объект байта, без записи в файл
# pickle.dumps(obj, protocol=None, fix_imports=True)

# Считать инкапсулированный объект из объекта байта и вернуть
# pickle.loads(bytes_object, fix_imports=True, encoding='ASCII', errors='strict')

#####################################################################################
data = [1, 2, 3]
# Сериализация данных и возврат в виде объекта байта
dumps_obj = pickle.dumps(data)
print('pickle.dumps():', dumps_obj)
# Десериализовать данные из байтового объекта
loads_data = pickle.loads(dumps_obj)
print('pickle.loads():', loads_data)
filename = 'data.log'
# Сериализация данных в файл
with open(filename, 'wb') as file:
    pickle.dump(data, file)
# Загрузка и десериализация из файла
with open(filename, 'rb') as file:
    load_data = pickle.load(file)
    print('pickle.load():', load_data)

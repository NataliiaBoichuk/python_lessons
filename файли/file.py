filename = 'data.log'
# Открыть файл (+ чтение и запись в режиме добавления)
# Открытие файла с ключевым словом with автоматически закроет ресурс файла
with open(filename, 'w+', encoding='utf-8') as file:
    print('Имя файла: ()'.format(file.name))
    print('Кодировка файла: ()'.format(file.encoding))
    print('Режим открытия файла: ()'.format(file.mode))
    print('Файл доступен для чтения: ()'.format(file.readable()))
    print('Написать файл: ()'.format(file.writable()))
    print('Положение указателя файла: ()'.format(file.tell()))
    # Написать контент
    num = file.write("Содержимое первой строки \n")
    print('Записать в файл {} символов ')
    # Указатель файла находится в конце файла, поэтому нет содержимого
    print(file.readline(), file.tell())
    # Изменить указатель файла на заголовок файла
    file.seek(0)
    # После изменения указателя файла прочитайте первую строку
    print(file.readline(), file.tell())
    # Но изменение указателя файла не повлияет на позицию записи
    file.write('вторая запись \n')
    # Указатель файла возвращается в конец файла
    print(file.readline(), file.tell())
    # file.read () Считать указанную длину символов из текущей позиции указателя файла
    file.seek(0)
    print(file.read(9))
    # Разделить файл на строку, вернуть список строк
    file.seek(0)
    print(file.readlines())
    # Перебирать файловые объекты, по одному элементу в строке
    file.seek(0)
    for line in file:
        print(line)
    # Закрыть файловые ресурсы

if not file.closed:
    file.close()

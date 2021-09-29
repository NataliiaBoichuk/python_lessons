# генератор - це функція, яка повертає об’єкт (ітератор), по якому ми можемо перебирати (одне значення за раз).
# генератор який віддає по одному рядку з файлу, якщо рядків немає тоді виходить з файлу
def read_file_line_by_line(file_name):
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line

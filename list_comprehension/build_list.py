# new_list = [expression for member in iterable]

# підняти до квадрату кожне парне число до 10
squares = [i * i for i in range(10) if i % 2 == 0]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# додати число позитивне, якщо негативне додати нуль
prices = [i if i > 0 else 0 for i in original_prices]

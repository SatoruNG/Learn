data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, int):  # Если элемент - целое число
            total_sum += item
        elif isinstance(item, str):  # Если элемент - строка
            total_sum += len(item)
        elif isinstance(item, list):  # Если элемент - список
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для списка
        elif isinstance(item, dict):  # Если элемент - словарь
            total_sum += calculate_structure_sum(item.keys())  # Суммируем длины ключей
            total_sum += calculate_structure_sum(item.values())  # Суммируем значения
        elif isinstance(item, tuple):  # Если элемент - кортеж
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для кортежа
        elif isinstance(item, set):  # Если элемент - множество
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для множества

    return total_sum

result = calculate_structure_sum(data_structure)
print(result)
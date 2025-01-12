from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Примеры вызова функций
result1 = fake_divide(69, 3)   # Ожидаем 23.0
result2 = fake_divide(3, 0)    # Ожидаем 'Ошибка'
result3 = true_divide(49, 7)   # Ожидаем 7.0
result4 = true_divide(15, 0)   # Ожидаем inf

# Вывод результатов в консоль
print(result1)
print(result2)
print(result3)
print(result4)
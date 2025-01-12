def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов внутренней функции
    inner_function()

# Вызов внешней функции
test_function()
#inner_function() - Ошибка: Не найдена функция
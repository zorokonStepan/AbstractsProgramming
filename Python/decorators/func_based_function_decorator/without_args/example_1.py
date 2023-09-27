def simple_decorator(func):
    """внешняя функция с аргументом"""

    def inner():
        """внутренняя функция — модификатор аргумента func"""
        print('Начало работы декоратора...')
        func()
        print('Декоратор отработал!')

    return inner  # возвращение внутренней функции как объекта


def print_hi():
    print(f'Это функция, которую задекорировали')


print_hi()  # вызов недекорированной функции
print('---------------------')

# в декоратор отправляется функция для декорирования изменённая (декорированная) функция принимается по ссылке
# на объект декорирования ...
print_hi = simple_decorator(print_hi)
# ... и выполняется
print_hi()

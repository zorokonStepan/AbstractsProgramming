class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self, a, b):
        print('> до вызова из класса...', self.func.__name__)
        self.func(a, b)
        print('> после вызова из класса')


@Decorator
def wrapped(a, b):
    print('функция wrapped:', a, b)


print('>> старт')
wrapped(10, 20)
print('>> конец')

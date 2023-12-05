def closure(*args, **kwargs):
    def inner():
        print(*args, *kwargs.values())
    return inner


f = closure(1, 2, x=3, y=4)

f()

# 1 2 3 4

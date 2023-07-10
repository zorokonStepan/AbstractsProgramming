def decorator1(func):
    def wrap(*args, **kwargs):
        print('decorator1')
        print(args[0] * 2)
        return func(*args, **kwargs)
    return wrap


def decorator2(func):
    def wrap(*args, **kwargs):
        print('decorator2')
        print(args[0] * 3)
        return func(*args, **kwargs)
    return wrap


def decorator3(func):
    def wrap(*args, **kwargs):
        print('decorator3')
        print(args[0] * 4)
        return func(*args, **kwargs)
    return wrap


@decorator1
@decorator2
@decorator3
def test_func(num: int):
    print(num)


if __name__ == "__main__":
    test_func(5)

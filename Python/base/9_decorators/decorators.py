def decorator1(func):
    def wrap(*args, **kwargs):
        print('start decorator1')
        func(*args, **kwargs)
        print('stop decorator1')
    return wrap


def decorator2(func):
    def wrap(*args, **kwargs):
        print('start decorator2')
        func(*args, **kwargs)
        print('stop decorator2')
    return wrap


def decorator3(func):
    def wrap(*args, **kwargs):
        print('start decorator3')
        func(*args, **kwargs)
        print('stop decorator3')
    return wrap


@decorator1
@decorator2
@decorator3
def test_func(num: int):
    print(num)


if __name__ == "__main__":
    test_func(5)

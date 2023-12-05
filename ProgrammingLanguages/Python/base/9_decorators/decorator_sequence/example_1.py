def decorator_1(func):
    def _wrapper(*args, **kwargs):
        print('start decorator_1')
        func(*args, **kwargs)
        print('stop decorator_1')

    return _wrapper


def decorator_2(func):
    def _wrapper(*args, **kwargs):
        print('start decorator_2')
        func(*args, **kwargs)
        print('stop decorator_2')

    return _wrapper


def decorator_3(func):
    def _wrapper(*args, **kwargs):
        print('start decorator_3')
        func(*args, **kwargs)
        print('stop decorator_3')

    return _wrapper


@decorator_1
@decorator_2
@decorator_3
def run():
    print("start function 'run'")


run()


"""
start decorator_1
start decorator_2
start decorator_3
start function 'run'
stop decorator_3
stop decorator_2
stop decorator_1
"""
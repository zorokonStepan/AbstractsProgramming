from datetime import datetime
from functools import wraps


def add_timestamp(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print("@add_timestamp")
        return "{}:{}\n".format(datetime.now(), func(*args, **kwargs))
    return inner_func


def file(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print("@file")
        res = func(*args, **kwargs)
        with open("log.txt", "w") as file:
            file.write(res)
        return res
    return inner_func


def console(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print("@console")
        res = func(*args, **kwargs)
        print(res)
        return res
    return inner_func


@file
@add_timestamp
def log1(msg):
    return msg


@file
@console
@add_timestamp
def log2(msg):
    return msg


@console
@add_timestamp
def log3(msg):
    return msg


log1("log1. This is a test message for file only")
log2("log2. This is a test message for both file and console")
log3("log3. This message is for console only")

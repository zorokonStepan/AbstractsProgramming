import random


class LazyProperty(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value


class WithSortedRandoms:
    @LazyProperty
    def lazily_initialized(self):
        return sorted([[random.random() for _ in range(5)]])

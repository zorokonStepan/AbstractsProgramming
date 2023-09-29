from functools import singledispatchmethod


class Example:

    @singledispatchmethod
    def method(self, argument):
        pass

    @method.register
    def _(self, argument: float):
        pass

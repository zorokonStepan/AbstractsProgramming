def maker(a):
    x = a * 5

    def add(b):
        nonlocal x
        return b + x
    return add


test = maker(6)
print(test(10))

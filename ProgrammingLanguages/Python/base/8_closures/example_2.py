def mul(a):
    def inner(b):
        return a * b
    return inner


mul5 = mul(5)

print(f'{mul5(5) = }')
print(f'{mul5(6) = }')
print(f'{mul5(7) = }')

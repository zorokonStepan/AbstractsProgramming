```
    - Если функция явно не возвращает значение, то функция возвращает None.
    
    - параметры функции: позиционные, *, именованные, **
        ** - tuple
        def func(*, value=value): прием, чтоб использовать только именованные параметры
```

#### lambda
```
    lambda params: result
```

#### Closure
```    
    def main_func(name):
        def inner_func():
            return f'Hello my friend, {name}'
        return inner_func
```

#### Generator Function
```
    def my_range(first=0, last=10, step=1):
        number = first
        
        while number < last:
            yield number
            number += step
```

#### Decorator
```
    def decortor1(func):
        def wrapper(*args, **kwargs):
            print(1)
            func(*args, **kwargs)
            return
        return wrapper    

    def decortor2(func):
        def wrapper(*args, **kwargs):
            print(2)
            func(*args, **kwargs)
            return
        return wrapper  
    
    def decortor3(func):
        def wrapper(*args, **kwargs):
            print(3)
            func(*args, **kwargs)
            return
        return wrapper  
        
    @decortor1
    @decortor2
    @decortor3
    def new_function():
        print('new_function')    
        
    new_function()      
    
    >>> 1
    >>> 2
    >>> 3
    >>> new_function
```
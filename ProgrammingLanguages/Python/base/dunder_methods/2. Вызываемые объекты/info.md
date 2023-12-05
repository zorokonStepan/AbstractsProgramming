```
    __call__(self[, args...]) — позволяет любому экземпляру класса вести себя как обычная функция. Например:
                                >>> class Test:
                                >>>     def __call__(self, message):
                                >>>         print(message)
                                >>>         return True
                                >>>
                                >>> test = Test()
                                >>> test("Hello World")
                                ... 'Hello World'
                                ... True 
                                
    __await__(self) — возвращает итератор, превращая класс в корутину, результат выполнения которой можно получить с 
                      помощью await. Подробнее об этом можно узнать в PEP 492.
```
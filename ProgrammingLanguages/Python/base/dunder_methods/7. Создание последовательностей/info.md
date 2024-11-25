```
    Любой объект может реализовать методы встроенных последовательностей 
    (словари, кортежи, списки, строки и так далее). 
    Доступ к значениям последовательности переопределяется следующими методами:

    __len__(self) — вызывается методом len(...) и возвращает количество элементов в последовательности.
    
    < --------------------------------------------------------------------------------------------------------------- >
    
    __getitem__(self, key) — вызывается при обращении к элементу в последовательности по его ключу (индексу). 
                             Метод должен выбрасывать исключение TypeError, если используется некорректный тип ключа, 
                             KeyError, если данному ключу не соответствует ни один элемент в последовательности. Например:
                             
    >>> list_object = [1, 2, 3, 4, 5]
    >>> print(list_object[0])
    ... 1
    >>>
    >>> string_object = "hello world"
    >>> print(string_object[0:5])
    ... 'hello'
    >>>
    >>> dict_object = {"key0": True, "key1": False}
    >>> print(dict_object["key0"])
    ... True   
    
    < --------------------------------------------------------------------------------------------------------------- >
    
    __setitem__(self, key, value) — вызывается при присваивании какого-либо значения элементу в последовательности. 
                                    Также может выбрасывать исключения TypeError и KeyError. Например:        
                                    
    >>> list_object = [1, 2, 3, 4, 5]
    >>> list_object[0] = 78
    >>> print(list_object)
    ... [78, 2, 3, 4, 5]
    >>>
    >>> dict_object = {"key0": True, "key1": False}
    >>> dict_object["key0"] = False
    >>> print(dict_object)
    ... {"key0": False, "key1": False}    
    
    < --------------------------------------------------------------------------------------------------------------- >                                    
    
    __delitem__(self, key) — вызывается при удалении значения в последовательности по его индексу (ключу) с 
                             помощью синтаксиса ключевого слова del.

    __missing__(self, key) — вызывается в случаях, когда значения в последовательности не существует.
    
    __iter__(self) — вызывается методом iter(...) и возвращает итератор последовательности, 
                     например, для использования объекта в цикле:                                                                                           
                    >>> class Test:
                    >>>     def __iter__(self):
                    >>>         return (1, 2, 3)
                    >>>
                    >>> for value in Test():
                    >>>     print(value)
                    ... 1
                    ... 2
                    ... 3      
                    
    __aiter__(self) - должен возвращать асинхронный итерируемый объект и семантически похож на метод __iter__() простого итератора.
    
    __next__(self) - Метод должен возвращать следующий элемент из контейнера, а если элементы в последовательности 
                     закончились, то метод container.__next__() должен бросить исключение StopIteration.
                     Как только метод container.__next__() итератора вызывает StopIteration, он должен продолжать 
                     вызывать его и при последующих вызовах. Реализации, которые не подчиняются этому свойству, 
                     считаются нарушенными.
    
    __anext__(self) - Асинхронный метод object.__anext__() семантически похож на метод __next__() простого итератора, с 
                      той лишь разницей, что ондолжен возвращать следующее значение итератора в результате awaitable.
                    
    __reversed__(self) — вызывается методом reversed(...) и аналогично методу __iter__ возвращает тот же итератор, 
                         только в обратном порядке.

    __contains__(self, item) — вызывается при проверке принадлежности элемента к последовательности с помощью in или not in.          
    
    < --------------------------------------------------------------------------------------------------------------- >  
    
    object.__length_hint__() вызывается operator.length_hint() - Метод object.__length_hint__() вызывается для 
                    реализации operator.length_hint(). Должен возвращать оценочную длину объекта (которая может быть 
                    больше или меньше фактической длины). Длина должна быть целым числом >= 0. Возвращаемое значение 
                    также может быть NotImplemented, что обрабатывается так же, как если бы метод __length_hint__ 
                    вообще не существовал. Этот метод является чисто оптимизационным и никогда не требуется для 
                    корректности.
                                                             
```

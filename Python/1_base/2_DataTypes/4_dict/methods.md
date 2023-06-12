```
    dict.get(value, [default]) --> return value or default or None
    
    dict.keys()   --> return all keys
    dict.values() --> return all values
    dict.items()  --> return all (key, value), ...
    
    # ОБЪЕДИНИТЬ СЛОВАРИ:
    1. {**a, **b}
    2. a.update(b)
    
    # УДАЛЕНИЕ
    1. del dict[key]
    2. value = dict.pop(key)
    3. dict.clear() --> {}
    
    # ПОВЕРХНОСТНОЕ КОПИРОВАНИЕ
    new_dict = dict.copy()
    
    # ПОЛНОЕ КОПИРОВАНИЕ:
    import copy 

    b = copy.deepcopy(a)
```
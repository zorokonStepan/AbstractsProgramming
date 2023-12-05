```
    list.append(value) - добавить в конец списка
    list.insert(index, value) - добавить на указанный индекс
    list1.extend(list2) - добавить элементы list2 в list1
    
    # УДАЛЕНИЕ
    del list[index]    - удалить элемент списка
    list.remove(value) - удалить элемент списка по значению(первый, если их несколько)
    value = list.pop(index) - default index=-1
    list.clear() --> [] 
    
     # ПОИСК И ВЫБОР   
    list.index(value) --> index
    
    list.count() --> int count
    
    # СОРТИРОВКА
    list1.sort() --> list1 сортирует "на месте"
    list2 = sorted(list1) 
     
    # КОПИРОВАНИЕ
    a = [1, 2, 3]
    
    # ПОВЕРХНОСТНОЕ КОПИРОВАНИЕ:
    b = a.copy()
    c = list(a)
    d = a[:] 
    
    # ПОЛНОЕ КОПИРОВАНИЕ:
    import copy 
    
    a = [1, 2, [8, 9]]
    b = copy.deepcopy(a)
```
```
    set.add(value)    - добавить элемент
    set.remove(value) - удалить элемент
    
    # ПЕРЕСЕЧЕНИЕ
    set3 = set1 & set2
    set3 = set1.intersection(set2)
    
    # ОБЪЕДИНЕНИЕ
    set3 = set1 | set2
    set3 = set1.union(set2)
    
    # РАЗНОСТЬ
    set3 = set1 - set2
    set3 = set1.difference(set2)    
    or     
    set3 = set2 - set1
    set3 = set2.difference(set1)
    
    # исключающего ИЛИ
    set3 = set1 ^ set2
    set3 = set1.symmetric_difference(set2)
    
    # ПОДМНОЖЕСТВА
    set1 <= set2        --> bool
    set1.issubset(set2) --> bool
    
    # НАДМНОЖЕСТВО
    set1 >= set2          --> bool
    set1.issuperset(set2) --> bool   
```
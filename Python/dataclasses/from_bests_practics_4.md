```
    class Vector: 
        def __init__(self, х, у): 
            self.x = х 
            self.y = у 
            
        def __add__(self, other): 
            """Суммирует векторы оператором +'""' 
            return Vector(self .x + other.x, self.y + other.y) 
            
        def __sub__(self, other): 
            """Вычитает векторы оператором 
            return Vector(self.x - other.x, self.y - other.y) 
            
        def __repr__(self): 
            """Возвращает текстовое представление вектора""" 
            returп f"<Vector: x={self.x}, y={self.y}>" 
            
        def __eq__(self, other): 
            """Проверяет два вектора на равенство'""' 
            return self.x == other.x and self.y == other.y 
```

```
    Если в вашей программе много похожих простых классов, которые ориентированы на работу с данными и не требуют 
    сложной инициализации, вы рискуете увязнуть в кучах шаблонного кода для методов __init__(), __repr__() и __еq__(). 
    С модулем dataclasses класс Vector становится намного короче: 
    
    
    from dataclasses import dataclass 
    
    @dataclass 
    class Vector: 
        х: int 
        у: int 
        
        def __add__(self, other): 
            """Суммирует векторы оператором +'""' 
            return Vector(self .x + other.x, self.y + other.y) 
            
        def __sub__(self, other): 
            """Вычитает векторы оператором 
            return Vector(self.x - other.x, self.y - other.y) 
            
    Декоратор класса dataclass читает аннотации атрибутов класса Vector и автоматически создает методы __init__(), 
    __repr__() и __eq__(). Проверка равенства по умолчанию предполагает, что два экземпляра равны, если их 
    соответствующие атрибуты равны друг другу.        
```

```
    Но у классов данных есть и много других полезных возможностей. 
    В частности, можно легко обеспечить их совместимость с другими протоколами Python. 
    Допустим, вы хотите, чтобы экземпляры класса Vector были неизменяемыми: тогда их можно будет использовать как ключи 
    словаря и элементы множеств. Для этого достаточно добавить в декоратор dataclass аргумент frozen=True:  
    
    from dataclasses import dataclass 
    
    @dataclass(frozen=True) 
    class Frozenvector: 
        х: int 
        у: int 
```
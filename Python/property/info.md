```
    class property(fget=None, fset=None, fdel=None, doc=None)
    
    fget=None - функция для получения значения атрибута
    fset=None - функция для установки значения атрибута
    fdel=None - функция для удаления значения атрибута
    doc=None  - строка, для строки документации атрибута
    
    Класс property() позволяет использовать методы в качестве вычисляемых свойств объектов (дескрипторов данных).
    
    Если задана строка doc, то она будет строкой атрибута свойства. В противном случае строка документации будет 
    скопирована из функции fget, если она существует.
    
    Типичное использование класса property() - определить дескриптор (управляемый атрибут) x:
    
        class C:
            def __init__(self):
                self._x = None
        
            def getx(self):
                return self._x
        
            def setx(self, value):
                self._x = value
        
            def delx(self):
                del self._x
        
            x = property(getx, setx, delx, "I'm the 'x' property.")
            
            
        class C:
            def __init__(self):
                self._x = None
        
            @property
            def x(self): 
                """I'm the 'x' property."""
                return self._x
            
            # В декораторах 'setter' и 'deleter' нужно указывать имя метода-свойства
            @x.setter
            def x(self, value):
                self._x = value
        
            @x.deleter
            def x(self):
                del self._x        
```
### Конкатенация строковых литералов
```
    message = 'Привет, ' + 'мир!'
    print(message)
    >>> Привет, мир!
```

### Неявная конкатенация строковых литералов
Когда несколько строковых литералов записаны рядом и разделены пробелами или 
символами табуляции или символами новой строки, Python неявно объединит их
в строковый литерал.
```
    message = '1' '2' '3'
    print(message)
    >>> 123
    
    print('Введите объем '
          'продаж за каждый день и '
          'нажмите Enter.')
    >>> Введите объем продаж за каждый день и нажмите Enter.       
```

### Мультипликация строковых литералов
```
    '10' * 10
    >>> '10101010101010101010'
```
```
    pytest -v
        -v выводит имя каждого теста в новой строке
```

### Пропуск тестов
```
    pytest.skip()
    
    @pytest.mark.skip
```

### Запуск определенных тестов
```
    -k фильтрация тестов по имени
    
    pytest -v examples/test_skip.py -k test_fail
    
    --------
    
    -m маркировка тестов
    
    @pytest.mark.dicttest
    def test_something():
        pass
        
        
    pytest -v test_mark.py -m dicttest
    
    Или запустить все тесты которые не имеют метки
    
    pytest -v test_mark.py -m 'not dicttest'
    
    Pytest принимает сложные выражения с or, and, not.    
```

### Параллельный запуск тестов
```
    pip install pytest-xdist
    
    этот плагин расширяет команднуб строку --numprocesses или -n
    
    pytest -n 4 запустит тестовый набор в 4 параллельных процессах, сохраняя баланс между загруженностью доступных ядер
    
    pytest -n auto автоматически распределит тесты по доступным ядрам
```
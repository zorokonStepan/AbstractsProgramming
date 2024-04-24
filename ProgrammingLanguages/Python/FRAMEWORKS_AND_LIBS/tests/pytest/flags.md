```
    -v или --verbose: подробный вывод информации
        pytest -v 
        
    --tb=no: turn off tracebacks    
    
    --last-failed: перезапуск только упавших тестов
        python -m pytest --last-failed tests/test_prod.py
        
    --capture=no: не скрывать вывод(Чтобы увидеть вывод print() )
        python -m pytest -v --capture=no test_prod.py
        
    -k: запуск определённого теста       
        python -m pytest -v -k "test_basic_param_prod" tests/test_prod.py 
```
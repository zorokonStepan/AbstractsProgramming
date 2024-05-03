```
    -v или --verbose: подробный вывод информации
        pytest -v 
        
    -vv: еще более подробный вывод информации        
        
    --tb=no: turn off tracebacks    
    
    --tb=short: короткий трэйсбэк
    
    --last-failed: перезапуск только упавших тестов
        python -m pytest --last-failed tests/test_prod.py
        
    --capture=no: не скрывать вывод(Чтобы увидеть вывод print() )
        python -m pytest -v --capture=no test_prod.py
    -s: аналог --capture=no 
        
    -k: запуск определённого теста       
        python -m pytest -v -k "test_basic_param_prod" tests/test_prod.py 
        
    --setup-show: показывает порядок проведения tests и fixtures, включая этапы setup и teardown fixtures
    
    --fixtures: показывает список всех доступных fixtures, которые может использовать наш тест.    
    
    --fixtures-per-test: увидеть, какие fixtures используются в каждом тесте и где они определены;
```
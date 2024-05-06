```
    pytest --strict-markers -m smoke
    
    pytest.ini :
    
    [pytest]
    markers =
        smoke: subset of tests
        exception: check for expected exceptions
        finish: all of the "cards finish" related tests
    addopts =
        --strict-markers
```
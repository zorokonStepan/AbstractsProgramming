```
    pytest -v -m "finish and exception"
    
    pytest -v -m "finish and not smoke"

    pytest -v -m "(exception or smoke) and (not finish)"
    
    pytest -v -m smoke -k "not TestFinish"
```
```
    [pytest]
    
    markers =
        <marker_name>: <marker_description>
    addopts =
        --strict-markers : 
            Указывает pytest выдать ошибку, если он видит, что мы используем необъявленный маркер. 
            По умолчанию используется предупреждение
        -ra : 
            Указывает pytest перечислить причину любого теста, который не пройден. 
            К ним относятся fail, error, skip, xfail и xpass.
    xfail_strict = true
        Превращает все пройденные тесты, помеченные xfail, в неудачные тесты, так как наше 
        понимание поведения системы было неверным. Не указывайте это, если хотите, чтобы 
        пройденные тесты xfail приводили к XPASS.
```
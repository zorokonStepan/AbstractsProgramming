### pytest 6
```
    • @pytest.mark.filterwarnings(warning): 
        Этот маркер добавляет фильтр предупреждений к данному тесту.
    
    • @pytest.mark.skip(reason=None):
        Этот маркер пропускает тест по необязательной причине.
    
    • @pytest.mark.skipif(condition, ..., *, reason): 
        Этот маркер пропускает проверку, если какое-либо из условий имеет значение True.
    
    • @pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict):
        Этот маркер сообщает pytest, что мы ожидаем, что тест не пройдет.
    
    • @pytest.mark.parametrize(argnames, argvalues, indirect, ids, scope):
        Этот маркер вызывает тестовую функцию несколько раз, передавая по очереди разные аргументы.
    
    • @pytest.mark.usefixtures(fixturename1, fixturename2, ...):
        Этот маркер помечает тесты как требующие всех указанных приспособлений
```
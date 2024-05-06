```
    Маркеры регистрируются в pytest.ini чтобы отлавливать опечатки при запуске
    
    [pytest]
    markers =
        smoke: subset of tests
        exception: check for expected exceptions
```

### маркер на модуль
```
    pytestmark = pytest.mark.marker_one
    
    or
    
    pytestmark = [pytest.mark.marker_one, pytest.mark.marker_two]
```

### маркер на class 
```
    @pytest.mark.smoke
    class TestFinish:
```

### маркер на parameters
```
    @pytest.mark.parametrize(
        "start_state",
        [
            "todo",
            pytest.param("in prog", marks=pytest.mark.smoke),
            "done",
        ],
    )
    def test_finish_func(cards_db, start_state):
```

### маркер на функцию
```
    @pytest.mark.smoke
    @pytest.mark.exception
    def test_finish_non_existent(cards_db):
        i = 123  # any number will do, db is empty
        with pytest.raises(InvalidCardId):
            cards_db.finish(i)
```
